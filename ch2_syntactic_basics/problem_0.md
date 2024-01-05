## Explaining the `test` method:

**1. What are the arguments and what types do these arguments need to have for this function to work?**
2 arguments, function and examples.
Function refers to a function that will be called and tested with the examples.
The examples can be fed in as a list of examples with each "example" being a tuple. Based on the code, it should be such that the last value of the tuple is the expected result of the function.

**2. Walk us through the code line by line. What is happening here?**
first two lines rerun the kernel

First we define the name of the function we are creating, and its inputs (function, examples).
We initate two variables with integer values, passed and run and set them equal to 0.
We start to loop through the examples in our examples object. For each 'example' in examples, we go through the following operation:
- first increment up our run variable by 1 to keep track of how many times we have checked an example.
Since these examples are known, we create a new variable, expected, to keep track of what the function should return for the example and set it equal to the last value in the example tuple under review. Then we compute what the function actually returns within the actual function we are testing and input all of the values in the example tuple except the last (answer) value. 

If the expected variable equals the actual variable, we increment up our "passed" variable by 1. If it is not equal, it means our function failed and we display the error message including details on what example we were testing and what result we actual achieved.

Once we have run through all examples in above fashion, we print out how many passed runs (where actual == expected) occured out of all runs (number of examples tested).

**3. Does this function have a return value? How do you know?**
Yes, but the return function is None given that we do not define another return value.