class FailedAssertion(Exception):
    pass

class Assertion:
    def __init__(self, expression):
        self.expression = expression

    def is_true(self):
        '''
            Returns True if expression evaluates to true
            And raises a FailedAssertion if it doesn't.
        '''
        if self.expression:
            return True
        else:
            raise FailedAssertion(f"Expected the asserted expression to be true, but was false.")

    def equals(self, expected_result):
        '''
            Returns True if expression == expected result
            And raises a FailedAssertion if it doesn't.
        '''
        if self.expression == expected_result:
            return True
        else:
            raise FailedAssertion(f"Expected {expected_result} but got {self.expression}")

    def is_empty(self):
        '''
            This method returns True if a collection has no items
            And it raises a FailedAssertion if it doesn't.
        '''
        if len(self.expression) == 0:
            return True
        else:
            raise FailedAssertion(f"Expected {self.expression} to be empty")


    def has_size(self, size):
        '''
            This method returns True if a collection has the right number of items
            And it raises a FailedAssertion if it doesn't.
        '''
        if len(self.expression) == size:
            return True
        else:
            raise FailedAssertion(f"Expected {self.expression} to have size {size} but it instead had size {len(self.expression)}")

    def has_items(self, *args):
        '''
            This method returns True if a collection has the right items
            And it raises a FailedAssertion if it doesn't.
        '''
        missing_items = []
        for item in args:
            if not item in self.expression:
                missing_items.append(item)
        if missing_items:
            raise FailedAssertion(f"Expected {self.expression} to have items {missing_items}")

def assert_that(expression):
    return Assertion(expression)