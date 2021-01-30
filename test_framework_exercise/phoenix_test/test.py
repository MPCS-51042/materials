from colorama import Fore, Back, Style

class Test():
    types = []

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        cls.types.append(cls)

    @classmethod
    def run_all(cls, only=""):
        pass_count = 0
        run_count = 0

        for typ in cls.types:
            print(f"Running {typ.__name__}: ")
            passed, runned = typ().run(only=only)
            pass_count += passed
            run_count += runned

        print(f"{pass_count} out of {run_count} tests passed.\n")

    def setup(self):
        pass

    def teardown(self):
        pass

    def run(self, only=""):
        run_count = 0
        pass_count = 0
        test_methods = [
            token for token in dir(self) \
            if token.startswith("test") \
            and only in token \
            and callable(getattr(self.__class__, token))
            ]
        for method in test_methods:
            self.setup()
            run_count += 1
            try:
                getattr(self.__class__, method).__call__(self)
                pass_count += 1
                print(Fore.GREEN + f"    {method} passed!")
            except Exception as e:
                print(Fore.RED + f"    {method}:  {e}")
                self.teardown()
        print(Style.RESET_ALL + f"    {pass_count} out of {run_count} tests passed.\n")
        return pass_count, run_count
