import os
import re
import sys
import traceback


class Translate:
    def __init__(self):
        self.data_in = None
        self.step_count = 0
        self.step_number_in_scenario = 0
        self.scenarios = {}  # used to check if duplicate scenario names
        self.data_names = {}  # used to check for duplicate data
        self.data_names_internal = {}  # used to check for duplicate data
        self.import_names = {}  # used to hold conversion functions for imports

        self.lines_to_add_for_data_and_glue = []
        self.lines_to_add_to_end_of_glue = []
        self.define_names = {}
        self.setp_count = 0  # use to label duplicate scenarios
        self.glue_class = ""  # glue class name
        self.glue_object = ""  # glue object name

        self.first_scenario = True
        self.add_background = False  # Have seen Background
        self.add_cleanup = False  # have seen Cleanup

        self.in_cleanup = False  # Current scenario is Cleanup
        self.final_cleanup = False  # for the last part of scenario
        self.test_file = None

        self.feature_acted_on = False  # Have found a feature step
        self.feature_name = ""

        self.directory_name = ""
        self.feature_directory = ""  # if feature file is in a directory
        self.feature_package_path = ""
        self.package_path = "Not Set"

        self.class_data_names = []

        self.data_construct = DataConstruct(self)
        self.template_construct = TemplateConstruct(self)
        self.step_construct = StepConstruct(self)
        self.import_construct = ImportConstruct(self)
        self.define_construct = DefineConstruct(self)

        self.filter_expression = Configuration.filter_expression
        self.skip_steps = False

        self.scenario_count = 0  # Number of scenarios encountered
        self.background_count = 0  # Number of backgrounds encountered
        self.cleanup_count = 0  # Number of cleanups encountered

        self.TAG_INDICATOR = "@"
        self.tag_line = ""  # Contains last tag line
        self.tag_line_number = 0  # Line number for last tag line

        self.error_occurred = False

    @staticmethod
    def main(args):
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

        self.lines_to_add_for_data_and_glue.extend(Configuration.lines_to_add_for_data_and_glue)
        self.data_in = InputIterator(name, self.feature_directory, self)
        self.alter_feature_directory()
        if self.data_in.is_empty():
            return

        for pass_num in range(0, 4):
            self.data_in.reset()
            eof = False
            while not eof:
                line = self.data_in.next()
                if line == InputIterator.EOF:
                    eof = True
                    continue
                self.act_on_line(line, pass_num)
        self.end_up()

    def alter_feature_directory(self):
        search_for = Configuration.tree_directory
        alternate_search_for = search_for.replace("/", "\\")
        directory = self.feature_directory.replace(search_for, "")
        directory = directory.replace(alternate_search_for, "")
        self.feature_directory = directory
        self.featurre_package_path = self.feature_directory.replace("\\", ".").replace("/", ".")

    def find_feature_directory(self, name):
        directory = ""
        index_forward = name.rfind('/')
        index_back = name.rfind('\\')
        index = max(index_forward, index_back)
        if index >= 0:
            directory = name[:index + 1]
        self.feature_directory = directory
        self.featurre_package_path = self.feature_directory.replace("\\", ".").replace("/", ".")

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
            self.tag_line = line
            self.tag_line_number = self.data_in.get_line_number()
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
            if TagFilterEvaluator.should_not_execute(comment, self.filter_expression):
                self.data_in.go_to_end()
                print(" Skip Entire Feature ")
        elif keyword == "Feature" and pass_num == 0:
            self.act_on_feature_first_half(full_name)
            if TagFilterEvaluator.should_not_execute(comment, self.filter_expression):
                self.data_in.go_to_end()
                print(" Skip Entire Feature ")
        elif keyword == "Scenario" and pass_num == 3:
            if TagFilterEvaluator.should_not_execute(comment, self.filter_expression):
                self.skip_steps = True
            else:
                self.skip_steps = False
                self.act_on_scenario(full_name)
                self.in_cleanup = False
        elif keyword == "Background":
            self.add_background = True
            if pass_num == 3:
                self.skip_steps = False
                self.act_on_background(full_name)
                self.in_cleanup = True
        elif keyword == "Cleanup":
            self.add_cleanup = True
            if pass_num == 3:
                self.skip_steps = False
                self.act_on_cleanup(full_name)
                self.in_cleanup = True
        elif keyword in ["But", "Given", "When", "Then", "And", "Star", "Arrange", "Act", "Assert", "Rule",
                         "Calculation"]:
            if pass_num == 3 and not self.skip_steps:
                self.step_construct.act_on_step(full_name, comment)
        elif keyword == "Data" and pass_num == 1:
            self.skip_steps = False
            self.data_construct.act_on_data(words)
            self.step_count += 1
        elif keyword == "Import" and pass_num == 0:
            self.skip_steps = False
            self.import_construct.act_on_import(words)
        elif keyword == "Define" and pass_num == 0:
            self.skip_steps = False
            self.define_construct.act_on_define(words)

    def check_for_tag_line(self):
        if not self.tag_line:
            return

        if self.tag_line_number + 1 == self.data_in.get_line_number():
            self.test_print("")
            if Configuration.test_framework == "unittest":
                self.test_print("    " + self.tag_line)
            else:
                self.test_print(self.tag_line)
        self.tag_line = ""
        self.tag_line_number = 0

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
        # if self.act_on_feature_first_half(full_name):
        #     return

        test_framework = Configuration.test_framework
        if test_framework == "unittest":
            self.test_print("import unittest")
        elif test_framework == "pytest":
            self.test_print("import pytest")
        else:
            self.test_print("import pytest")
        self.test_print("from typing import List")
        self.test_print("import sys")
        self.make_init_py()
        self.test_print(self.make_import_for_data_directory())
        subdirectory = self.package_path.replace("/", ".").replace("\\", ".")
        # Configuration.test_sub_directory
        glue = "from " + subdirectory + "." + self.glue_class + " import " + self.glue_class
        self.test_print(glue)
        self.test_print("")
        self.test_print("")
        # if Configuration.log_it:
        # no imports needed
        self.check_for_tag_line()
        if test_framework == "unittest":
            self.test_print(f"class {full_name}(unittest.TestCase):")
        elif test_framework == "pytest":
            self.test_print(f"class {full_name}():")
        else:
            self.test_print(f"class {full_name}():")

        self.test_print(self.log_it())

        self.template_construct.begin_template()

    def act_on_feature_first_half(self, full_name):
        if self.feature_acted_on:
            self.warning(f"Feature keyword duplicated - it is ignored {full_name}")
            return True
        self.feature_acted_on = True
        self.feature_name = full_name
        self.package_path = f"{Configuration.add_to_package_name}{Configuration.package_name}.{self.feature_package_path}{self.feature_name}"
        self.print_flow(f"Package is {self.package_path}")
        feature_test_name = "test_" + full_name
        test_pathname = f"{Configuration.test_sub_directory}{self.feature_directory}{self.feature_name}/{feature_test_name}.py"
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

    def add_data_imports(self):
        ret = ""
        for name in self.data_names:
            imp_string = self.make_import_for_data_class(name)
            ret += imp_string + "\n"
        return ret

    def make_init_py(self):
        path = f"{Configuration.test_sub_directory}{self.feature_directory}{self.feature_name}/__init__.py"
        try:
            with open(path, 'w') as my_log:
                my_log.write(self.add_data_imports())
        except IOError as e:
            print(f"{e} Cause {e.__cause__}")
            print(f"**** Cannot write to __init__.py")

    def make_import_for_data_directory(self):
        path = self.package_path.replace("/", ".").replace("\\", ".")
        imp_string = "from " + path + " import *"
        return imp_string

    def make_import_for_data_class(self, name):
        path = self.package_path.replace("/", ".").replace("\\", ".")
        imp_string = "from " + path + "." + name + " import " + name
        return imp_string

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
        self.final_cleanup = self.add_background
        if self.first_scenario:
            self.first_scenario = False
        else:
            if self.add_background and not self.in_cleanup:
                self.test_print(f"        self.cleanup({self.glue_object}) # from previous")

        self.check_for_tag_line()
        self.test_print("")
        self.test_print(f"    def test_{full_name_to_use}(self):")
        self.test_print(f"        {self.glue_object} = {self.glue_class}()")

        if Configuration.log_it:
            self.test_print(f"        self.log(\"{full_name_to_use}\")")
        if self.add_background:
            self.test_print(f"        self.background({self.glue_object})")

    def act_on_background(self, full_name):
        self.background_count += 1
        full_name_to_use = "background"
        self.final_cleanup = False
        if self.background_count > 1:
            self.error("More than one Background statement")
            full_name_to_use += str(self.background_count)

        self.step_number_in_scenario = 0

        if self.first_scenario:
            self.first_scenario = False
        self.test_print("")
        self.test_print(f"    def {full_name_to_use}(self, {self.glue_object}):")
        if Configuration.log_it:
            self.test_print(f"        self.log(\"{full_name_to_use}\")")

    def act_on_cleanup(self, full_name):
        self.cleanup_count += 1
        self.final_cleanup = False
        full_name_to_use = "cleanup"
        if self.cleanup_count > 1:
            self.error("More than one cleanup statement")
            full_name_to_use += str(self.cleanup_count)

        self.step_number_in_scenario = 0

        if self.first_scenario:
            self.first_scenario = False
        self.test_print("")
        self.test_print(f"    def {full_name_to_use}(self, {self.glue_object}):")
        if Configuration.log_it:
            self.test_print(f"        self.log(\"{full_name_to_use}\")")

    def log_it(self):
        if Configuration.log_it:
            filename = os.path.join(self.directory_name, "log.txt")
            return f"""
    def log(self, value):
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
        exc_type, exc_value, exc_traceback = sys.exc_info()
        traceback.print_tb(exc_traceback)  # Prints just the traceback
        if self.data_in is None:
            print("Error is " + value)
        else:
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
            for name, replacement in self.define_names.items():
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
            print(f"Unable to read {e} {filepath}")
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
            print(f"Unable to read {e} {filepath}")
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
            print(f"Unable to read {filepath} + {e}")
            return
        lines = [line.strip() for line in raw]
        Configuration.feature_files.extend(lines)

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

    def from_import_data(self, data_type, value):
        if data_type in self.import_names:
            conversion_method = self.import_names[data_type].replace("$", value)
            return conversion_method
        return ""

    def make_value_from_string(self, variable, make_name_value, add_self=False):
        if make_name_value:
            value = Translate.make_name(variable.name)
        else:
            value = Translate.quote_it(variable.default_val)
        if add_self:
            value = "self." + value
        data_type = variable.data_type
        if data_type == "str":
            return value
        elif data_type == "int":
            return f"int({value})"
        elif data_type == "double":
            return f"float({value})"
        elif data_type == "float":
            return f"float({value})"
        elif data_type == "bool":
            return f"bool({value})"
        else:
            result = self.from_import_data(data_type, value)
            if result:
                return result
            return f"{data_type}({value})"  # Data type not found

    def end_up(self):
        if self.final_cleanup:
            self.test_print(f"        self.cleanup({self.glue_object}) # at the end")
        if self.scenario_count == 0:
            print("No scenarios")
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
                self.outer.error(f"Unable to read {filepath} {e}")
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
                    if len(line) > 1 and line[0] != '#':
                        self.lines_in.append(line.strip())
        except Exception as e:
            print(e)
        include_count -= 1

    def include_csv_file(self, included_file_name):
        try:
            raw = open(os.path.join(Configuration.feature_sub_directory, included_file_name)).readlines()
            for line in raw:
                line = line.strip()
                if len(line) > 1:
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
        follow_type, table = self.outer.look_for_follow()

        self.outer.test_print("")
        if follow_type == "TABLE":
            self.create_the_table(comment, table, full_name)
        elif follow_type == "NOTHING":
            self.no_parameter(full_name)
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
        self.outer.test_print(f"        string_list{s} = [")
        comma = ""
        for line in table:
            self.outer.test_print(f"            {comma}\"{line}\"")
            comma = ","
        self.outer.test_print("            ]")
        self.outer.test_print(f"        {self.outer.glue_object}.{full_name}(string_list{s})")
        self.outer.template_construct.make_function_template_is_list(data_type, full_name, "str")

    def string_to_string(self, table, full_name):
        s = str(self.step_number_in_scenario)
        self.outer.test_print(f"        string{s} =\"\"\"")
        for line in table:
            self.outer.test_print(f"{line}")
        self.outer.test_print("\"\"\".strip()")
        self.outer.test_print(f"        {self.outer.glue_object}.{full_name}(string{s})")
        self.outer.template_construct.make_function_template("str", full_name)

    def table_to_list_of_list_of_object(self, table, full_name, class_name):
        s = str(self.step_number_in_scenario)
        data_type = "List[List[str]]"
        data_type_initializer = "["

        self.outer.test_print(f"        string_list_list{s} :  {data_type}  = {data_type_initializer}")
        comma = ""
        for line in table:
            self.convert_bar_line_to_list(line, comma)
            comma = ","
        self.outer.test_print("            ]")
        self.outer.test_print(f"        {self.outer.glue_object}.{full_name}(string_list_list{s})")
        self.outer.template_construct.make_function_template_object(data_type, full_name, class_name)
        self.create_convert_table_to_list_of_list_of_object_method(class_name)

    def table_to_list_of_list(self, table, full_name):
        s = str(self.step_number_in_scenario)
        data_type = "List[List[str]]"
        data_type_initializer = "["

        self.outer.test_print(f"        string_list_list{s} = {data_type_initializer}")
        comma = ""

        for line in table:
            self.convert_bar_line_to_list(line, comma)
            comma = ","
        self.outer.test_print("            ]")
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
            self.table_to_string(table, full_name)
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
            self.table_to_list_of_object(table, full_name, class_name, transpose, compare)
        else:
            self.outer.error(f"Option not found, default to ListOfList {option}")
            self.table_to_list_of_list(table, full_name)

    def create_convert_table_to_list_of_list_of_object_method(self, to_class):
        variable = DataConstruct.DataValues("s", "s", to_class)
        convert = self.outer.make_value_from_string(variable, True)
        template = f"""
    def convert_list(self, string_list: List[List[str]]) -> List[List[{to_class}]]:
        class_list = []  # Initialize empty list
        for inner_list in string_list:
            inner_class_list = [{to_class}(s) for s in inner_list]  
        class_list.append(inner_class_list)  
        return class_list
        """
        self.outer.lines_to_add_to_end_of_glue.append(template)

    def table_to_string(self, table, full_name):
        s = str(self.step_number_in_scenario)
        self.outer.test_print(f"        table{s} = \"\"\"")
        for line in table:
            self.outer.test_print(f"{line}")
        self.outer.test_print("\"\"\".strip()")
        self.outer.test_print(f"        {self.outer.glue_object}.{full_name}(table{s})")
        self.outer.template_construct.make_function_template("str", full_name)

    def convert_bar_line_to_list(self, line_in, comma_in):
        line = line_in.split("#")[0].strip()
        self.outer.test_print(f"            {comma_in}[")
        elements = self.outer.parse_line(line)
        comma = ""
        for element in elements:
            self.outer.test_print(f"            {comma}\"{element}\"")
            comma = ","
        self.outer.test_print("            ]")

    def table_to_list_of_object(self, table, full_name, class_name, transpose, compare):
        self.outer.trace(f"TableToListOfObject class_names {class_name}")
        s = str(self.step_number_in_scenario)
        data_type = f"List[{class_name}]"
        data_type_initializer = "["
        self.outer.test_print(f"        object_list{s} : {data_type} = {data_type_initializer}")
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
        self.outer.test_print("            ]")
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
        self.outer.test_print(f"            {comma}{class_name}.Builder()")
        if compare:
            self.outer.test_print("             .set_compare()")
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
        self.package_path = ""
        self.final_cleanup = False
        self.glue_template_file = ""
        self.glue_functions = {}  # used to make sure only one glue implementation

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
        self.template_print(f"        its = self.convert_list(values)")
        self.template_print("        print(its)")
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
        self.template_print("            print(value)")
        self.template_print("             # Add calls to production code and asserts")
        if data_type != "List[List[str]]" and list_element != "str" and name in self.outer.data_names_internal:
            self.template_print(f"            i = value.to_{name}()")
        if not Configuration.in_test:
            self.template_print("        raise NotImplementedError(\"Must implement\")")
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

    def begin_template(self):

        for line in self.outer.lines_to_add_for_data_and_glue:
            self.template_print(line)
        # if Configuration.test_framework == "unittest":
        #     self.template_print("import unittest")
        # elif Configuration.test_framework == "pytest":
        #     self.template_print("import pytest")
        # else:
        #     self.template_print("pytest")

        # if Configuration.log_it:
        # nothing needed
        self.template_print(self.outer.make_import_for_data_directory())
        self.template_print("from typing import List")
        self.template_print("import sys")
        self.template_print("")
        self.template_print(f"class {self.outer.glue_class} :")
        self.template_print(f'    DNCString = "{Configuration.do_not_compare}"')
        self.template_print(self.outer.log_it())
        self.template_print("")

    def end_template(self):
        for line in self.outer.lines_to_add_to_end_of_glue:
            self.template_print(line)
        try:
            # self.outer.test_file.close()
            self.glue_template_file.close()
        except IOError as e:
            print(f"Error in closing: {e}")


class DataConstruct:
    def __init__(self, outer):
        self.outer = outer
        self.data_definition_file = None
        self.throw_string = ""  # needed if you want to catch errors in conversion methods
        self.one_data_file_started = False

    class DataValues:
        def __init__(self, name, default_val, data_type="str", notes=""):
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

        follow_type, table = self.outer.look_for_follow()
        #   follow_type = follow.get_first()
        #   table = follow.get_second()

        if follow_type != "TABLE":
            self.outer.error(f"Error table does not follow data {words[0]} {words[1]}")
            return

        if class_name in self.outer.data_names:
            self.outer.error(f"Data name is duplicated {class_name}")
            return;

        self.outer.trace(f"Creating class for {class_name}")
        self.outer.data_names[class_name] = class_name

        self.start_data_file(class_name, False)
        self.data_print_ln("import sys")
        self.data_print_ln("import re")
        self.data_print_ln("from typing import List")
        for line in self.outer.lines_to_add_for_data_and_glue:
            self.data_print_ln(line)
        self.data_print_ln("")
        self.data_print_ln("")
        self.data_print_ln(f"class {class_name}:")

        variables = []
        do_internal = self.create_variable_list(table, variables)
        for variable in variables:
            self.outer.class_data_names.append(f"{class_name}#{variable.name}")
            # self.data_print_ln(
            #     f"     {self.outer.make_name(variable.name)} : {variable.data_type} = \"{variable.default_val}\"")

        self.create_constructor(variables, class_name)
        self.create_equals_method(variables, class_name)
        self.data_print_ln("")
        self.create_to_string_method(variables, class_name)
        self.data_print_ln("")
        self.create_to_json_method(variables)
        self.create_from_json_method(variables, class_name)
        self.create_table_to_json_method(class_name)
        self.create_json_to_table_method(class_name)

        if do_internal:
            self.outer.data_names_internal[internal_class_name] = internal_class_name
            self.data_print_ln("")
            self.create_conversion_method(internal_class_name, variables)
        self.create_builder_method(variables, class_name)
        self.end_data_file()

        if do_internal:
            self.create_internal_class(internal_class_name, class_name, variables, provided_other_class_name)

    def create_json_to_table_method(self, class_name):
        code = f"""
    @staticmethod
    def list_from_json(json: str) -> List[\"{class_name}\"]:
        result_list = []
        json = re.sub(r"\\s+", "", json) 
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
    def list_to_json(list: List[\"{class_name}\"]) -> str:
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

    def data_print(self, line):
        try:
            self.data_definition_file.write(line)
        except IOError:
            self.outer.error("IO ERROR")

    def create_constructor(self, variables, class_name):
        self.data_print_ln(f"    def __init__(self,")
        comma = ""
        for variable in variables:
            self.data_print_ln(
                f"                {comma} {self.outer.make_name(variable.name)}: str = \"{variable.default_val}\"")
            comma = ","
        self.data_print_ln("                ) -> None:")
        for variable in variables:
            self.data_print_ln(
                f"        self.{self.outer.make_name(variable.name)} = {self.outer.make_name(variable.name)}")

    def create_internal_constructor(self, variables, class_name):
        self.data_print_ln(f"    def __init__(self,")
        comma = ""
        for variable in variables:
            self.data_print_ln(f"               {comma} {self.outer.make_name(variable.name)}: {variable.data_type}")
            comma = ","
        self.data_print_ln("                ) -> None:")
        for variable in variables:
            self.data_print_ln(f"        self.{self.outer.make_name(variable.name)} = {variable.name}")

    def create_to_string_method(self, variables, class_name):
        code = """
    def __str__(self) -> str:
        return "{CLASSNAME} {" + \\
        """
        code = code.replace("CLASSNAME", class_name)
        for variable in variables:
            code += f' " {variable.name} = " + str(self.{variable.name}) + " " '
        code += ' "} "'
        if Configuration.add_line_to_string:
            code += ' + "\\n"'
        self.data_print_ln(code)

    def create_from_json_method(self, variables, class_name):
        first_part = f"""
    @staticmethod
    def from_json(json: str):
        instance = {class_name}()
        json = re.sub(r"\\s+", "", json) 
        json = json.replace("{{","").replace("}}","") 
        key_value_pairs = json.split(",")
        for pair in key_value_pairs:
            entry = pair.split(":")
            key = entry[0].replace('\\"', "").strip()
            value = entry[1].replace('\\"', "").strip()
            switch = {{
   """

        middle_part = ""
        for variable in variables:
            middle_part += f'                "{variable.name}": lambda: setattr(instance, "{variable.name}", value),\n'
        last_part = f"""
                }}
            switch.get(key, lambda: print(f"Invalid JSON element {{key}}", file=sys.stderr))()
        return instance
        """
        self.data_print_ln(first_part + middle_part + last_part)

    def create_to_json_method(self, variables):
        code = "    def to_json(self) -> str:" + '\n'
        code += '        return "{" + \\' + '\n'

        comma = ""
        #   This needs some work
        for variable in variables:
            code += f'            {comma}\'"{variable.name}": "\'' + \
                    f' + str(self.{variable.name}) + \'"\' +  \\' + "\n"
            comma = '"," + '
        code += '            "}"'
        self.data_print_ln(code)

    def data_print_ln(self, line):
        try:
            self.data_definition_file.write(line + "\n")
        except IOError:
            self.outer.error("IO ERROR")

    def create_builder_method(self, variables, class_name):
        self.data_print_ln("")
        self.data_print_ln("    class Builder:")
        self.data_print_ln(f"        def __init__(self) -> None:")
        for variable in variables:
            self.data_print_ln(f"            self.{variable.name} = {self.outer.quote_it(variable.default_val)}")
        for variable in variables:
            self.data_print_ln("")
            self.data_print_ln(
                f"        def {self.outer.make_build_name(variable.name)}(self, {variable.name}: str) -> 'Builder':")
            self.data_print_ln(f"            self.{variable.name} = {variable.name}")
            self.data_print_ln("            return self")
        self.data_print_ln("")
        self.data_print_ln("        def set_compare(self) -> 'Builder':")
        for variable in variables:
            self.data_print_ln(
                f"            self.{variable.name} = {self.outer.quote_it(Configuration.do_not_compare)}")
        self.data_print_ln("            return self")
        self.data_print_ln("")
        self.data_print_ln(f"        def build(self):")
        self.data_print_ln(f"            return {class_name}(")
        comma = ""
        for variable in variables:
            self.data_print_ln(f"                {comma}self.{variable.name}")
            comma = ","
        self.data_print_ln("            )")

    def create_equals_method(self, variables, class_name):
        self.data_print_ln("")
        self.data_print_ln("    def __eq__(self, other) -> bool:")
        self.data_print_ln("        if self is other:")
        self.data_print_ln("            return True")
        self.data_print_ln("        if other is None or not isinstance(other, self.__class__):")
        self.data_print_ln("            return False")
        variable_name = "_" + class_name
        self.data_print_ln(f"        {variable_name} = other")
        self.data_print_ln("        result1 = True")

        for variable in variables:
            self.data_print_ln("        if not (self." + variable.name + " == " + Translate.quote_it( \
                Configuration.do_not_compare) + " or " + \
                               variable_name + "." + variable.name + " == " + Translate.quote_it( \
                Configuration.do_not_compare) + "):")
            self.data_print_ln(
                "            if not " + variable_name + "." + variable.name + " == self." + variable.name + ":")
            self.data_print_ln(
                "                result1 = False")
        self.data_print_ln("        return result1")

    def create_conversion_method(self, internal_class_name, variables):
        self.data_print_ln(f"    def to_{internal_class_name}(self): ")
        self.data_print_ln("        " + self.outer.make_import_for_data_class(internal_class_name))
        self.data_print_ln(f"        return {internal_class_name}(")
        comma = ""
        for variable in variables:
            initializer = self.outer.make_value_from_string(variable, True, True)
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
        # Will need to be altered to language specific types
        return {
            "Integer": "int",
            "Int": "int",
            "Character": "str",
            "Decimal": "float",
            "Double": "float",
            "string": "str",
            "String": "str",
            "Boolean": "bool",
            "char": "str",
            "Char": "str"
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

        for line in self.outer.lines_to_add_for_data_and_glue:
            self.data_print_ln(line)
        self.data_print_ln(f"class {class_name}:")
        self.data_print_ln("")
        self.create_data_type_to_string_object(class_name, variables)
        self.data_print_ln("")
        self.create_conversion_to_string_object(other_class_name, variables)
        self.data_print_ln("")
        self.create_internal_constructor(variables, class_name)
        self.data_print_ln("")
        self.create_internal_equals_method(variables, class_name)
        self.data_print_ln("")
        self.create_to_string_method(variables, class_name)
        self.end_data_file()

    def create_internal_equals_method(self, variables, class_name):
        self.data_print_ln("    def __eq__(self, other) -> bool:")
        self.data_print_ln("        if self is other:")
        self.data_print_ln("            return True")
        self.data_print_ln("        if other is None or not isinstance(other, self.__class__):")
        self.data_print_ln("            return False")
        variable_name = f"_{class_name}"
        self.data_print_ln(f"        {variable_name} = other")
        self.data_print("        return ")
        and_str = ""
        for variable in variables:
            comparison = "==" if self.primitive_data_type(variable) else "=="
            self.data_print(
                f" {and_str}( {variable_name}.{variable.name} {comparison} self.{variable.name})")
            and_str = " and "

    def primitive_data_type(self, variable):
        return variable.data_type in ["bool", "int", "float", "str", "complex"]

    def create_data_type_to_string_object(self, class_name, variables):
        self.data_print_ln("    @staticmethod")
        self.data_print_ln("    def to_data_type_string() -> str:")
        self.data_print_ln(f"        return {self.outer.quote_it(class_name + ' {')}")
        add_str = "+"
        space = " "
        for variable in variables:
            self.data_print_ln(f"        {add_str} {self.outer.quote_it(variable.data_type + space)} ")
        self.data_print_ln(f"        + {self.outer.quote_it('} ')}")

    def create_conversion_to_string_object(self, other_class_name, variables):
        self.data_print_ln(f"    def to_{other_class_name}(self) :")
        self.data_print_ln("        " + self.outer.make_import_for_data_class(other_class_name))
        self.data_print_ln(f"        return {other_class_name}(")
        comma = ""
        for variable in variables:
            method = self.make_value_to_string(variable, True, True)
            self.data_print_ln(f"        {comma} {method}")
            comma = ","
        self.data_print_ln("        )")

    def make_value_to_string(self, variable, make_name_value, add_self=False):
        value = self.outer.make_name(variable.name) if make_name_value else self.outer.quote_it(
            variable.default_val)
        if (add_self):
            value = "self." + value
        if variable.data_type in ["str", "int", "float", "bool", "complex"]:
            return f"str({value})"
        return f"str({value})"


class ImportConstruct:

    def __init__(self, outer):
        self.outer = outer

    class ImportData:
        def __init__(self, data_type, conversion_method, import_name="", notes=""):
            self.data_type = data_type
            self.import_name = import_name
            self.conversion_method = conversion_method
            self.notes = notes

    def act_on_import(self, words):
        follow_type, table = self.outer.look_for_follow()
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
                value = im.import_name
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

    def __init__(self, outer):
        self.outer = outer

    class DefineData:
        def __init__(self, name, value):
            self.name = name
            self.value = value

        def __str__(self):
            return f" name = {self.name} value = {self.value}"

    def act_on_define(self, words):
        follow_type, table = self.outer.look_for_follow()
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
    feature_sub_directory = "tests/"
    tree_directory = "features/"
    starting_feature_directory = feature_sub_directory + tree_directory
    search_tree = False
    package_name = "gherkinexecutor"
    test_sub_directory = f"tests/{package_name}/"
    data_definition_file_extension = "py"
    test_framework = "unittest"
    add_to_package_name = feature_sub_directory
    lines_to_add_for_data_and_glue = ["from tests.gherkinexecutor.ID import ID",
                                      "from tests.gherkinexecutor.TemperatureCalculations import TemperatureCalculations"]
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


if __name__ == '__main__':
    Translate.main(sys.argv[1:])
