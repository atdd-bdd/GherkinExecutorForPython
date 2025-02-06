import os


class Translate:
    def __init__(self):
        self.scenarios = {"": ""}  # used to check if duplicate scenario names
        self.glue_functions = {"": ""}  # used to make sure only one glue implementation
        self.data_names = {"": ""}  # used to check for duplicate data
        self.step_count = 0  # use to label duplicate scenarios
        self.base_path = Configuration.test_sub_directory
        self.glue_class = ""  # glue class name
        self.glue_object = ""  # glue object name
        self.step_number_in_scenario = 0  # use to label variables in scenario
        self.data_in = InputIterator("")
        self.first_scenario = True  # If first scenario
        self.background = False  # Have seen background
        self.cleanup = False  # Have seen cleanup

        # Create the output files, save names for deletions
        self.test_file_name = self.base_path + "Test" + ".tmp"
        self.test_file = open(self.test_file_name, 'w')

        self.glue_template_filename = self.base_path + "Glue" + ".tmp"
        self.glue_template_file  = open(self.glue_template_filename, 'w')
        self.data_definition_filename = self.base_path + "DataDefinition" + ".tmp"
        self.data_definition_file  = open(self.data_definition_filename, 'w')
        self.feature_acted_on = False  # Have found a feature step

    def translate_in_tests(self, name):
        self.data_in = InputIterator(name)
        eof = False
        while not eof:
            line = self.data_in.next()
            if line == InputIterator.EOF:
                eof = True
                continue
            self.act_on_line(line)
        self.end_up()

    def act_on_line(self, line):
        words, comment = self.split_line(line)
        if len(words) > 0:
            keyword = words[0].strip(':')
            if keyword == "*":
                keyword = "Star"
            words[0] = keyword
            self.act_on_keyword(keyword, words, comment)

    def split_line(self, line):
        allWords = line.split(" ")
        words = []
        comment = []
        inComment = False
        for aWord in allWords:
            word = aWord.strip()
            if not word:
                continue
            if word.endswith(":"):
                word = word.strip(':')
            if inComment:
                comment.append(word)
                continue
            if word[0] == '#':
                inComment = True
                word = word.strip('#')
                if word:
                    comment.append(word)
                continue
            words.append(word)
        return words, comment

    def act_on_keyword(self, keyword, words, comment):
        full_name = "_".join(words)
        self.trace("Act on keyword " + keyword + " " + full_name)
        if keyword == "Feature":
            self.act_on_feature(full_name)
        elif keyword == "Scenario":
            self.act_on_scenario(full_name, True)
        elif keyword == "Background":
            self.act_on_scenario(full_name, False)
            self.background = True
        elif keyword == "Cleanup":
            self.act_on_scenario(full_name, False)
            self.cleanup = True
        elif keyword in ["Given", "When", "Then", "And", "Star", "Arrange", "Act", "Assert"]:
            self.act_on_step(full_name, comment)
        elif keyword == "Data":
            self.act_on_data(words)
        else:
            self.error("keyword not recognized " + keyword)

    def act_on_feature(self, full_name):
        if self.feature_acted_on:
            self.error("Feature keyword duplicated - it is ignored " + full_name)
            return
        feature_name = full_name
        self.feature_acted_on = True
        testPathname = Configuration.feature_sub_directory + feature_name + "\\" + feature_name + ".kt"
        print(" Writing " + testPathname)
        self.clean_files()
        os.makedirs(Configuration.feature_sub_directory + feature_name, exist_ok=True)
        self.test_file = open(testPathname, 'w')
        templateFilename = Configuration.feature_sub_directory + feature_name + "\\" + feature_name + "_glue.tmpl"
        self.glue_template_file = open(templateFilename, 'w')
        dataDefinitionPathname = Configuration.feature_sub_directory + feature_name + "\\" + feature_name + "_data." + Configuration.data_definition_file_extension
        self.trace(" Writing " + dataDefinitionPathname)
        self.data_definition_file = open(dataDefinitionPathname, 'w')

        self.glue_class = full_name + "_glue"
        self.glue_object = self.make_name(full_name) + "_glue_object"
        self.test_print("package " + Configuration.package_name + "." + feature_name)
        self.test_print("import org.junit.jupiter.api.Test")
        self.test_print("import org.junit.jupiter.api.TestInstance")
        self.test_print("@TestInstance(TestInstance.Lifecycle.PER_CLASS)")
        self.test_print("class " + full_name + "{")
        self.test_print("")

        self.template_print("package " + Configuration.package_name + "." + feature_name)
        self.template_print("import kotlin.test.fail")
        self.template_print("")
        self.template_print("class " + self.glue_class + " {")
        self.template_print("")
        self.data_definition_print("package " + Configuration.package_name + "." + feature_name)

    def make_name(self, input):
        if not input:
            return "NAME_IS_EMPTY"
        temp = input.replace(' ', '_')
        return temp[0].lower() + temp[1:]

    class DataValues:
        def __init__(self, name, default, dataType="String", notes=""):
            self.name = name
            self.default = default
            self.dataType = dataType
            self.notes = notes

    def act_on_data(self, words):
        internal_class_name = ""
        if len(words) < 2:
            self.error("Need to specify data class name")
        class_name = words[1]
        if len(words) > 2:
            internal_class_name = words[2]
        else:
            internal_class_name = class_name + "Internal"
        follow_type, table = self.look_for_follow()
        if follow_type != "TABLE":
            self.error("Error table does not follow data " + words[0] + " " + words[1])
            return
        if class_name in self.data_names:
            self.error("Data name is duplicated, has been renamed " + class_name)
            class_name += str(self.step_count)
        self.trace("Creating class for " + class_name)
        self.data_names[class_name] = ""
        self.data_definition_print("data class " + class_name + "(")
        variables = []
        do_internal = self.create_variable_list(table, variables)
        for variable in variables:
            self.data_definition_print(
                "    val " + self.make_name(variable.name) + ": String = \"" + variable.default + "\","
            )
        self.data_definition_print("    )")

        if do_internal:
            self.create_conversion_method(internal_class_name, variables)
            self.create_internal_class(internal_class_name, class_name, variables)

    def create_conversion_method(self, internal_class_name, variables):
        self.data_definition_print(" {")
        self.data_definition_print("    fun to" + internal_class_name + "() : " + internal_class_name + "{")
        self.data_definition_print("        return " + internal_class_name + "(")
        for variable in variables:
            self.data_definition_print("        " + self.make_name(variable.name) + ".to" + variable.dataType + "(),")
        self.data_definition_print("        ) }")  # end function
        self.data_definition_print("    }")  # end class

    def create_variable_list(self, table, variables):
        header_line = True
        do_internal = False
        for line in table:
            if header_line:
                headers = self.parse_line(line)
                self.check_headers(headers)
                header_line = False
                if len(headers) > 2:
                    do_internal = True
                continue
            elements = self.parse_line(line)
            if len(elements) < 2:
                self.error(" Data line has less than 2 entries " + line)
                continue
            if len(elements) > 3:
                variables.append(self.DataValues(elements[0], elements[1], elements[2], elements[3]))
            elif len(elements) > 2:
                variables.append(self.DataValues(elements[0], elements[1], elements[2]))
            else:
                variables.append(self.DataValues(elements[0], elements[1]))
        return do_internal

    def check_headers(self, headers):
        expected = ["Name", "Default", "Datatype", "Notes"]
        if not (headers[0] == expected[0] and headers[1] == expected[1]):
            self.error("Headers should start with " + str(expected))

    def create_internal_class(self, class_name, other_class_name, variables):
        class_name_internal = class_name
        if class_name_internal in self.data_names:
            self.error("Data name is duplicated, has been renamed " + class_name_internal)
            class_name_internal += str(self.step_count)
        self.trace("Creating internal class for " + class_name_internal)
        self.data_names[class_name_internal] = ""
        self.data_definition_print("data class " + class_name_internal + "(")
        for variable in variables:
            self.data_definition_print(
                "    val " + self.make_name(
                    variable.name) + ": " + variable.dataType + "= \"" + variable.default + "\".to" + variable.dataType + "(),"
            )
        self.data_definition_print("    ) {")
        self.data_definition_print("    fun to" + other_class_name + "() : " + other_class_name + "{")
        self.data_definition_print("        return " + other_class_name + "(")
        for variable in variables:
            self.data_definition_print("        " + self.make_name(variable.name) + ".toString(),")
        self.data_definition_print("        ) }")  # end function
        self.data_definition_print("    }")  # end class

    def act_on_scenario(self, full_name, add_background):
        full_name_to_use = full_name
        if full_name in self.scenarios:
            full_name_to_use += str(self.step_count)
            self.error("Scenario name duplicated renamed " + full_name_to_use)
        else:
            self.scenarios[full_name_to_use] = ""
        self.step_number_in_scenario = 0
        if self.first_scenario:
            self.first_scenario = False
        else:
            if self.cleanup and add_background:
                self.test_print("        test_Cleanup()")
            self.test_print("        }")  # end previous scenario
        self.test_print("    @Test")
        self.test_print("    fun test_" + full_name_to_use + "(){")
        self.test_print("        val " + self.glue_object + " = " + self.glue_class + "()")
        if self.background and add_background:
            self.test_print("        test_Background()")

    def table_to_list_of_object(self, table, full_name, class_name, transpose):
        self.trace("classNames " + class_name)
        s = str(self.step_number_in_scenario)
        data_type = "List<" + class_name + ">"
        data_type_initializer = "list_of<" + class_name + ">"
        self.test_print("        val objectList" + s + " = " + data_type_initializer + "(")
        in_header_line = True
        data_list = self.convert_to_list_list(table, transpose)
        headers = [""]
        for row in data_list:
            if in_header_line:
                headers = row
                in_header_line = False
                continue
            values = row
            self.convert_bar_line_to_parameter(headers, values, class_name)
        self.test_print("            )")
        self.test_print("        " + self.glue_object + "." + full_name + "(objectList" + s + ")")
        self.make_function_template(data_type, full_name)

    def convert_to_list_list(self, table, transpose):
        temporary = []
        for line in table:
            temporary.append(self.parse_line(line))
        result = temporary
        if transpose:
            result = self.transpose(temporary)
        return result

    def table_to_list_of_list(self, table, full_name):
        s = str(self.step_number_in_scenario)
        data_type = "List<List<String>>"
        data_type_initializer = "list_of<List<String>>"
        self.test_print("        val stringListList" + s + " = " + data_type_initializer + "(")
        for line in table:
            self.convert_bar_line_to_list(line)
        self.test_print("            )")
        self.test_print("        " + self.glue_object + "." + full_name + "(stringListList" + s + ")")
        self.make_function_template(data_type, full_name)

    def make_function_template(self, data_type, full_name):
        if full_name in self.glue_functions:
            current_data_type = self.glue_functions[full_name]
            if current_data_type != data_type:
                error(f"Function {full_name} datatype {current_data_type} not equals {data_type}")
            return  # already have a prototype

        self.glue_functions[full_name] = data_type
        if not data_type:
            self.template_print(f"    def {full_name}(self):")
        else:
            self.template_print(f"    def {full_name}(self, value: {data_type}):")
        self.template_print("        print('*******')")
        if data_type:
            self.template_print("        print(value)")
        self.template_print("        fail(\"Not yet implemented\"")
        self.template_print("")
    def convert_bar_line_to_list(self, line):
        self.test_print("           list_of<String>(")
        elements = self.parse_line(line)
        for element in elements:
            self.test_print("            \"" + element + "\",")
        self.test_print("            ),")

    def convert_bar_line_to_parameter(self, headers, values, class_name):
        self.trace("Headers " + str(headers))
        size = len(headers)
        if len(headers) > len(values):
            size = len(values)
            self.error("not sufficient values, using what is there" + str(values))
        self.test_print("            " + class_name + "(")
        for i in range(size):
            self.test_print(
                "                " + self.make_name(headers[i]) + " = \"" + values[i].replace(
                    Configuration.space_characters, ' '
                ) + "\","
            )
        self.test_print("                ),")

    def act_on_step(self, full_name, comment):
        self.step_number_in_scenario += 1
        follow_type, table = self.look_for_follow()
        self.test_print("")
        if follow_type == "TABLE":
            self.create_the_table(comment, table, full_name)
        elif follow_type == "NOTHING":
            self.no_parameter(full_name)
        elif follow_type == "STRING":
            self.create_the_string_code(comment, table, full_name)

    def create_the_string_code(self, comment, table, full_name):
        option = "String"
        if len(comment) > 0 and comment[0]:
            option = comment[0]
        if option == "ListOfString":
            self.string_to_list(table, full_name)
        else:
            self.string_to_string(table, full_name)

    def create_the_table(self, comment, table, full_name):
        option = "ListOfList"
        if len(comment) > 0 and comment[0]:
            option = comment[0]
        if option == "ListOfList":
            if len(comment) > 1 and comment[1]:
                object_name = comment[1]
                self.table_to_list_of_list_of_object(table, full_name, object_name)
            else:
                self.table_to_list_of_list(table, full_name)
        elif option in ["String", "string"]:
            self.table_to_string(table, full_name)
        elif option == "ListOfObject":
            if len(comment) < 2:
                self.error("No class name specified")
                return True
            class_name = comment[1]
            transpose = False
            if len(comment) > 2:
                action = comment[2]
                if action not in ["transpose", "Transpose"]:
                    self.error("Action not recognized " + action)
                else:
                    transpose = True
            self.table_to_list_of_object(table, full_name, class_name, transpose)
        else:
            self.error("Option not found, default to ListOfList " + option)
            self.table_to_list_of_list(table, full_name)
        return False

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
            self.trace("Table is " + str(ret_value))
            return "TABLE", ret_value
        if line == '"""':
            ret_value = self.read_string()
            self.trace("Multi Line String is " + str(ret_value))
            return "STRING", ret_value
        return "NOTHING", empty

    def convert_bar_line_to_list_of_object(self, line, object_name):
        self.test_print("           list_of<" + object_name + ">(")
        elements = self.parse_line(line)
        for element in elements:
            self.test_print("            " + object_name + "(\"" + element + "\"),")
        self.test_print("            ),")

    def parse_line(self, line):
        line_short = line.strip()
        if line_short[0] == '|':
            line_short = line_short[1:]
        else:
            self.error("table not begin with | " + line)
            return ["ERROR IN TABLE LINE " + line]
        last = len(line_short) - 1
        if last < 0:
            self.error("table format error " + line)
            return ["ERROR IN TABLE LINE " + line]
        if line_short[last] == '|':
            line_short = line_short[:last]
        else:
            self.error("table not end with | " + line)
        elements = line_short.split("|")
        elements_trimmed = [element.strip().replace(Configuration.space_characters, ' ') for element in elements]
        return elements_trimmed

    def read_table(self):
        ret_value = []
        line = self.data_in.peek().strip()
        while line and (line[0] == '|' or line[0] == '#'):
            line = self.data_in.next().strip()
            if line[0] == '|' and line.endswith('|'):
                ret_value.append(line)
            else:
                self.error("Invalid line in table " + line)
            line = self.data_in.peek().strip()
        return ret_value

    def read_string(self):
        ret_value = []
        first_line = self.data_in.peek()
        count_indent = self.count_indent(first_line)
        self.data_in.next()
        line = self.data_in.next()
        while line.strip() != '"""':
            ret_value.append(line[count_indent:])
            line = self.data_in.next()
        return ret_value

    def count_indent(self, first_line):
        line = first_line.lstrip()
        return len(first_line) - len(line)

    def clean_files(self):
        self.test_file.close()
        self.glue_template_file.close()
        self.data_definition_file.close()
        os.remove("test.tmp")
        os.remove("glue.tmp")
        os.remove("data_definition.tmp")

    def test_print(self, line):
        self.test_file.write(line + "\n")

    def data_definition_print(self, line):
        self.data_definition_file.write(line + "\n")

    def template_print(self, line):
        self.glue_template_file.write(line + "\n")

    def end_up(self):
        if self.cleanup:
            self.test_print("        test_Cleanup()")
        self.test_print("        }")  # End last scenario
        self.test_print("    }")  # End the class
        self.test_print("")
        self.template_print("    }")  # End the class
        self.test_file.close()
        self.glue_template_file.close()
        self.data_definition_file.close()

    def transpose(self, matrix):
        transposed = [["" for _ in range(len(matrix))] for _ in range(len(matrix[0]))]
        size_row = len(matrix[0])
        for element in matrix:
            if len(element) != size_row:
                self.error("*** Table has uneven rows - not transposed")
                self.error("     Will probably exit ")
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                transposed[j][i] = matrix[i][j]
        return transposed

    def trace(self, value):
        if Configuration.trace_on:
            print(value)

    def error(self, value):
        print("*** " + value)

    def end_up(self):
        if self.cleanup:
            self.test_print("        test_Cleanup()")
        self.test_print("        }")  # End last scenario
        self.test_print("    }")  # End the class
        self.test_print("")
        self.template_print("    }")  # End the class
        self.test_file.close()
        self.glue_template_file.close()
        self.data_definition_file.close()

    def transpose(self, matrix):
        transposed = [["" for _ in range(len(matrix))] for _ in range(len(matrix[0]))]
        size_row = len(matrix[0])
        for element in matrix:
            if len(element) != size_row:
                self.error("*** Table has uneven rows - not transposed")
                self.error("     Will probably exit ")
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                transposed[j][i] = matrix[i][j]
        return transposed

    def trace(self, value):
        if Configuration.trace_on:
            print(value)

    def test_print(self, line):
        self.test_file.write(line + "\n")


