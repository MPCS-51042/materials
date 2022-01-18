## Explaining the `test` method:

**1. What are the arguments and what types do these arguments need to have for this function to work?**
    To have the test function to work, we need to have 2 arguments: function and examples. 
    The 'function' is a function that we want to test whether it works with all the test cases. 
    The 'examples' is a list of all the test cases. Each test case is a tuple that consists of inputs for the 'function' and expected result. The expected result is placed in the last position (or the last item) in each test case. 
  
**2. Walk us through the code line by line. What is happening here?**
    First we set two variables, 'passed' and 'run', equal 0.
    For each test case in the 'examples' argument, we will add 1 to the 'run' variable. This is to count how many test cases we run in total at the end. 
    Also, in each test case, we set 'expected' variable (expected result) equal to the last item in the test case. For the remainding items in each test case, we use them as inputs for 'function', generating 'actual' variable (actual result).
    If the expected result equals to actual result, we add 1 to the 'passed' variable. Otherwise, we print out a statement stating that "Whoops. For example {example}, the function returned {actual}." This means to show users the difference in actual and expected results, given the inputs. 
    After going through all test case, the 'test' function will print out the number of passes out of the total test cases it ran. 
  
**3. Does this function have a return value? How do you know?**
    Yes, this function has a "None" return value because when we print out the function: print(test(function, examples)), we will get "None".