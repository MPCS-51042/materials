#Pending - scenario with emtpy string returns: Whoops. For example ('', []), the function returned [''].

string_of_letters = "b-D,z,m-q,n,C-E"

def expand_letter_ranges(string_of_letters):
    '''
        This function takes in a comma-separated string of letters and letter ranges and
        returns a list of the letters and expanded ranges in alphabetical order.

        Inputs:
            string_of_letters (string): a comma-separated string of letters and letter ranges.

        Output:
            a list of the letters and expanded ranges in alphabetical order.
        '''
    ABC = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    list_input = string_of_letters.split(',')
    letter_list = []

    #Main algorithm

    #Scenario 1: empty list
    if list_input == []:
        output_list = []
    #Scenario 2: non empty list
    else:
        for letter in list_input:
            if '-' in letter:
                first_index = ABC.index(letter[0].upper())
                last_index = ABC.index(letter[-1].upper())
                for x in range(first_index, last_index+1):
                    letter_list.append(ABC[x])
            else:
                letter_list.append(letter.upper())


    #Remove duplicates and sort
    output_list = []

    for item in letter_list:
        if item not in output_list:
            output_list.append(item)

    output_list.sort()
    return output_list

#print(expand_letter_ranges(string_of_letters))



