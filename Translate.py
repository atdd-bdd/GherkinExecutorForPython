import os
import re
import sys

class Translate:
    def __init__(self):
        self.scenarios = {}  # used to check if duplicate scenario names
        self.glueFunctions = {}  # used to make sure only one glue implementation
        self.dataNames = {}  # used to check for duplicate data
        self.dataNamesInternal = {}  # used to check for duplicate data
        self.importNames = {}  # used to hold conversion functions for imports

        self.linesToAddForDataAndGlue = []
        self.linesToAddToEndOfGlue = []
        self.defineNames = {}
        self.stepCount = 0  # use to label duplicate scenarios
        self.glueClass = ""  # glue class name
        self.glueObject = ""  # glue object name

        self.stepNumberInScenario = 0  # use to label variables in scenario
        self.dataIn = InputIterator("", "", self)
        self.firstScenario = True  # If first scenario
        self.addBackground = False  # Have seen Background
        self.addCleanup = False  # have seen Cleanup

        self.inCleanup = False  # Current scenario is Cleanup
        self.finalCleanup = False  # for the last part of scenario
        self.testFile = None

        self.featureActedOn = False  # Have found a feature step
        self.featureName = ""

        self.directoryName = ""
        self.featureDirectory = ""  # if feature file is in a directory
        self.featurePackagePath = ""
        self.packagePath = "Not Set"

        self.classDataNames = []

        self.dataConstruct = DataConstruct()
        self.templateConstruct = TemplateConstruct()
        self.stepConstruct = StepConstruct()
        self.importConstruct = ImportConstruct()
        self.defineConstruct = DefineConstruct()

        self.filterExpression = Configuration.filterExpression
        self.skipSteps = False

        self.scenarioCount = 0  # Number of scenarios encountered
        self.backgroundCount = 0  # Number of backgrounds encountered
        self.cleanupCount = 0  # Number of cleanups encountered

        self.TAG_INDICATOR = "@"
        self.tagLine = ""  # Contains last tag line
        self.tagLineNumber = 0  # Line number for last tag line

    @staticmethod
    def themain(args):
        Translate.print_flow("Gherkin Executor")
        Configuration.current_directory = os.getcwd()
        Translate.process_arguments(args)
        if Configuration.search_tree and Configuration.starting_feature_directory:
            files_in_tree = Translate.find_feature_files(Configuration.starting_feature_directory)
            Translate.print_flow("Adding directory tree files")
            for file in files_in_tree:
                print(file)
            Configuration.feature_files.extend(files_in_tree)
        Translate.read_option_list()
        Translate.read_filter_list()
        Translate.read_feature_list()
        for name in Configuration.feature_files:
            translate = Translate()
            Translate.print_flow(f"Translating {name}")
            translate.translate_in_tests(name)


    def translate_in_tests(self, name):
        self.find_feature_directory(name)

        self.linesToAddForDataAndGlue.extend(Configuration.linesToAddForDataAndGlue)
        self.dataIn = InputIterator(name, self.featureDirectory, self)
        self.alter_feature_directory()
        if self.dataIn.is_empty():
            return

        for pass_num in range(1, 4):
            self.dataIn.reset()
            eof = False
            while not eof:
                line = self.dataIn.next()
                if line == InputIterator.EOF:
                    eof = True
                    continue
                self.act_on_line(line, pass_num)
        self.end_up()

    def alter_feature_directory(self):
        search_for = Configuration.treeDirectory
        alternate_search_for = search_for.replace("/", "\\")
        directory = self.featureDirectory.replace(search_for, "")
        directory = directory.replace(alternate_search_for, "")
        self.featureDirectory = directory
        self.featurePackagePath = self.featureDirectory.replace("\\", ".").replace("/", ".")

    def find_feature_directory(self, name):
        directory = ""
        index_forward = name.rfind('/')
        index_back = name.rfind('\\')
        index = max(index_forward, index_back)
        if index >= 0:
            directory = name[:index + 1]
        self.featureDirectory = directory
        self.featurePackagePath = self.featureDirectory.replace("\\", ".").replace("/", ".")

        def act_on_line(self, line, pass_num):
            words, comment = self.split_line(line, pass_num)
            if words:
                keyword = self.word_without_colon(words[0])
                if keyword == "*":
                    keyword = "Star"
                words[0] = keyword
                self.act_on_keyword(keyword, words, comment, pass_num)

        def split_line(self, line, pass_num):
            all_words = line.split(" ")
            words = []
            comment = []
            if (pass_num == 3 or pass_num == 2) and line.strip().startswith(self.TAG_INDICATOR):
                self.tagLine = line
                self.tagLineNumber = self.dataIn.get_line_number()
            in_comment = False
            for a_word in all_words:
                word = a_word.strip()
                if not word:
                    continue
                if word.endswith(":"):
                    word = self.word_without_colon(word)
                if not word:
                    continue
                if in_comment:
                    comment.append(word)
                    continue
                if word.startswith("#"):
                    in_comment = True
                    word = self.word_without_hash(word)
                    if word:
                        comment.append(word)
                    continue
                word = self.filter_word(word)
                words.append(word)
            return words, comment

        @staticmethod
        def filter_word(input):
            if input is None:
                return ""
            return re.sub(r"[^0-9a-zA-Z_*]", "", input)

        @staticmethod
        def word_without_colon(word):
            return re.sub(r"^:+|:+$", "", word)

        @staticmethod
        def word_without_hash(word):
            return re.sub(r"^#+|#+$", "", word)

    def act_on_keyword(self, keyword, words, comment, pass_num):
        full_name = self.make_full_name(words)
        self.trace(f"Act on keyword {keyword} {full_name} words {words} pass {pass_num}")

        if keyword == "Star":
            if words[1] in ["Data", "Import", "Define", "Cleanup"]:
                keyword = words[1]
                words.pop(0)

        if keyword == "Feature" and pass_num == 2:
            self.act_on_feature(full_name)
            if TagFilterEvaluator.should_not_execute(comment, self.filterExpression):
                self.dataIn.go_to_end()
                print(" Skip Entire Feature ")
        elif keyword == "Scenario" and pass_num == 3:
            if TagFilterEvaluator.should_not_execute(comment, self.filterExpression):
                self.skipSteps = True
            else:
                self.skipSteps = False
                self.act_on_scenario(full_name)
                self.inCleanup = False
        elif keyword == "Background":
            self.addBackground = True
            if pass_num == 3:
                self.skipSteps = False
                self.act_on_background(full_name)
                self.inCleanup = True
        elif keyword == "Cleanup":
            self.addCleanup = True
            if pass_num == 3:
                self.skipSteps = False
                self.act_on_cleanup(full_name)
                self.inCleanup = True
        elif keyword in ["But", "Given", "When", "Then", "And", "Star", "Arrange", "Act", "Assert", "Rule",
                         "Calculation"]:
            if pass_num == 3 and not self.skipSteps:
                self.stepConstruct.act_on_step(full_name, comment)
        elif keyword == "Data" and pass_num == 2:
            self.skipSteps = False
            self.dataConstruct.act_on_data(words)
        elif keyword == "Import" and pass_num == 1:
            self.skipSteps = False
            self.importConstruct.act_on_import(words)
        elif keyword == "Define" and pass_num == 1:
            self.skipSteps = False
            self.defineConstruct.act_on_define(words)

    def check_for_tag_line(self):
        if not self.tagLine:
            return

        if self.tagLineNumber + 1 == self.dataIn.get_line_number():
            self.test_print(self.tagLine)
        self.tagLine = ""
        self.tagLineNumber = 0


import os
import re


