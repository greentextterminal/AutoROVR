"""This file contains the source code for getting the cardinal/intercardinal directions from row,col matrix system"""

import numpy as np

#test_arr = np.array([(0, 2), (1, 2), (2, 2), (2, 1), (2, 0), (1, 0), (0, 0), (0, 1), (0, 2)],
#                    dtype=[('x', int), ('y', int)])
# test_arr = np.array([(0, 2), (1, 1), (2, 0), (1, 0), (0, 0), (0, 1), (1, 2), (2, 1), (1, 1)],
#                     dtype=[('x', int), ('y', int)])
# test_arr = np.array([(0, 2)],
#                     dtype=[('x', int), ('y', int)])
# test_arr = np.array([( 2,  0), ( 3,  1), ( 3,  2), ( 4,  3), ( 4,  4), ( 5,  5), ( 6,  6), ( 6,  7), ( 7,  8), ( 7,  9), ( 8, 10),
#                      ( 8, 11), ( 9, 12), (10, 13), (10, 14), (11, 15), (11, 16), (12, 17), (13, 18), (13, 19), (14, 20),
#                      (14, 21), (15, 22), (15, 23), (16, 24), (17, 25), (17, 26), (18, 27), (18, 28), (19, 29)],
#                     dtype=[('x', int), ('y', int)])


def navigation_directions(cells_array):
    """Parses a cell array in order to determine the direction from cell to cell
    and returns a cardinal or intercardinal symbol """
    array_length = len(cells_array)
    if array_length == 0:
        print('cells array is empty')
        return 1
    direction_list = np.empty((0,), dtype='str')

    for idx, cell in enumerate(cells_array):
        if idx == (array_length - 1):
            print('end reached or array contained 1 cell')
        else:
            # cell variables for comparison
            curr_cell = cells_array[idx]
            next_cell = cells_array[idx + 1]

            # comparison cells isolated x and y components
            curr_cell_row = curr_cell[0]
            curr_cell_col = curr_cell[1]

            next_cell_row = next_cell[0]
            next_cell_col = next_cell[1]

            direction = None  # undeclared direction

            # N , NW, NE case
            if next_cell_row == (curr_cell_row + 1):
                if next_cell_col == (curr_cell_col - 1):  # NW
                    direction = 'NW'
                elif next_cell_col == (curr_cell_col + 1):  # NE
                    direction = 'NE'
                else:  # N
                    direction = 'N'
            # S, SW, SE case
            elif next_cell_row == (curr_cell_row - 1):
                if next_cell_col == (curr_cell_col - 1):  # SW
                    direction = 'SW'
                elif next_cell_col == (curr_cell_col + 1):  # SE
                    direction = 'SE'
                else:  # S
                    direction = 'S'
            # W, E case
            elif next_cell_row == curr_cell_row:
                if next_cell_col == (curr_cell_col + 1):  # E case
                    direction = 'E'
                else:  # W case
                    direction = 'W'

            # appending direction list with next direction
            direction_list = np.append(direction_list, np.array([direction], dtype='str'))

    return direction_list


#print(navigation_directions(test_arr))
