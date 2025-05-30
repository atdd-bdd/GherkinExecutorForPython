# Gherkin Executor for Python

This application is in development mode.   It is being converted from java to python.    

The full documentation is at [GitHub - atdd-bdd/GherkinExecutorForJava: Gherkin Executor for Java translates Gherkin files into unit tests](https://github.com/atdd-bdd/GherkinExecutorForJava)

The examples.feature file shows how it works.    



To install a Gherkin Executor for your project:

- Create a new project 

- Copy `translate.py`into the project

- Create a `tests `directory

- Copy` starting.feature` into the `tests `directory

- Alter `test_framework = "unittest"`to` test_framework = "pytest" `if using pytest 

- Execute` translate.py` with `starting.feature` as an argument.   

You should see a directory` tests/gherkinexecutor/Feature_Starting` 

In that directory, there are four files.      

- The tests are in` test_Feature_Starting.py  `

- You need to rename Feature_Starting_glue.tmpl to Feature_Starting_glue.py.     This is the file you will alter to call the production code.   

- Run the tests in `test_Feature_Starting.py`

- They should all fail.   Create a temperature convertor and alter the glue code to call it. 