class Translate:
    def __init__(self, data_in, package_path, feature_directory, feature_package_path):
        self.data_in = data_in
        self.package_path = package_path
        self.feature_directory = feature_directory
        self.feature_package_path = feature_package_path
        self.feature_name = ""
        self.feature_acted_on = False
        self.test_file = None
        self.template_construct = None  # Assuming this is defined elsewhere
        self.glue_class = ""
        self.glue_object = ""

    def write_input_feature(self, filename):
        full_filename = f"{filename}feature.txt"
        self.print_flow(f"Logging to {full_filename}")
        try:
            with open(full_filename, 'w') as my_log:
                my_log.write(str(self.data_in))
        except IOError as e:
            print(f"{e} Cause {e.__cause__}")
            print(f"**** Cannot write to {full_filename}")

    @staticmethod
    def make_full_name(words):
        temp = "_".join(words)
        temp = re.sub(r'[^A-Za-z0-9_]', '_', temp)
        return temp

    def act_on_feature(self, full_name):
        if self.act_on_feature_first_half(full_name):
            return
        self.test_print(f"package {self.package_path};")
        test_framework = Configuration.test_framework
        if test_framework == "JUnit4":
            self.test_print("import org.junit.*;")
        elif test_framework == "TestNG":
            self.test_print("import org.testng.annotations.*;")
        else:
            self.test_print("import org.junit.jupiter.api.*;")
        self.test_print("import java.util.List;")
        if Configuration.log_it:
            self.test_print("import java.io.FileWriter;")
            self.test_print("import java.io.IOException;")
        self.check_for_tag_line()
        self.test_print(f"class {full_name}{{")
        self.test_print(self.log_it())
        self.test_print("")
        self.template_construct.begin_template()

    def act_on_feature_first_half(self, full_name):
        if self.feature_acted_on:
            self.warning(f"Feature keyword duplicated - it is ignored {full_name}")
            return True
        self.feature_name = full_name
        self.feature_acted_on = True
        self.package_path = f"{Configuration.add_to_package_name}{Configuration.package_name}.{self.feature_package_path}{self.feature_name}"
        self.print_flow(f"Package is {self.package_path}")
        test_pathname = f"{Configuration.test_sub_directory}{self.feature_directory}{self.feature_name}/{self.feature_name}.java"
        self.print_flow(f"Writing {test_pathname}")
        template_filename = f"{Configuration.test_sub_directory}{self.feature_directory}{self.feature_name}/{self.feature_name}_glue.tmpl"
        directory_name = f"{Configuration.test_sub_directory}{self.feature_directory}{self.feature_name}"
        self.print_flow(f"Directory {directory_name} ")
        try:
            os.makedirs(directory_name, exist_ok=True)
            self.test_file = open(test_pathname, 'w')
            self.template_construct.glue_template_file = open(template_filename, 'w')
        except IOError as e:
            self.error("IO Exception in setting up the files")
            self.error(f"Writing {test_pathname}")
        self.glue_class = f"{full_name}_glue"
        self.glue_object = f"{self.make_name(full_name)}_glue_object"
        self.write_input_feature(f"{Configuration.test_sub_directory}{self.feature_directory}{self.feature_name}/")
        return False

    @staticmethod
    def make_build_name(s):
        temp = Translate.make_name(s)
        temp = temp.capitalize()
        return f"set{temp}"

    @staticmethod
    def make_name(input):
        if not input:
            return "NAME_IS_EMPTY"
        temp = input.replace(" ", "_")
        temp = Translate.filter_word(temp)
        return temp[0].lower() + temp[1:]

    def act_on_scenario(self, full_name):
        self.scenario_count += 1
        full_name_to_use = full_name
        if full_name in self.scenarios:
            full_name_to_use += str(self.scenario_count)
            self.error(f"Scenario name duplicated renamed {full_name_to_use}")
        else:
            self.scenarios[full_name_to_use] = ""

        self.step_number_in_scenario = 0
        self.final_cleanup = self.add_cleanup
        if self.first_scenario:
            self.first_scenario = False
        else:
            if self.add_cleanup and not self.in_cleanup:
                self.test_print(f"        test_Cleanup({self.glue_object}); // from previous")
            self.test_print("        }")  # end previous scenario

        self.check_for_tag_line()
        self.test_print(f"    @Test")
        self.test_print(f"    void test_{full_name_to_use}(){{")
        self.test_print(f"         {self.glue_class} {self.glue_object} = new {self.glue_class}();")

        if Configuration.log_it:
            self.test_print(f"        log(\"{full_name_to_use}\");")
        if self.add_background:
            self.test_print(f"        test_Background({self.glue_object});")

    def act_on_background(self, full_name):
        self.background_count += 1
        full_name_to_use = full_name
        self.final_cleanup = False
        if self.background_count > 1:
            self.error("More than one Background statement")
            full_name_to_use += str(self.background_count)

        self.step_number_in_scenario = 0

        if self.first_scenario:
            self.first_scenario = False
        else:
            self.test_print("        }")  # end previous scenario

        self.test_print(f"    void test_{full_name_to_use}({self.glue_class} {self.glue_object}){{")
        if Configuration.log_it:
            self.test_print(f"        log(\"{full_name_to_use}\");")

    def act_on_cleanup(self, full_name):
        self.cleanup_count += 1
        self.final_cleanup = False
        full_name_to_use = full_name
        if self.cleanup_count > 1:
            self.error("More than one cleanup statement")
            full_name_to_use += str(self.cleanup_count)

        self.step_number_in_scenario = 0

        if self.first_scenario:
            self.first_scenario = False
        else:
            self.test_print("        }")  # end previous scenario

        self.test_print(f"    void test_{full_name_to_use}({self.glue_class} {self.glue_object}){{")
        if Configuration.log_it:
            self.test_print(f"        log(\"{full_name_to_use}\");")

    def log_it(self):
        if Configuration.log_it:
            filename = os.path.join(self.directory_name, "log.txt")
            return f"""
            def log(value):
               try:
               with open("{filename}", "a") as my_log:
               my_log.write(value + "\\n")
             except IOError:
                print("*** Cannot write to log", file=sys.stderr)
            """
        else:
            return ""

    def trace(self, value):
        if Configuration.trace_on:
            print(value)

    def error(self, value):
        print(f"[GherkinExecutor] ~ line {self.data_in.get_line_number()} in feature.txt {value} ", file=sys.stderr)
        self.error_occurred = True

    def warning(self, value):
        print(f"[GherkinExecutor] Warning ~ line {self.data_in.get_line_number()} in feature.txt {value}",
              file=sys.stderr)

    @staticmethod
    def print_flow(value):
        print(value)

    def test_print(self, line):
        try:
            self.test_file.write(line + "\n")
        except IOError:
            self.error("IO ERROR")

    def parse_line(self, line):
        line_short = line.strip()
        if line_short[0] == '|':
            line_short = line_short[1:]
        else:
            self.error(f"table not begin with | {line}")
            return ["ERROR IN TABLE LINE " + line]

        last = len(line_short) - 1
        if last < 0:
            self.error(f"table format error {line}")
            return ["ERROR IN TABLE LINE " + line]

        if line_short[last] == '|':
            line_short = line_short[:last]
        else:
            self.error(f"table not end with | {line}")

        elements = line_short.split('|')
        elements_trimmed = [self.replace_defines(element.strip().replace(Configuration.space_characters, ' ')) for
                            element in elements]
        return elements_trimmed

    def look_for_follow(self):
        line = self.data_in.peek()
        empty = []
        while line and line[0] == '#':
            self.data_in.next()
            line = self.data_in.peek()

        line = line.strip()
        if not line:
            return "NOTHING", empty

        if line[0] == '|':
            ret_value = self.read_table()
            self.trace(f"Table is {ret_value}")
            return "TABLE", ret_value

        if line == '"""':
            ret_value = self.read_string()
            self.trace(f"Multi Line String is {ret_value}")
            return "STRING", ret_value

        return "NOTHING", empty

    def read_table(self):
        ret_value = []
        line = self.data_in.peek().strip()
        line = line.split("#")[0].strip()
        while line and (line[0] == '|' or line[0] == '#'):
            line = self.data_in.next().strip()
            line = line.split("#")[0].strip()
            if line[0] == '|' and line.endswith("|"):
                ret_value.append(line)
            else:
                self.error(f"Invalid line in table {line}")
            line = self.data_in.peek().strip()
        return ret_value

    def read_string(self):
        ret_value = []
        first_line = self.data_in.peek()
        count_indent = self.count_indent(first_line)
        self.data_in.next()
        line = self.data_in.next()
        while line.strip() != "\"\"\"":
            ret_value.append(line[count_indent:])
            line = self.data_in.next()
        return ret_value

    def replace_defines(self, in_string):
        did_replacement = True
        change_string = in_string
        while did_replacement:
            did_replacement = False
            for name, replacement in define_names.items():
                if name in change_string:
                    did_replacement = True
                    change_string = change_string.replace(name, replacement)
        return change_string

    @staticmethod
    def count_indent(first_line):
        line = first_line.strip()
        return len(first_line) - len(line)

    @staticmethod
    def find_feature_files(directory):
        feature_files = []
        Translate.collect_feature_files(os.path.join(directory), feature_files)
        return feature_files

    @staticmethod
    def read_filter_list():
        filepath = os.path.join(Configuration.feature_sub_directory, "filter.txt")
        Translate.print_flow(f"Path is {filepath}")
        try:
            raw = open(filepath).readlines()
        except Exception as e:
            print(f"Error: Unable to read {e} {filepath}")
            return
        arguments = [""]
        arguments = raw
        Configuration.filter_expression = arguments[0]
        print(f"Filter is {arguments[0]}")

    @staticmethod
    def read_option_list():
        filepath = os.path.join(Configuration.feature_sub_directory, "options.txt")
        Translate.print_flow(f"Path is {filepath}")
        try:
            raw = open(filepath).readlines()
        except Exception as e:
            print(f"Error: Unable to read {e} {filepath}")
            return
        arguments = [""]
        arguments = raw
        Translate.process_arguments(arguments)

    @staticmethod
    def read_feature_list():
        filepath = os.path.join(Configuration.feature_sub_directory, "features.txt")
        Translate.print_flow(f"Path is {filepath}")
        try:
            raw = open(filepath).readlines()
        except Exception as e:
            print(f"Unable to read {filepath}")
            return
        Configuration.feature_files.extend(raw)

    @staticmethod
    def collect_feature_files(dir, feature_files):
        remove = Configuration.feature_sub_directory.replace("/", "\\")
        if os.path.isdir(dir):
            for file in os.listdir(dir):
                file_path = os.path.join(dir, file)
                if os.path.isdir(file_path):
                    Translate.collect_feature_files(file_path, feature_files)
                elif file.endswith(".feature"):
                    path = file_path.replace(remove, "")
                    feature_files.append(path)


    @staticmethod
    def process_arguments(args):
        Translate.print_flow("Optional arguments are logIt inTest searchTree traceOn")
        filter_next = False
        for arg in args:
            Translate.print_flow(f"Program argument: {arg}")
            if arg == "logIt":
                Configuration.log_it = True
                Translate.print_flow("logIt on")
            elif arg == "inTest":
                Configuration.in_test = True
                Translate.print_flow("inTest on")
            elif arg == "traceOn":
                Configuration.trace_on = True
                Translate.print_flow("traceOn true")
            elif arg == "searchTree":
                Configuration.search_tree = True
                Translate.print_flow("searchTree on")
            elif arg == "--filter":
                filter_next = True
            else:
                if filter_next:
                    filter_next = False
                    Configuration.filter_expression = arg
                else:
                    Configuration.feature_files.append(arg)

    @staticmethod
    def quote_it(default_val):
        return f'"{default_val}"'

    @staticmethod
    def from_import_data(data_type, value):
        if data_type in import_names:
            conversion_method = import_names[data_type].replace("$", value)
            return conversion_method
        return ""

    @staticmethod
    def make_value_from_string(variable, make_name_value):
        if make_name_value:
            value = Translate.make_name(variable.name)
        else:
            value = Translate.quote_it(variable.default_val)

        data_type = variable.data_type
        if data_type == "String":
            return value
        elif data_type == "int":
            return f"int({value})"
        elif data_type == "double":
            return f"float({value})"
        elif data_type == "byte":
            return f"bytes({value})"
        elif data_type == "short":
            return f"int({value})"
        elif data_type == "long":
            return f"int({value})"
        elif data_type == "float":
            return f"float({value})"
        elif data_type in ["boolean", "Boolean"]:
            return f"bool({value})"
        elif data_type == "char":
            return f"({value}[0] if len({value}) > 0 else ' ')"
        elif data_type == "Byte":
            return f"bytes({value})"
        elif data_type == "Short":
            return f"int({value})"
        elif data_type == "Integer":
            return f"int({value})"
        elif data_type == "Long":
            return f"int({value})"
        elif data_type == "Float":
            return f"float({value})"
        elif data_type == "Double":
            return f"float({value})"
        elif data_type == "Character":
            return f"({value}[0] if len({value}) > 0 else ' ')"
        else:
            result = Translate.from_import_data(data_type, value)
            if result:
                return result
            return f"{data_type}({value})"  # Data type not found

    @staticmethod
    def print_flow(message):
        print(message)

    @staticmethod
    def find_feature_files(directory):
        feature_files = []
        Translate.collect_feature_files(directory, feature_files)
        return feature_files

    @staticmethod
    def read_option_list():
        filepath = os.path.join(Configuration.feature_sub_directory, "options.txt")
        Translate.print_flow(f"Path is {filepath}")
        try:
            raw = open(filepath).readlines()
        except Exception as e:
            print(f"Error: Unable to read {e} {filepath}")
            return
        arguments = raw
        Translate.process_arguments(arguments)

    @staticmethod
    def read_filter_list():
        filepath = os.path.join(Configuration.feature_sub_directory, "filter.txt")
        Translate.print_flow(f"Path is {filepath}")
        try:
            raw = open(filepath).readlines()
        except Exception as e:
            print(f"Error: Unable to read {e} {filepath}")
            return
        Configuration.filter_expression = raw[0]
        print(f"Filter is {raw[0]}")

    @staticmethod
    def read_feature_list():
        filepath = os.path.join(Configuration.feature_sub_directory, "features.txt")
        Translate.print_flow(f"Path is {filepath}")
        try:
            raw = open(filepath).readlines()
        except Exception as e:
            print(f"Unable to read {filepath}")
            return
        Configuration.feature_files.extend(raw)

    def end_up(self):
        if self.final_cleanup:
            self.test_print(f"        test_Cleanup({self.glue_object}); // at the end")
        if self.scenario_count == 0:
            print("No scenarios")
        else:
            self.test_print("        }")  # End last scenario
        self.test_print("    }")  # End the class
        self.test_print("")
        try:
            self.test_file.close()
        except IOError:
            self.error("Error in closing")

        self.template_construct.end_template()
        if self.error_occurred:
            print("*** Error in translation, scan the output", file=sys.stderr)
            sys.exit(-1)
        self.data_construct.end_one_data_file()

    def test_print(self, line):
        try:
            self.test_file.write(line + "\n")
        except IOError:
            self.error("IO ERROR")

    class InputIterator:
        EOF = "EOF"

        def __init__(self, name, feature_directory, outer):
            self.outer = outer
            self.lines_in = []
            self.index = 0
            self.feature_directory = feature_directory
            if name:
                self.read_file(name, 0)

        def get_line_number(self):
            return self.index

        def __str__(self):
            return "\n".join(self.lines_in)

        def read_file(self, file_name, include_count):
            include_count += 1
            if include_count > 20:
                self.outer.error("Too many levels of include")
                return
            try:
                filepath = os.path.join(Configuration.feature_sub_directory, file_name)
                Translate.print_flow(f"Path is {filepath}")
                try:
                    raw = open(filepath).readlines()
                except Exception as e:
                    self.outer.error(f"Unable to read {filepath}")
                    return
                for line in raw:
                    if line.startswith("Include"):
                        parts = line.split("\"")
                        self.outer.trace(f"Parts are {', '.join(parts)}")
                        local_file = True
                        if len(parts) < 2:
                            parts = line.split("'")
                            local_file = False
                            if len(parts) < 2:
                                self.outer.error(f"Error filename not surrounded by quotes: {line}")
                                continue
                        if not parts[1]:
                            self.outer.error(f"Error zero length filename {line}")
                            continue
                        included_file_name = parts[1].strip()
                        if local_file:
                            included_file_name = os.path.join(self.feature_directory, included_file_name)
                        self.outer.trace(f"Including {included_file_name}")
                        if included_file_name.endswith(".csv"):
                            self.include_csv_file(included_file_name)
                        else:
                            self.read_file(included_file_name, include_count)
                    else:
                        if line and line[0] != '#':
                            self.lines_in.append(line.strip())
            except Exception as e:
                print(e)
            include_count -= 1

        def include_csv_file(self, included_file_name):
            try:
                raw = open(os.path.join(Configuration.feature_sub_directory, included_file_name)).readlines()
                for line in raw:
                    if line:
                        contents = self.convert_csv_to_table(line)
                        self.lines_in.append(contents.strip())
            except IOError as e:
                print(e)

        def convert_csv_to_table(self, csv_data):
            lines = csv_data.split("\n")
            data = [self.parse_csv_line(line) for line in lines]
            formatted_data = ["|" + "|".join(row) + "|" for row in data]
            return "\n".join(formatted_data)

        def parse_csv_line(self, line):
            result = []
            current = []
            in_quotes = False

            length = len(line)
            i = 0
            while i < length:
                c = line[i]
                if c == '"':
                    if in_quotes and i + 1 < length and line[i + 1] == '"':
                        current.append('"')
                        i += 1
                    else:
                        in_quotes = not in_quotes
                elif c == ',' and not in_quotes:
                    result.append("".join(current))
                    current = []
                else:
                    current.append(c)
                i += 1
            result.append("".join(current))
            return result

        def peek(self):
            if self.index < len(self.lines_in):
                return self.lines_in[self.index]
            else:
                return self.EOF

        def next(self):
            if self.index < len(self.lines_in):
                self.index += 1
                return self.lines_in[self.index - 1]
            else:
                return self.EOF

        def go_to_end(self):
            self.index = len(self.lines_in)

        def is_empty(self):
            return not self.lines_in

        def reset(self):
            self.index = 0

    class StepConstruct:
        def __init__(self, outer):
            self.outer = outer
            self.step_number_in_scenario = 0

        def act_on_step(self, full_name, comment):
            self.step_number_in_scenario += 1
            follow = self.outer.look_for_follow()
            follow_type = follow.get_first()
            table = follow.get_second()
            self.outer.test_print("")
            if follow_type == "TABLE":
                self.create_the_table(comment, table, full_name)
            elif follow_type == "NOTHING":
                self.outer.no_parameter(full_name)
            elif follow_type == "STRING":
                self.create_the_string_code(comment, table, full_name)
            else:
                self.outer.error(f"Internal Error - Follow type {follow_type}")

        def create_the_string_code(self, comment, table, full_name):
            option = "String"
            if comment and comment[0]:
                option = comment[0]
            if option == "ListOfString":
                self.string_to_list(table, full_name)
            else:
                self.string_to_string(table, full_name)

        def string_to_list(self, table, full_name):
            s = str(self.step_number_in_scenario)
            data_type = "List[str]"
            data_type_initializer = "list"
            self.outer.test_print(f"        {data_type} string_list{s} = {data_type_initializer}(")
            comma = ""
            for line in table:
                self.outer.test_print(f"            {comma}\"{line}\"")
                comma = ","
            self.outer.test_print("            )")
            self.outer.test_print(f"        {self.outer.glue_object}.{full_name}(string_list{s})")
            self.outer.template_construct.make_function_template_is_list(data_type, full_name, "String")

        def string_to_string(self, table, full_name):
            s = str(self.step_number_in_scenario)
            self.outer.test_print(f"        str string{s} =")
            self.outer.test_print("            \"\"\"")
            for line in table:
                self.outer.test_print(f"            {line}")
            self.outer.test_print("            \"\"\".strip()")
            self.outer.test_print(f"        {self.outer.glue_object}.{full_name}(string{s})")
            self.outer.template_construct.make_function_template("String", full_name)

        def table_to_list_of_list_of_object(self, table, full_name, class_name):
            s = str(self.step_number_in_scenario)
            data_type = "List[List[str]]"
            data_type_initializer = "list"

            self.outer.test_print(f"        {data_type} string_list_list{s} = {data_type_initializer}(")
            comma = ""
            for line in table:
                self.outer.convert_bar_line_to_list(line, comma)
                comma = ","
            self.outer.test_print("            )")
            self.outer.test_print(f"        {self.outer.glue_object}.{full_name}(string_list_list{s})")
            self.outer.template_construct.make_function_template_object(data_type, full_name, class_name)
            self.create_convert_table_to_list_of_list_of_object_method(class_name)

        def table_to_list_of_list(self, table, full_name):
            s = str(self.step_number_in_scenario)
            data_type = "List[List[str]]"
            data_type_initializer = "list"

            self.outer.test_print(f"        {data_type} string_list_list{s} = {data_type_initializer}(")
            comma = ""
            for line in table:
                self.outer.convert_bar_line_to_list(line, comma)
                comma = ","
            self.outer.test_print("            )")
            self.outer.test_print(f"        {self.outer.glue_object}.{full_name}(string_list_list{s})")
            self.outer.template_construct.make_function_template_is_list(data_type, full_name, "List[str]")

        def create_the_table(self, comment, table, full_name):
            option = "ListOfList"
            class_name = None
            if comment and comment[0]:
                option = comment[0]
            if option == "ListOfList":
                self.table_to_list_of_list(table, full_name)
            elif option == "ListOfListOfObject":
                if len(comment) < 2:
                    self.outer.error("No class name specified")
                    return
                class_name = comment[1]
                self.table_to_list_of_list_of_object(table, full_name, class_name)
            elif option in ["String", "string"]:
                self.outer.table_to_string(table, full_name)
            elif option == "ListOfObject":
                if len(comment) < 2:
                    self.outer.error("No class name specified")
                    return
                class_name = comment[1]
                transpose = False
                compare = False
                if len(comment) > 2:
                    action = comment[2]
                    if action.lower() == "compare":
                        compare = True
                    elif action.lower() == "transpose":
                        transpose = True
                    else:
                        self.outer.error(f"Action not recognized {action}")
                self.outer.table_to_list_of_object(table, full_name, class_name, transpose, compare)
            else:
                self.outer.error(f"Option not found, default to ListOfList {option}")
                self.table_to_list_of_list(table, full_name)

        def create_convert_table_to_list_of_list_of_object_method(self, to_class):
            variable = DataConstruct.DataValues("s", "s", to_class)
            convert = self.outer.make_value_from_string(variable, True)

            template = f"""
            public static List<List<{to_class}>> convert_list(List[List[str]] string_list) {{
                List<List<{to_class}>> class_list = new ArrayList<>();
                for (List[str] inner_list : string_list) {{
                    List<{to_class}> inner_class_list = new ArrayList<>();
                    for (str s : inner_list) {{
                        inner_class_list.add({convert});
                    }}
                    class_list.add(inner_class_list);
                }}
                return class_list;
            }}
            """.strip()
            self.outer.lines_to_add_to_end_of_glue.append(template)

        def create_convert_table_to_list_of_list_of_object_method(self, to_class):
            variable = DataConstruct.DataValues("s", "s", to_class)
            convert = self.outer.make_value_from_string(variable, True)

            template = f"""
            public static List<List<{to_class}>> convert_list(List[List[str]] string_list) {{
                List<List<{to_class}>> class_list = new ArrayList<>();
                for (List[str] inner_list : string_list) {{
                    List<{to_class}> inner_class_list = new ArrayList<>();
                    for (str s : inner_list) {{
                        inner_class_list.add({convert});
                    }}
                    class_list.add(inner_class_list);
                }}
                return class_list;
            }}
            """.strip()
            self.outer.lines_to_add_to_end_of_glue.append(template)

        def table_to_string(self, table, full_name):
            s = str(self.step_number_in_scenario)
            self.outer.test_print(f"        str table{s} =")
            self.outer.test_print("            \"\"\"")
            for line in table:
                self.outer.test_print(f"            {line}")
            self.outer.test_print("            \"\"\".strip()")
            self.outer.test_print(f"        {self.outer.glue_object}.{full_name}(table{s})")
            self.outer.template_construct.make_function_template("String", full_name)

        def convert_bar_line_to_list(self, line_in, comma_in):
            line = line_in.split("#")[0].strip()
            self.outer.test_print(f"           {comma_in}list(")
            elements = self.outer.parse_line(line)
            comma = ""
            for element in elements:
                self.outer.test_print(f"            {comma}\"{element}\"")
                comma = ","
            self.outer.test_print("            )")

        def table_to_list_of_object(self, table, full_name, class_name, transpose, compare):
            self.outer.trace(f"TableToListOfObject classNames {class_name}")
            s = str(self.step_number_in_scenario)
            data_type = f"List[{class_name}]"
            data_type_initializer = "list("
            self.outer.test_print(f"        {data_type} object_list{s} = {data_type_initializer}")
            in_header_line = True
            data_list = self.convert_to_list_list(table, transpose)
            headers = []
            comma = ""
            for row in data_list:
                if in_header_line:
                    headers = row
                    for data_name in row:
                        if not self.find_data_class_name(class_name, self.outer.make_name(data_name)):
                            self.outer.error(f"Data name {data_name} not in Data for {class_name}")
                    in_header_line = False
                    continue

                self.convert_bar_line_to_parameter(headers, row, class_name, comma, compare)
                comma = ","
            self.outer.test_print("            )")
            self.outer.test_print(f"        {self.outer.glue_object}.{full_name}(object_list{s})")
            self.outer.template_construct.make_function_template_is_list(data_type, full_name, class_name)

        def convert_to_list_list(self, table, transpose):
            temporary = [self.outer.parse_line(line) for line in table]
            result = temporary
            if transpose:
                result = self.transpose(temporary)
            return result

        def find_data_class_name(self, class_name, data_name):
            compare = f"{class_name}#{data_name}"
            return compare in self.outer.class_data_names

        def convert_bar_line_to_parameter(self, headers, values, class_name, comma, compare):
            self.outer.trace(f"Headers {headers}")
            size = min(len(headers), len(values))
            if len(headers) > len(values):
                self.outer.error(f"not sufficient values, using what is there {values}")
            self.outer.test_print(f"            {comma} new {class_name}.Builder()")
            if compare:
                self.outer.test_print("             .setCompare()")
            for i in range(size):
                value = f"\"{values[i].replace(Configuration.space_characters, ' ')}\""
                self.outer.test_print(f"                .{self.outer.make_build_name(headers[i])}({value})")
            self.outer.test_print("                .build()")

        def no_parameter(self, full_name):
            self.outer.test_print(f"        {self.outer.glue_object}.{full_name}()")
            self.outer.template_construct.make_function_template_nothing("", full_name)

        def transpose(self, matrix):
            transposed = []
            for i in range(len(matrix[0])):
                row = [matrix[j][i] for j in range(len(matrix))]
                transposed.append(row)
            return transposed

    class TemplateConstruct:
        def __init__(self, outer):
            self.outer = outer
            self.glue_template_file = None
            self.glue_functions = {}
            self.package_path = ""
            self.lines_to_add_for_data_and_glue = []
            self.lines_to_add_to_end_of_glue = []
            self.glue_class = ""
            self.test_file = None

        def template_print(self, line):
            try:
                self.glue_template_file.write(line + "\n")
            except IOError:
                self.outer.error("IO ERROR")

        def make_function_template_object(self, data_type, full_name, list_element):
            if self.check_for_existing_template(data_type, full_name):
                return  # already have a prototype
            self.glue_functions[full_name] = data_type
            self.template_print(f"    def {full_name}(self, values: {data_type}) -> None:")
            self.template_print(f"        is = self.convert_list(values)")
            self.template_print("        print(is)")
            if Configuration.log_it:
                self.template_print(f"        self.log(\"---  \" + \"{full_name}\")")
            if not Configuration.in_test:
                self.template_print("        raise NotImplementedError(\"Must implement\")")
            self.template_print("")

        def check_for_existing_template(self, data_type, full_name):
            if full_name in self.glue_functions:
                current_data_type = self.glue_functions[full_name]
                if current_data_type != data_type:
                    self.outer.error(f"function {full_name} datatype {current_data_type} not equals {data_type}")
                    return True
                return True
            return False

        def make_function_template_nothing(self, data_type, full_name):
            if self.check_for_existing_template(data_type, full_name):
                return  # already have a prototype
            self.glue_functions[full_name] = data_type
            self.template_print(f"    def {full_name}(self) -> None:")
            self.template_print(f"        print(\"---  \" + \"{full_name}\")")
            if Configuration.log_it:
                self.template_print(f"        self.log(\"---  \" + \"{full_name}\")")
            if not Configuration.in_test:
                self.template_print("        raise NotImplementedError(\"Must implement\")")
            self.template_print("")

        def make_function_template_is_list(self, data_type, full_name, list_element):
            if self.check_for_existing_template(data_type, full_name):
                return  # already have a prototype
            self.glue_functions[full_name] = data_type
            self.template_print(f"    def {full_name}(self, values: {data_type}) -> None:")
            self.template_print(f"        print(\"---  \" + \"{full_name}\")")
            if Configuration.log_it:
                self.template_print(f"        self.log(\"---  \" + \"{full_name}\")")
                self.template_print("        self.log(str(values))")
            name = f"{list_element}Internal"
            self.template_print(f"        for value in values:")
            self.template_print("             print(value)")
            self.template_print("             # Add calls to production code and asserts")
            if data_type != "List[List[str]]" and list_element != "String" and name in self.outer.data_names_internal:
                self.template_print(f"              i = value.to{name}()")
            self.template_print("        if not Configuration.in_test:")
            self.template_print("            raise NotImplementedError(\"Must implement\")")
            self.template_print("")

        def make_function_template(self, data_type, full_name):
            if self.check_for_existing_template(data_type, full_name):
                return  # already have a prototype
            self.glue_functions[full_name] = data_type
            self.template_print(f"    def {full_name}(self, value: {data_type}) -> None:")
            self.template_print(f"        print(\"---  \" + \"{full_name}\")")
            if Configuration.log_it:
                self.template_print(f"        self.log(\"---  \" + \"{full_name}\")")
                self.template_print("        self.log(str(value))")
            self.template_print("        print(value)")
            if not Configuration.in_test:
                self.template_print("        raise NotImplementedError(\"Must implement\")")
            self.template_print("")


        def beginTemplate(self):
            self.templatePrint(f"package {self.packagePath};")
            for line in self.linesToAddForDataAndGlue:
                self.templatePrint(line)
            if self.Configuration["testFramework"] == "JUnit4":
                self.templatePrint("import static org.junit.Assert.*;")
            elif self.Configuration["testFramework"] == "TestNG":
                self.templatePrint("import static org.testng.Assert.*;")
            else:
                self.templatePrint("import static org.junit.jupiter.api.Assertions.*;")
            self.templatePrint("import java.util.List;")
            if self.Configuration["logIt"]:
                self.templatePrint("import java.io.FileWriter;")
                self.templatePrint("import java.io.IOException;")
            self.templatePrint("")
            self.templatePrint(f"class {self.glueClass} {{")
            self.templatePrint(f'    final String DNCString = "{self.Configuration["doNotCompare"]}";')
            self.templatePrint(self.logIt())
            self.templatePrint("")

        def endTemplate(self):
            for line in self.linesToAddToEndOfGlue:
                self.templatePrint(line)
            self.templatePrint("    }")  # End the class
            try:
                self.testFile.close()
                self.glueTemplateFile.close()
            except IOError as e:
                print(f"Error in closing: {e}")


