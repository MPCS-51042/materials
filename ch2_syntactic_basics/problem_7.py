
def find_minimum(sequence, comparator=None):
    '''
    :param sequence: a list of items (like numbers or strings) that decreases, then increases

    :param comparator (optional): a function that takes in TWO items
    and returns a boolean indicating whether the first one is smaller than the second

    :return: A tuple containing the smallest item and the index at which it occurs
    '''
    #process the input based on comparator
    if comparator == len:
        sequence_input = list(map(len, sequence))
    elif comparator == total_error:
        sequence_input = []
        for i in sequence:
            sequence_input.append(i.error)
    else:
        sequence_input = list(map(int, sequence))
        
    #find min in the sequence
    min = sequence_input[0]
    for i in sequence_input:
        if i < min:
            min = i

    #find the index of the min value 
    min_index = sequence_input.index(min)

    #divide the sequence into the left and right part
    sequence_left = sequence_input[:min_index]
    sequence_right = sequence_input[min_index:]

    #check if the left part is strictly decrease :
    decrease_check = all(i > j for i, j in zip(sequence_left, sequence_left[1:]))
    
    #check if the right part is strictly increase
    increase_check = all(i < j for i, j in zip(sequence_right, sequence_right[1:]))

    #print result
    if len(sequence_right) != 1 and len(sequence_left) != 0:
        if decrease_check == True and increase_check == True:
            if comparator == len or comparator == total_error:
                return (sequence[min_index],min_index)
            else:
                return (min,min_index)
        else:
            return "Invalid Sequence"
    else:
        return "Invalid Sequence"

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
    return training_attempt.error
