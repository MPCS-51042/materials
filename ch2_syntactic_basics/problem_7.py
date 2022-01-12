
from typing import Sequence


def find_minimum(sequence, comparator=None):
    '''
    :param sequence: a list of items (like numbers or strings) that decreases, then increases

    :param comparator (optional): a function that takes in TWO items
    and returns a boolean indicating whether the first one is smaller than the second

    :return: A tuple containing the smallest item and the index at which it occurs
    '''
    pass

sequence = [6, 5, 4, 3, 2, 3, 4, 5, 6, 7]

min_seq = min(sequence)
index_min = sequence.index(min_seq)

flag_1 = False
for item in range(0, index_min):
    if sequence[item+1] > sequence[item]:
        print('yes')
    else:
        print('no')

#Scenarios


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
