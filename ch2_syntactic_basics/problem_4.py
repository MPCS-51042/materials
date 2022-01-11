
def expand_letter_ranges(string_of_letters):
    '''
        This function takes in a comma-separated string of letters and letter ranges and
        returns a list of the letters and expanded ranges in alphabetical order.

        Inputs:
            string_of_letters (string): a comma-separated string of letters and letter ranges.

        Output:
            a list of the letters and expanded ranges in alphabetical order.
        '''
    pass



string_1 = "1, 2, 20,22, 44, 99"
string_2 = "3,5, 22, 100, 44, 2"

def removeSpaces(string):
    string = string.replace(' ','')
    return string

string_1_no_space = removeSpaces(string_1)

list_1 = string_1_no_space.split(',')


list_2 = string_2.split(',')
req_value = '2'
output_list = []

for num in list_1:
    if req_value in num:
        print(int(num))

print(list_1)
print(list_2)