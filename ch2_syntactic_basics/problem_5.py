
def find_minimum(sequence, comparator=None):
    '''
    :param sequence: a list of items (like numbers or strings) that decreases, then increases

    :param comparator (optional): a function that takes in TWO items
    and returns a boolean indicating whether the first one is smaller than the second

    :return: A tuple containing the smallest item and the index at which it occurs
    '''
    pass

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
