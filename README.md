# Gherkin Executor for Python

The full documentation is at [GitHub - atdd-bdd/GherkinExecutorBase: This is the base for Gherkin Executor containing Documentation and Examples](https://github.com/atdd-bdd/GherkinExecutorBase)

You can see an example of a featurex file at:

[GherkinExecutorForPython/tests/examples.feature at main · atdd-bdd/GherkinExecutorForPython · GitHub](https://github.com/atdd-bdd/GherkinExecutorForPython/blob/main/tests/examples.feature)

The generated code, as well as the altered glue file are in this directory:: 

[GherkinExecutorForPython/tests/gherkinexecutor/Feature_Examples at main · atdd-bdd/GherkinExecutorForPython · GitHub](https://github.com/atdd-bdd/GherkinExecutorForPython/tree/main/tests/gherkinexecutor/Feature_Examples)

To install a Gherkin Executor for your project:

- Create a new project 

- Copy `translate.py`into the project

- Create a `tests `directory

- Copy` starting.featurex` into the `tests `directory

- Alter `test_framework = "unittest"`to` test_framework = "pytest" `if using pytest 

- Execute` translate.py` with `starting.featurex` as an argument.

You should see a directory` tests/gherkinexecutor/Feature_Starting` 

In that directory, there are four files.      

- The tests are in` test_Feature_Starting.py  `

- You need to rename Feature_Starting_glue.tmpl to Feature_Starting_glue.py.     This is the file you will alter to call the production code.   

- Run the tests in `test_Feature_Starting.py`

- They should all fail.   Create a temperature convertor and alter the glue code to call it. 