class DataConstruct:
    def __init__(self, outer):
        self.outer = outer
        self.data_definition_file = None
        self.throw_string = ""  # needed if you want to catch errors in conversion methods

    class DataValues:
        def __init__(self, name, default_val, data_type="String", notes=""):
            self.name = name
            self.default_val = default_val
            self.data_type = data_type
            self.notes = notes

    def act_on_data(self, words):
        if len(words) < 2:
            self.outer.error("Need to specify data class name")
            return

        class_name = words[1]
        provided_other_class_name = len(words) > 2
        internal_class_name = words[2] if provided_other_class_name else f"{class_name}Internal"

        follow = self.outer.look_for_follow()
        follow_type = follow.get_first()
        table = follow.get_second()

        if follow_type != "TABLE":
            self.outer.error(f"Error table does not follow data {words[0]} {words[1]}")
            return

        if class_name in self.outer.data_names:
            class_name += str(self.outer.step_count)
            self.outer.warning(f"Data name is duplicated, has been renamed {class_name}")

        self.outer.trace(f"Creating class for {class_name}")
        self.outer.data_names[class_name] = ""

        self.start_data_file(class_name, False)
        self.data_print_ln(f"package {self.outer.package_path}")
        for line in self.outer.lines_to_add_for_data_and_glue:
            self.data_print_ln(line)
        self.data_print_ln(f"class {class_name}:")

        variables = []
        do_internal = self.create_variable_list(table, variables)
        for variable in variables:
            self.outer.class_data_names.add(f"{class_name}#{variable.name}")
            self.data_print_ln(
                f"    {variable.data_type} {self.outer.make_name(variable.name)} = \"{variable.default_val}\"")

        self.create_constructor(variables, class_name)
        self.create_equals_method(variables, class_name)
        self.create_builder_method(variables, class_name)
        self.create_to_string_method(variables, class_name)
        self.create_to_json_method(variables)
        self.create_from_json_method(variables, class_name)
        self.create_table_to_json_method(class_name)
        self.create_json_to_table_method(class_name)

        if do_internal:
            self.outer.data_names_internal[internal_class_name] = ""
            self.create_conversion_method(internal_class_name, variables)

        self.data_print_ln("    }")
        self.end_data_file()

        if do_internal:
            self.create_internal_class(internal_class_name, class_name, variables, provided_other_class_name)

    def create_json_to_table_method(self, class_name):
        code = f"""
            @staticmethod
            def list_from_json(json: str) -> List[{class_name}]:
                list = []
                json = json.replace("\\s", "")
                json = json.replace("[", "").replace("]", "")
                json_objects = re.split(r'(?<=}}),\\s*(?={{)', json)
                for json_object in json_objects:
                    list.append({class_name}.from_json(json_object))
                return list
        """
        self.data_print_ln(code)


