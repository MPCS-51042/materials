class Stream:
    def __init__(self, items_as_list=[]):
        self._data = items_as_list

    # maybe they can add methods to push to, pop from, and even index off of the stream? maybe not index

    def map(self, function):
        # start with these as loops and challenge them to change them to listcomps?
        self._data = [function(x) for x in self._data]
        # they should be able to explain why we need this line
        return self

    def filter(self, function):
        # after they change to list comps, can they further change this to a generator?
        # What would that do? How can they check whether it did that?
        self._data = [x for x in self._data if function(x) == True]
        return self

    def reduce(self, function):
        # Can they explain what is happening here?
        iterable = iter(self._data)
        combined_value = next(iterable)
        for next_element in iterable:
            combined_value = function(combined_value, next_element)
        return combined_value

    def as_list(self):
        return self._data

