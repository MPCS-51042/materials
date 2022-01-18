
def mean(string_of_numbers):
    '''
        This function takes in a space-separated string of integers and floats and
        returns a their mean as a float.

        Inputs:
            string_of_numbers (string): a space-separated string of integers and floats.

        Output:
            a float, the mean of the inputted numbers.
        '''
    if string_of_numbers == "":
        return 0.0
    else: 
        inputs = list(map(float, string_of_numbers.split(" ")))
        result = sum(inputs)/len(inputs)
        return result