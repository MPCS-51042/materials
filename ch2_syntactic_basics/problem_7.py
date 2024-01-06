
def find_minimum(sequence, comparator=None):
    '''
    :param sequence: a list of items (like numbers or strings) that decreases, then increases

    :param comparator (optional): a function that takes in TWO items
    and returns a boolean indicating whether the first one is smaller than the second

    :return: A tuple containing the smallest item and the index at which it occurs
    '''
    # assumes sequence is a list of integers as per examples given. 
    error = "Invalid Sequence"
    decreasing = False
    increasing = False 

    for i in range(1,len(sequence)-1):
        if sequence[i] < sequence[i-1]:
            if increasing == True:
                return error
            decreasing = True
        elif sequence[i] == sequence[i-1]:
            return error 
        elif sequence[i] > sequence[i-1] and sequence[i-1] < sequence[i-2]:
            increasing = True

    if not (decreasing and increasing):  #doesnt make a v shape
        return error

    #now that we have confirmed valid, find min

    for i in range(1, len(sequence) - 1):
        if sequence[i] < sequence[i-1] and sequence[i] < sequence[i+1]:
            return (sequence[i], i)


class TrainingAttempt():
    def __init__(self, id, weights, error):
        self.id = id
        self.weights = weights
        self.error = error

    def __repr__(self):
        return f'TrainingAttempt {self.id}'

def total_error(training_attempt):
    '''
    :param training_attempt: a TrainingAttempt

    :return: the error of a given TrainingAttempt
    '''
    pass
