class FeatureSimpleTestGlue:
    def given_table_is(self, value : list):
        print("*******")
        print(value)
        self.fail("Must implement")

    def fail(self, message):
        raise AssertionError(message)