class Translate:
    class DataConstruct:
        def __init__(self, outer):
            self.outer = outer
            self.data_definition_file = None
            self.throw_string = ""  # needed if you want to catch errors in conversion methods
            self.one_data_file_started = False

        class DataValues:
            def __init__(self, name, default_val, data_type="String", notes=""):
                self.name = name
                self.default_val = default_val
                self.data_type = data_type
                self.notes = notes

        import re
        from typing import List

        def create_json_to_table_method(self, class_name):
            code = f"""
            @staticmethod
            def list_from_json(json: str) -> List[{class_name}]:
                result_list = []
                json = json.replace("\\s", "")
                json = json.replace("[", "").replace("]", "")
                json_objects = re.split(r"(?<=}}),\\s*(?={{)", json)
                for json_object in json_objects:
                    result_list.append({class_name}.from_json(json_object))
                return result_list
            """
            self.data_print_ln(code)

        def create_table_to_json_method(self, class_name):
            code = f"""
            @staticmethod
            def list_to_json(list: List[{class_name}]) -> str:
                json_builder = []
                json_builder.append("[")
                for i in range(len(list)):
                    json_builder.append(list[i].to_json())
                    if i < len(list) - 1:
                        json_builder.append(",")
                json_builder.append("]")
                return "".join(json_builder)
            """
            self.data_print_ln(code)

        def end_data_file(self):
            if Configuration.one_data_file:
                return
            try:
                self.data_definition_file.close()
            except IOError:
                raise RuntimeError("Error in closing data definition file")

        def end_one_data_file(self):
            if not Configuration.one_data_file or not self.one_data_file_started:
                return
            try:
                self.data_definition_file.close()
                self.one_data_file_started = False
            except IOError:
                raise RuntimeError("Error in closing one data file")

        def start_data_file(self, class_name, create_tmpl):
            if Configuration.one_data_file:
                self.start_one_data_file()
                return
            extension = Configuration.data_definition_file_extension
            if create_tmpl:
                extension = "tmpl"
            data_definition_pathname = f"{Configuration.test_sub_directory}{self.outer.feature_directory}{self.outer.feature_name}/{class_name}.{extension}"
            try:
                self.data_definition_file = open(data_definition_pathname, 'w')
            except IOError:
                self.outer.error("IO Exception in setting up the files")
                self.outer.error(f"Writing {data_definition_pathname}")

        def start_one_data_file(self):
            if self.one_data_file_started:
                return
            self.one_data_file_started = True
            extension = Configuration.data_definition_file_extension
            data_definition_pathname = f"{Configuration.test_sub_directory}{self.outer.feature_directory}{self.outer.feature_name}/{self.outer.feature_name}_data.{extension}"
            try:
                self.data_definition_file = open(data_definition_pathname, 'w')
            except IOError:
                self.outer.error("IO Exception in setting up the files")
                self.outer.error(f"Writing {data_definition_pathname}")

        def data_print_ln(self, line):
            try:
                self.data_definition_file.write(line + "\n")
            except IOError:
                self.outer.error("IO ERROR")

        def create_constructor(self, variables, class_name):
            self.data_print_ln(f"    def __init__(self) -> None:")
            self.data_print_ln("        pass")
            self.data_print_ln(f"    def __init__(self,")
            comma = ""
            for variable in variables:
                self.data_print_ln(f"        {comma} {self.outer.make_name(variable.name)}: str")
                comma = ","
            self.data_print_ln("        ) -> None:")
            for variable in variables:
                self.data_print_ln(
                    f"        self.{self.outer.make_name(variable.name)} = {self.outer.make_name(variable.name)}")

        def create_internal_constructor(self, variables, class_name):
            self.data_print_ln(f"    def __init__(self,")
            comma = ""
            for variable in variables:
                self.data_print_ln(f"        {comma} {self.outer.make_name(variable.name)}: {variable.data_type}")
                comma = ","
            self.data_print_ln("        ) -> None:")
            for variable in variables:
                self.data_print_ln(f"        self.{self.outer.make_name(variable.name)} = {variable.name}")

        def create_to_string_method(self, variables, class_name):
            code = f"""
            def __str__(self) -> str:
                return "{class_name} {{" + \\
            """
            for variable in variables:
                code += f'                " {variable.name} = " + str(self.{variable.name}) + " " + \\\n'
            code += '                "} "'
            if Configuration.add_line_to_string:
                code += ' + "\\n"'
            code += ' }'
            self.data_print_ln(code)

        def create_from_json_method(self, variables, class_name):
            first_part = f"""
            @staticmethod
            def from_json(json: str) -> {class_name}:
                instance = {class_name}()
                json = json.replace("\\s", "")
                key_value_pairs = json.replace("{", "").replace("}", "").split(",")
                for pair in key_value_pairs:
                    entry = pair.split(":")
                    key = entry[0].replace('\\"', "").strip()
                    value = entry[1].replace('\\"', "").strip()
                    switch = {{
            """
            middle_part = ""
            for variable in variables:
                middle_part += f'                    "{variable.name}": lambda: setattr(instance, "{variable.name}", value),\n'
            last_part = f"""
                    }}
                    switch.get(key, lambda: print(f"Invalid JSON element {{key}}", file=sys.stderr))()
                return instance
            """
            self.data_print_ln(first_part + middle_part + last_part)

        def create_to_json_method(self, variables):
            code = """
            def to_json(self) -> str:
                return " {" + 
            """
            comma = ""
            ##   This needs some work
      #      for variable in variables:
       #         code += f'                {comma} "{variable.name}": \\" + str(self.{variable.name}) + \\"' +
       #                 comma = '         + ","'
            code += '                "} "'
            self.data_print_ln(code)

        def data_print_ln(self, line):
            try:
                self.data_definition_file.write(line + "\n")
            except IOError:
                self.outer.error("IO ERROR")

        def create_builder_method(self, variables, class_name):
            self.data_print_ln("    class Builder:")
            for variable in variables:
                self.data_print_ln(f"        def __init__(self) -> None:")
                self.data_print_ln(f"            self.{variable.name} = {self.outer.quote_it(variable.default_val)}")
            for variable in variables:
                self.data_print_ln(
                    f"        def {self.outer.make_build_name(variable.name)}(self, {variable.name}: str) -> 'Builder':")
                self.data_print_ln(f"            self.{variable.name} = {variable.name}")
                self.data_print_ln("            return self")
            self.data_print_ln("        def set_compare(self) -> 'Builder':")
            for variable in variables:
                self.data_print_ln(
                    f"            self.{variable.name} = {self.outer.quote_it(Configuration.do_not_compare)}")
            self.data_print_ln("            return self")
            self.data_print_ln(f"        def build(self) -> {class_name}:")
            self.data_print_ln(f"            return {class_name}(")
            comma = ""
            for variable in variables:
                self.data_print_ln(f"                {comma}{variable.name}")
                comma = ","
            self.data_print_ln("            )")

        def create_equals_method(self, variables, class_name):
            self.data_print_ln("    def __eq__(self, other) -> bool:")
            self.data_print_ln("        if self is other:")
            self.data_print_ln("            return True")
            self.data_print_ln("        if other is None or not isinstance(other, self.__class__):")
            self.data_print_ln("            return False")
            self.data_print_ln(f"        {variable_name} = other")
            self.data_print_ln("        result = True")
            for variable in variables:
                self.data_print_ln(
                    f"        if self.{variable.name} != {self.outer.quote_it(Configuration.do_not_compare)} and {variable_name}.{variable.name} != {self.outer.quote_it(Configuration.do_not_compare)}:")
                self.data_print_ln(f"            if self.{variable.name} != {variable_name}.{variable.name}:")
                self.data_print_ln("                result = False")
            self.data_print_ln("        return result")

        def create_conversion_method(self, internal_class_name, variables):
            self.data_print_ln(f"    def to_{internal_class_name}(self) -> {internal_class_name}:")
            self.data_print_ln(f"        return {internal_class_name}(")
            comma = ""
            for variable in variables:
                initializer = self.outer.make_value_from_string(variable, True)
                self.data_print_ln(f"            {comma}{initializer}")
                comma = ","
            self.data_print_ln("        )")

        def create_variable_list(self, table, variables):
            header_line = True
            do_internal = False
            for line in table:
                if header_line:
                    headers = self.outer.parse_line(line)
                    self.check_headers(headers)
                    header_line = False
                    if len(headers) > 2:
                        do_internal = True
                    continue
                elements = self.outer.parse_line(line)
                if len(elements) < 2:
                    self.outer.error(f"Data line has less than 2 entries {line}")
                    continue
                if len(elements) > 3:
                    variables.append(self.DataValues(self.outer.make_name(elements[0]), elements[1],
                                                     self.alter_data_type(elements[2]), elements[3]))
                elif len(elements) > 2:
                    variables.append(self.DataValues(self.outer.make_name(elements[0]), elements[1],
                                                     self.alter_data_type(elements[2])))
                else:
                    variables.append(self.DataValues(self.outer.make_name(elements[0]), elements[1]))
            return do_internal

        def alter_data_type(self, s):
            # Will need to be altered to language specific types
            return {
                "Int": "int",
                "Char": "str",
                "Decimal": "float",
                "string": "str"
            }.get(s, s)

        def check_headers(self, headers):
            expected = ["Name", "Default", "Datatype", "Notes"]
            if headers[:2] != expected[:2]:
                self.outer.error(f"Headers should start with {expected}")

        def create_internal_class(self, class_name, other_class_name, variables, provided_class_name):
            class_name_internal = class_name
            if class_name_internal in self.outer.data_names:
                class_name_internal += str(self.outer.step_count)
                self.outer.warning(f"Data name is duplicated, has been renamed {class_name_internal}")
            self.outer.trace(f"Creating internal class for {class_name_internal}")
            self.outer.data_names[class_name_internal] = ""
            self.start_data_file(class_name, provided_class_name)
            self.data_print_ln(f"package {self.outer.package_path}")
            for line in self.outer.lines_to_add_for_data_and_glue:
                self.data_print_ln(line)
            self.data_print_ln(f"class {class_name}:")
            for variable in variables:
                self.data_print_ln(f"    {variable.data_type} {self.outer.make_name(variable.name)}")
            self.data_print_ln("")
            self.create_data_type_to_string_object(class_name, variables)
            self.create_to_string_object(other_class_name, variables)
            self.create_internal_constructor(variables, class_name)
            self.create_internal_equals_method(variables, class_name)
            self.create_to_string_method(variables, class_name)
            self.data_print_ln("    }")  # end class
            self.end_data_file()

        def create_internal_equals_method(self, variables, class_name):
            self.data_print_ln("    def __eq__(self, other) -> bool:")
            self.data_print_ln("        if self is other:")
            self.data_print_ln("            return True")
            self.data_print_ln("        if other is None or not isinstance(other, self.__class__):")
            self.data_print_ln("            return False")
            variable_name = f"_{class_name}"
            self.data_print_ln(f"        {variable_name} = other")
            self.data_print_ln("        return ")
            and_str = ""
            for variable in variables:
                comparison = " == " if self.primitive_data_type(variable) else ".equals"
                self.data_print_ln(
                    f"                {and_str}( {variable_name}.{variable.name} {comparison} self.{variable.name})")
                and_str = " and "

        def primitive_data_type(self, variable):
            return variable.data_type in ["boolean", "char", "int", "float", "double", "long", "byte", "short"]

        def create_data_type_to_string_object(self, class_name, variables):
            self.data_print_ln("    @staticmethod")
            self.data_print_ln("    def to_data_type_string() -> str:")
            self.data_print_ln(f"        return {self.outer.quote_it(class_name + ' {')}")
            add_str = "+"
            space = " "
            for variable in variables:
                self.data_print_ln(f"        {add_str} {self.outer.quote_it(variable.data_type + space)} ")
            self.data_print_ln(f"            + {self.outer.quote_it('} ')}")

        def create_to_string_object(self, other_class_name, variables):
            self.data_print_ln(f"    def to_{other_class_name}(self) -> {other_class_name}:")
            self.data_print_ln(f"        return {other_class_name}(")
            comma = ""
            for variable in variables:
                method = self.make_value_to_string(variable, True)
                self.data_print_ln(f"        {comma} {method}")
                comma = ","
            self.data_print_ln("        )")

        def make_value_to_string(self, variable, make_name_value):
            value = self.outer.make_name(variable.name) if make_name_value else self.outer.quote_it(
                variable.default_val)
            if variable.data_type in ["String", "int", "double", "byte", "short", "long", "float", "boolean", "char",
                                      "Byte", "Short", "Integer", "Long", "Float", "Double", "Boolean", "Character"]:
                return f"str({value})"
            return f"{value}.to_string()"

    class ImportConstruct:
        class ImportData:
            def __init__(self, data_type, conversion_method, import_name="", notes=""):
                self.data_type = data_type
                self.import_name = import_name
                self.conversion_method = conversion_method
                self.notes = notes

        def act_on_import(self, words):
            follow = self.outer.look_for_follow()
            follow_type = follow.get_first()
            table = follow.get_second()
            if follow_type != "TABLE":
                self.outer.error(f"Error table does not follow import {words[0]} {words[1]}")
                return
            imports = []
            self.create_import_list(table, imports)
            for im in imports:
                if im.data_type in self.outer.import_names:
                    self.outer.error(f"Data type is duplicated, has been renamed {im.data_type}")
                    continue
                if im.conversion_method:
                    self.outer.import_names[im.data_type] = im.conversion_method
                else:
                    method_name = f"{im.data_type}($)"
                    self.outer.import_names[im.data_type] = method_name

            for im in imports:
                if im.import_name:
                    value = f"import {im.import_name}"
                    self.outer.lines_to_add_for_data_and_glue.append(value)

        def create_import_list(self, table, variables):
            header_line = True
            for line in table:
                if header_line:
                    headers = self.outer.parse_line(line)
                    self.check_headers(headers)
                    header_line = False
                    continue
                elements = self.outer.parse_line(line)
                if len(elements) < 2:
                    self.outer.error(f"Data line has less than 2 entries {line}")
                    continue
                if len(elements) > 3:
                    variables.append(self.ImportData(elements[0], elements[1], elements[2], elements[3]))
                elif len(elements) > 2:
                    variables.append(self.ImportData(elements[0], elements[1], elements[2]))
                else:
                    variables.append(self.ImportData(elements[0], elements[1]))

        def check_headers(self, headers):
            expected = ["Datatype", "ConversionMethod", "Import", "Notes"]
            if headers[:2] != expected[:2]:
                self.outer.error(f"Headers should start with {expected}")

    class DefineConstruct:
        class DefineData:
            def __init__(self, name, value):
                self.name = name
                self.value = value

            def __str__(self):
                return f" name = {self.name} value = {self.value}"

        def act_on_define(self, words):
            follow = self.outer.look_for_follow()
            follow_type = follow.get_first()
            table = follow.get_second()
            if follow_type != "TABLE":
                self.outer.error(f"Error table does not follow define {words[0]} {words[1]}")
                return
            defines = []
            self.create_define_list(table, defines)
            for im in defines:
                if im.name in self.outer.define_names:
                    self.outer.warning(f"Define is duplicated will be skipped {im.name} = {im.value}")
                    continue
                if not im.value:
                    self.outer.warning("Empty value for define")
                self.outer.define_names[im.name] = im.value

        def create_define_list(self, table, variables):
            header_line = True
            for line in table:
                if header_line:
                    headers = self.outer.parse_line(line)
                    self.check_headers(headers)
                    header_line = False
                    continue
                elements = self.outer.parse_line(line)
                if len(elements) < 2:
                    self.outer.error(f"Data line has less than 2 entries {line}")
                else:
                    variables.append(self.DefineData(elements[0], elements[1]))

        def check_headers(self, headers):
            expected = ["Name", "Value", "Notes"]
            if headers[:2] != expected[:2]:
                self.outer.error(f"Headers should start with {expected}")

    class Configuration:
        log_it = False
        in_test = False
        trace_on = False
        space_characters = '~'
        add_line_to_string = True
        do_not_compare = "?DNC?"
        current_directory = ""
        feature_sub_directory = "src/test/java/"
        tree_directory = "features/"
        starting_feature_directory = feature_sub_directory + tree_directory
        search_tree = False
        package_name = "gherkinexecutor"
        test_sub_directory = f"src/test/java/{package_name}/"
        data_definition_file_extension = "java"
        test_framework = "JUnit5"
        add_to_package_name = ""
        lines_to_add_for_data_and_glue = ["import java.util.*;"]
        feature_files = []
        tag_filter = ""
        filter_expression = ""
        one_data_file = False

    class TagFilterEvaluator:
        @staticmethod
        def should_not_execute(words, filter_expression):
            scenario_tags = set(words)
            return not TagFilterEvaluator.should_execute(scenario_tags, filter_expression)

        @staticmethod
        def should_execute(scenario_tags, filter_expression):
            if filter_expression.strip() == "":
                return True

            required_conditions = []
            excluded_tags = set()

            TagFilterEvaluator.parse_expression(filter_expression, required_conditions, excluded_tags)

            has_excluded_tag = any(tag in excluded_tags for tag in scenario_tags)
            matches_required = not required_conditions or any(
                scenario_tags.issuperset(tags) for tags in required_conditions)

            return matches_required and not has_excluded_tag

        @staticmethod
        def parse_expression(expression, required_conditions, excluded_tags):
            groups = expression.split(" OR ")
            for group in groups:
                tags = set()
                elements = group.strip().split(" AND ")
                for element in elements:
                    element = element.strip()
                    if element.startswith("NOT "):
                        excluded_tags.add(element.replace("NOT ", ""))
                    else:
                        tags.add(element)
                if tags:
                    required_conditions.append(tags)


class Pair:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def get_first(self):
        return self.key

    def get_second(self):
        return self.value

    def __str__(self):
        return f"Pair{{key={self.key}, value={self.value}}}"




 if __name__ == "__main__":



