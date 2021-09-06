
def power_status(grid, row_bounds, col_bounds):
    '''
    Determines the status of the homes within a sector. A sector is defined by a row  and column
    boundary. A row boundary is a tuple of two integers from ([0, nRows), [0, nRows)) and the column
    boundary is a tuple of two integers ([0, nColumns), [0, nColumns)), where nRows is equal to the
    number of rows in the grid and nColumns is equal to the number of columns in the grid. Make note
    the upper-bound is exclusive!

    Based on the boundary specified, the function returns a list indicating the power status of the
    homes within the bounds of the sector. Order in the list does matter! Start at the top-left of the
    sector and work your way down towards the bottom-right corner. You increase by in the columns. Once
    you finish with a row then you move to the next row (i.e., increase by 1).

    You can assume the the first component of the boundary is always less than the second component.

    Inputs:
        grid(list of list of bools): the status of the homes
        row_bounds(tuple of ints): the row boundary for the sector
        col_bounds(tuple of ints): the column boundary for the sector

    Outputs:
        Returns a list of booleans indicating the power status of the homes within the bounds of the sector.

    '''
    pass
