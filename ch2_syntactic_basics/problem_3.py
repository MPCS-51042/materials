
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
    list1 = string_1.split(",")
    list2 = string_2.split(",")
    
    result = []
    
    for a in list1:
        a3 = a.strip()
        if "2" in a3:
            for b in list2:
                if (b.strip() == a3) and (int(a3) not in result):
                    result.append(int(a3))
    return result
    
   