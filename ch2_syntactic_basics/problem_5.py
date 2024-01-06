
def mean(string_of_numbers):
    '''
        This function takes in a space-separated string of integers and floats and
        returns a their mean as a float.

        Inputs:
            string_of_numbers (string): a space-separated string of integers and floats.

        Output:
            a float, the mean of the inputted numbers.
        '''
    if not string_of_numbers:
        return 0
    else:
        number_list = [int(number) for number in string_of_numbers.split(" ") if number != ""] 
        return sum(number_list)/len(number_list)