class InputIterator:
    EOF = "EOF"
    includeCount = 0

    def __init__(self, name):
        self.linesIn = []
        self.index = 0
        if name:
            self.read_file(name)

    def read_file(self, file_name):
        InputIterator.includeCount += 1
        if InputIterator.includeCount > 20:
            self.error("Too many levels of include")
            return
        with open(os.path.join(Configuration.feature_sub_directory, file_name), 'r') as file:
            raw = file.readlines()
        for line in raw:
            if line.startswith("Include"):
                parts = line.split("\"")
                self.trace("Parts are " + str(parts))
                if len(parts) < 2:
                    self.error("Error filename not surrounded by quotes: " + line)
                    continue
                if not parts[1]:
                    self.error("Error zero length filename " + line)
                    continue
                included_file_name = parts[1].strip()
                self.trace("Including " + included_file_name)
                if included_file_name.endswith(".csv"):
                    self.include_csv_file(included_file_name)
                else:
                    self.read_file(included_file_name)
            else:
                if line and line[0] != '#':
                    self.linesIn.append(line.strip())
        InputIterator.includeCount -= 1

    def include_csv_file(self, included_file_name):
        with open(os.path.join(Configuration.feature_sub_directory, included_file_name), 'r') as file:
            raw = file.readlines()
        for line in raw:
            if not line:
                continue
            contents = self.convert_csv_to_table(line)
            self.linesIn.append(contents.strip())

    def convert_csv_to_table(self, csv_data):
        lines = csv_data.split("\n")
        data = [self.parse_csv_line(line) for line in lines]
        formatted_data = ["|" + "|".join(row) + "|" for row in data]
        return "\n".join(formatted_data)

    def parse_csv_line(self, line):
        result = []
        current = []
        in_quotes = False
        i = 0
        while i < len(line):
            char = line[i]
            if char == '"':
                if in_quotes and i + 1 < len(line) and line[i + 1] == '"':
                    current.append('"')
                    i += 1
                else:
                    in_quotes = not in_quotes
            elif char == ',' and not in_quotes:
                result.append("".join(current))
                current = []
            else:
                current.append(char)
            i += 1
        result.append("".join(current))
        return result

    def peek(self):
        if self.index < len(self.linesIn):
            return self.linesIn[self.index]
        else:
            return InputIterator.EOF

    def next(self):
        if self.index < len(self.linesIn):
            item = self.linesIn[self.index]
            self.index += 1
            return item
        else:
            return InputIterator.EOF

    def trace(self, value):
        if Configuration.trace_on:
            print(value)

    def error(self, value):
        print("*** " + value)


class Configuration:
    trace_on = True  # Set to true to see trace
    space_characters = '^'  # Will replace with space in tables
    current_directory = ""
    feature_sub_directory = ""
    package_name = "gherkinexecutor"
    test_sub_directory = ""  # + packageName + "\\"
    data_definition_file_extension = "tmpl"  # change to kt if altering data file
    feature_files = [
        # "tictactoe.feature",
        # "smoketest.feature",
        # "GherkinTranslator.feature",
        # "include.feature",
        # "testfeature.feature",
        # "examples.feature",
        # "tablesandstrings.feature",
        # "FlowGrid.feature",
        # "Robot Game.feature",
        # "data_definition.feature",
        # "ParseCSV.feature",
        "SimpleTest.feature",
        # "GherkinTranslatorSmokeTest.feature",
        # "GherkinTranslatorFullTest.feature"
    ]


def main(args):
    print("Gherkin Executor")
    Configuration.current_directory = os.getcwd()
    print("Arguments")
    for arg in args:
        print("   " + arg)
        Configuration.feature_files.append(arg)
    for name in Configuration.feature_files:
        translate = Translate()
        print("Translating " + name)
        translate.translate_in_tests(name)


if __name__ == "__main__":
    import sys

    main(sys.argv[1:])
