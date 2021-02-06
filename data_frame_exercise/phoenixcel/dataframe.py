import csv


class Series(list):
    def sum(self):
        return sum(self)

    def average(self):
        return sum(self) / len(self)

    avg = average

    def apply(self, func):
        self = [func(x) for x in self]
        return self


class GroupBy(dict):
    def sum(self, on=None):
        return self.aggregate(on=on, using_func=sum)

    def average(self, on=None):
        def func(listo):
            return sum(listo) / len(listo)

        return self.aggregate(on=on, using_func=func)

    avg = average

    def count(self, on=None):
        return self.aggregate(on=on, using_func=len)

    def aggregate(self, on=None, using_func=None):
        aggregator = {}
        if on == None:
            raise Exception("What column do you want aggregated?")
        if using_func == None:
            raise Exception(f"How do you want '{on}' aggregated?")
        else:
            for key in self.keys():
                addends = [item[on] for item in self[key]]
                aggregator[key] = using_func(addends)
        return aggregator


class DataFrame():
    def __init__(self):
        self._dictionary = {}
        self._list = []

    # Ways to crate an instance
    @classmethod
    def from_csv(cls, file_path):
        df = cls()
        header_unread = True

        with open(file_path) as f:
            reader = csv.DictReader(f)

            for row in reader:
                if header_unread:
                    for key in row.keys():
                        df._dictionary[key] = Series()
                    header_unread = False
                else:
                    df._list.append(row)

                for key in row.keys():
                    df._dictionary[key].append(row[key])

            for key in list(df._dictionary.keys()):
                setattr(df, key.lower().replace(" ", "_"), df._dictionary[key])
        return df

    @classmethod
    def from_rows(cls, rows):
        df = cls()
        for key in rows[0].keys():
            df._dictionary[key] = Series()
        for row in rows:
            for key in rows[0].keys():
                df._dictionary[key].append(row[key])
            df._list.append(row)

        for key in list(df._dictionary.keys()):
            setattr(df, key.lower().replace(" ", "_"), df._dictionary[key])

        return df

    @classmethod
    def from_dictionary(cls, dictionary):
        df = cls()
        df._dictionary = dictionary
        for i in range(len(dictionary[list(dictionary.keys())[0]])):
            item = {}
            for key in dictionary.keys():
                item[key] = dictionary[key][i]
            df._list.append(item)

        for key in list(df._dictionary.keys()):
            setattr(df, key.lower().replace(" ", "_"), df._dictionary[key])

        return df

    # Properties
    @property
    def shape(self):
        return \
            len(self._dictionary.keys()), \
            len(self._dictionary[list(self._dictionary.keys())[0]])

    @property
    def columns(self):
        return list(self._dictionary.keys())

    # Methods for getting a column in the dictionary
    def __getitem__(self, item):
        '''
        Get a reference to a column in the dataframe.

        Input:
          item - the column header

        Output:
          the column, which is a series

        Modifies:
          Nothing
        '''
        return self._dictionary[item]

    # Method for setting a column in the dictionary
    def __setitem__(self, key, value):
        '''
        Set a new column in the dataframe.

        Inputs:
          key - the column header
          value - the column (as a Series for consistency, please)

        Outputs:
          None

        Modifies:
          Modifies the dataframe object in place.
        '''
        self._dictionary[key] = value
        for index, item in enumerate(self._list):
            item[key] = value[index]

        setattr(self, key.lower().replace(" ", "_"), self._dictionary[key])

    def where(self, condition):
        df = self
        rows = [row for row in self._list if condition(row)]
        return DataFrame.from_rows(rows)

    def group_by(self, column):
        '''
        Returns an object that aggregates the items in the dataframe
        based on one value that they have in common,
        similar to a pivot table in the software to which
        phoenixcell's name pays tribute (Please don't sue me, Microsoft)

        Inputs:
          column - the column on whose value the items should be grouped

        Outputs:
          A new GroupBy() object

        Modifies:
          Nothing
        '''
        groups = GroupBy()
        for item in self._list:
            maybe_unique_column_value = item[column]
            if maybe_unique_column_value in groups.keys():
                groups[maybe_unique_column_value].append(item)
            else:
                groups[maybe_unique_column_value] = Series()
                groups[maybe_unique_column_value].append(item)
        return groups