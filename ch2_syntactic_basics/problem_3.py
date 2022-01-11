#string_1 = "1, 2, 20,22, 44, 99"
#string_2 = "3,5, 22, 100, 44, 2"

def removeSpaces(string):
    string = string.replace(' ','')
    return string

def find_twos(string_1, string_2):
    '''
        This function takes in two strings that only contains integers, commas and whitespace and
        returns a list of integers, where each integer,

           1. Appears in both strings
           2. Contains a 2 as a digit in the number.

        Inputs:
            str1, str2 (string): strings that contains integers, commas, and whitespace. You can assume each integer is separated by a single comma followed by zero or more whitespaces.

        Output:
            A list of integers, where the list contents is described by above. The returned list must not contain duplicates.
        '''
    string_1_no_space = removeSpaces(string_1)
    list_1 = string_1_no_space.split(',')
    string_2_no_space = removeSpaces(string_2)
    list_2 = string_2_no_space.split(',')
    
    req_value = '2'

    output_list = []

    for num in list_1:
        if num in list_2 and req_value in num:
            output_list.append(int(num))
    
    unique_list = []   
    for item in output_list:
        if item not in unique_list:
            unique_list.append(item)

    return unique_list
    
#print(find_twos(string_1,string_2))
