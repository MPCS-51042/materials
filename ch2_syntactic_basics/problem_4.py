
def expand_letter_ranges(string_of_letters):
    '''
        This function takes in a comma-separated string of letters and letter ranges and
        returns a list of the letters and expanded ranges in alphabetical order.

        Inputs:
            string_of_letters (string): a comma-separated string of letters and letter ranges.

        Output:
            a list of the letters and expanded ranges in alphabetical order.
        '''
    #take the string, seperate into a list by commas.
    string_list = [value for value in string_of_letters.split(",")]
    expanded_letters = set()
    
    for value in string_list:
        if "-" in value:
            start, end = value.split("-")
            start_value = ord(start.upper())
            end_value = ord(end.upper())
            while start_value <= end_value:
                expanded_letters.add(chr(start_value))
                start_value +=1
        else:
            expanded_letters.add(value.upper())
    expanded_letters_list = sorted(list(expanded_letters_set))
    return expanded_letters
            

    # intiate new empty list numbered_list
    # for each part of the list, if there's a hyphen, then what should I do?
    # for items in list where there's no hyphen, convert to lowercase then convert to number with ord() and append to numbered_list.
    # sort numbered list
    #