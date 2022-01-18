def find_numbers():
    '''
        This function computes the combinations of the numbers, 1 through 9, for which

        ABC = A*B*C*(A+B+C)
    '''
    result = []
    
    digits = range(1,10)
    for a in digits:
        for b in digits:
            for c in digits:
                if (100*a+10*b+c) == (a*b*c*(a+b+c)):
                    result.append("For {}, {}, and {}, the equation solution is {}".format(a,b,c,100*a+10*b+c))
    
    return result