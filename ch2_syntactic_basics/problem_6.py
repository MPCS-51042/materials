#Pending: List. Solo falta beautify y explanations

def find_numbers():
    '''
        This function computes the combinations of the numbers, 1 through 9, for which

        ABC = A*B*C*(A+B+C)
    '''
    possible_numbers = [1,2,3,4,5,6,7,8,9]
    input_list = []
    output_list = []

    for x in possible_numbers:
        for y in possible_numbers:
            for z in possible_numbers:
                total_result = x*100 + y*10 + z*1

                if total_result == x*y*z * (x + y + z):
                    input_list.append([x,y,z])
                    output_list.append(total_result)

    solution = []

    for result in range(len(output_list)):
         solution.append('For {0}, {1}, and {2}, the equation solution is {3}'.format(input_list[result][0], input_list[result][1], input_list[result][2], output_list[result]))

    return solution
            
#print(find_numbers())

