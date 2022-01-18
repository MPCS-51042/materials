
def expand_letter_ranges(string_of_letters):
    '''
        This function takes in a comma-separated string of letters and letter ranges and
        returns a list of the letters and expanded ranges in alphabetical order.

        Inputs:
            string_of_letters (string): a comma-separated string of letters and letter ranges.

        Output:
            a list of the letters and expanded ranges in alphabetical order.
        '''
    if string_of_letters == "":
        return []

    else:
        inputs = string_of_letters.split(",")
        output_num = []

        for input in inputs:
            input_uppercase = input.upper()

            if "-" in input_uppercase:
                start = ord(input_uppercase[0])
                end = ord(input_uppercase[-1])
                for i in range(start, end+1):
                    output_num.append(i)
            else:
                output_num.append(ord(input_uppercase))
        
        output = []

        for item in sorted(output_num):
            if chr(item) not in output:
                output.append(chr(item))
        
        return output
    