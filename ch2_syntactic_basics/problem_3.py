
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
    string1_list = [num.strip() for num in string_1.split(",")]
    string2_list = [num.strip() for num in string_2.split(",")]
    matches = []
    for number in string1_list:
        if "2" in number:
            if number in string2_list:
                if int(number) not in matches:
                    matches.append(int(number))
    return matches 







# looked up from: https://stackoverflow.com/questions/7844118/how-to-convert-comma-delimited-string-to-list-in-python 
# 
