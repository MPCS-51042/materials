def find_numbers():
    '''
        This function computes the combinations of the numbers, 1 through 9, for which

        ABC = A*B*C*(A+B+C)
    '''
    solutions = []

    #note kept cap letters to align with prompt, not pythonic i don't think
    for A in range(1,10):
        for B in range(1,10):
            for C in range(1,10):
                if A*B*C*(A+B+C) == (A*100+B*10+C):
                    solutions.append(f"For {A}, {B}, and {C}, the equation solution is {(A*100+B*10+C)}")
    return solutions 