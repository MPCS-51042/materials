#string_of_numbers = "1 2 3"

def mean(string_of_numbers):
    '''
        This function takes in a space-separated string of integers and floats and
        returns a their mean as a float.

        Inputs:
            string_of_numbers (string): a space-separated string of integers and floats.

        Output:
            a float, the mean of the inputted numbers.
        '''
    list_input = string_of_numbers.split(' ')

    if string_of_numbers == '':
        mean = 0.0
    else:
        list_numbers = []
        for item in list_input:
            list_numbers.append(int(item))

        total_calculation = sum(list_numbers)

        mean = total_calculation/len(list_numbers)

    return mean

#print(mean(string_of_numbers))