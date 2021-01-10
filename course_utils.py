class Test:
    def __init__(self, examples=[], function=None, test_class=None):
        self.examples = examples
        self.function = function
        self.test_class = test_class
        self.passed = 0
        self.run = 0

    def equivalence(self):
        for i, (actual, expected) in enumerate(self.examples):
            self.run += 1
            if expected == actual:
                self.passed += 1
            else:
                print(
                    f"Whoops. For example {i}, the function returned {actual} and should've returned {expected}."
                )

        print(f"\n{self.passed} out of {self.run} examples worked as expected.")

    def generator_function(self):
        for i, example in enumerate(self.examples):
            self.run += 1
            expected = example[-1]
            actual = list(self.function(*example[:-1]))

            if expected == actual:
                self.passed += 1
            else:
                print(
                    f"Whoops. For example {i}, the function returned {actual} and should've returned {expected}."
                )

        print(f"\n{self.passed} out of {self.run} examples worked as expected.")

    def passed_function(self):
        for i, example in enumerate(self.examples):
            self.run += 1
            test_func, inputs, expected = example
            actual = self.function(test_func)(*inputs)

            if expected == actual:
                self.passed += 1
            else:
                print(
                    f"Whoops. For example {i} wrapping {test_func} with inputs {inputs}, the function returned {actual}."
                )

        print(f"\n{self.passed} out of {self.run} examples worked as expected.")

    def pitch_errors(self):
        for i, (string, error) in enumerate(self.examples):
            self.run += 1
            found = False
            try:
                eval(string, {"Pitch": self.test_class})
            except ValueError:
                if error == ValueError:
                    self.passed += 1
                    found = True
            except TypeError:
                if error == TypeError:
                    self.passed += 1
                    found = True
            finally:
                if not found:
                    print(
                        f"Whoops. For example {i}, the expression {string} failed to throw {error}."
                    )

        print(f"\n{self.passed} out of {self.run} examples worked as expected.")


def first_digit(x):
    return int(str(x)[0])
