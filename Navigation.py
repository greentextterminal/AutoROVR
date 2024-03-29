import math
import numpy as np
import matplotlib.pyplot as plt

np.set_printoptions(threshold=np.inf, linewidth=10000)  # fully prints matrix; full width


# USE NUMPY LISTS FOR STORING DATA SINCE THEY ARE MORE COMPRESSED !!!
# matrix map needs to be double the distance from the furthest distance between two cells in a path
# start node needs to be centered in the map so that the cells are inside the matrix "map"


def mile_to_meters(miles):
    """convert miles to meters"""
    return miles * 1609.34


def nearest_meter(meters):
    """get nearest integer meter from float"""
    return math.ceil(meters)


def bresenham_line(start_x, start_y, end_x, end_y):
    """creates line trace from cells connecting a start and an end and returns cell array that make the line"""
    dx = abs(end_x - start_x)
    dy = abs(end_y - start_y)
    if start_x < end_x:
        sx = 1
    else:
        sx = -1
    if start_y < end_y:
        sy = 1
    else:
        sy = -1
    error = dx - dy
    # line_cells = []
    line_cells = np.empty((0,), dtype=[('x', int), ('y', int)])

    while True:
        # line_cells.append((start_x, start_y))
        line_cells = np.append(line_cells, np.array([(start_x, start_y)], dtype=line_cells.dtype))
        if start_x == end_x and start_y == end_y:
            break
        doubled_error = 2 * error
        if doubled_error > -dy:
            error -= dy
            start_x += sx
        if doubled_error < dx:
            error += dx
            start_y += sy

    return line_cells


# visualize map and nodes
def visualizer(matrix, max_val):
    """creates and shows a colored NxN trial matrix populated with obstacles"""
    # 0 for free cell, 1 for start, 2 for end, 3 for path
    plt.rcParams["figure.figsize"] = [7.50, 3.50]
    plt.rcParams["figure.autolayout"] = True

    fig, ax = plt.subplots()
    # ax.matshow(matrix, cmap='plasma') # prev used

    # plot matrix plot with imshow
    im = ax.imshow(matrix, cmap='plasma')
    # setting origin in bottom left corner
    ax.set_ylim(ax.get_ylim()[::-1])

    for i in range(max_val):
        for j in range(max_val):
            c = matrix[j, i]
            ax.text(i, j, str(c), va='center', ha='center')

    return plt.show()


def matrix_generator(n):
    """returns an NxN matrix"""
    initialized_zero_matrix = np.zeros((n, n), dtype=int)
    return initialized_zero_matrix


def target_cells_populater(target_cell_list, mat):
    """populates a matrix with target path trace nodes, including start, end, and intermediary nodes
    and returns target cell populated matrix"""
    # 0 is a free cell, 1 is start, 2 is end, 3 is intermediary node, 4 is path cell
    list_length = len(target_cell_list)

    for idx, cell in enumerate(target_cell_list):
        row = cell[0]
        col = cell[1]
        if idx == 0:
            mat[row][col] = 1
        elif idx == (list_length - 1):
            mat[row][col] = 2
        else:
            mat[row][col] = 3

    return mat


def cell_paths_generator(target_cell_list):
    """returns combined cell paths used to connect all target cells from start to end"""
    list_length = len(target_cell_list)
    cell_paths = np.empty((0,), dtype=[('x', int), ('y', int)])  # store all cells used in path creation

    for idx, cell in enumerate(target_cell_list):
        if idx == (list_length - 1):
            break
        else:
            cell1 = target_cell_list[idx]
            cell2 = target_cell_list[idx + 1]

            cell1_row = cell1[0]  # get cell1 row
            cell1_col = cell1[1]  # get cell1 col

            cell2_row = cell2[0]  # get cell2 row
            cell2_col = cell2[1]  # get cell2 col

            path = bresenham_line(cell1_row, cell1_col, cell2_row, cell2_col)  # intermediate cell path

            if idx == (list_length - 2):  # include complete path if last path is being generated
                cell_paths = np.append(cell_paths, np.array([path], dtype=cell_paths.dtype))
            else:  # removes duplicate cells that occur as repeated appended target cell by ignoring last cell
                cell_paths = np.append(cell_paths, np.array([path[:-1]], dtype=cell_paths.dtype))

    return cell_paths


def cell_paths_overlay(target_cell_list, mat):
    """returns matrix populated with cell paths"""
    cell_paths = cell_paths_generator(target_cell_list)

    for cell in cell_paths:
        row = cell[0]
        col = cell[1]
        mat[row][col] = 4

    return mat


def get_path_directions(target_cell_list):
    """returns the cardinal/intercardinal directions used to navigate the cells path"""
    path_cells = cell_paths_generator(target_cell_list)
    from Navigation_For_Matrix import navigation_directions  # local import to get nav func
    directions = navigation_directions(path_cells)

    return directions


def get_visuals(target_cell_list, n):
    """returns matrix plot of size NxN with target cells and cell paths based on passed target cell list"""
    mat = matrix_generator(n)  # create a template matrix to be used for
    visualizer(target_cells_populater(target_cell_list, mat), n)  # mat plot of target cells
    visualizer(cell_paths_overlay(cell_paths_generator(target_cell_list), mat), n)  # mat plot of all target cell paths

    return 0


def get_visuals_and_directions(target_cell_list, n):
    """get mat plots and print cell paths and directions"""
    # show the cells used for path
    cell_path = cell_paths_generator(target_cell_list)
    print('num of cells for path: ', len(cell_path), '\n')
    print(cell_path, '\n')

    # show the directions being used to traverse path
    directions = get_path_directions(target_cell_list)
    print('num of directions: ', len(directions), '\n')
    print(directions, '\n')

    # show plots
    get_visuals(target_cell_list, n)

    return 0


# MAT SIZE
N_SIZE = 30

# test array of targets cells
test_cells_arr = np.array([(2, 0), (25, 5), (25, 10), (7, 23), (19, 29)], dtype=[('x', int), ('y', int)])

# cell paths generator
# print(cell_paths_generator(cells_arr))
# print(len(cell_paths_generator(cells_arr)))

# get figures
get_visuals_and_directions(test_cells_arr, N_SIZE)


###### INITIAL PARTIAL TESTING STARTS HERE #######
# # making a matrix
# MAT_WIDTH = 30
# MAT_HEIGHT = 30
# initialized_zero_matrix = np.zeros((MAT_WIDTH, MAT_HEIGHT), dtype=int)
# # Node Coordinates (Nodes will be non zero values from 1 to n)
# start_node_x = 2
# start_node_y = 0
# end_node_x = MAT_WIDTH - 1 - 10
# end_node_y = MAT_HEIGHT - 1
#
# # will for loop for node placement, for now start and end are 1 and 2, intermediary nodes are 3, path cells are 4
# initialized_zero_matrix[start_node_x][start_node_y] = 1
# initialized_zero_matrix[end_node_x][end_node_y] = 2
#
# # bresenham line test
# path_cells_arr = bresenham_line(start_node_x, start_node_y, end_node_x, end_node_y)
# print(path_cells_arr)
#
# # nodes
# # active_node_list = [(start_node_x, start_node_y), (end_node_x, end_node_y)] # convert to numpy list
# # MAKE NODE LIST OF NUMPY TYPE IN ORDER TO USE INHERENT PYTHON SYNTAX
# active_node_list = np.array([(start_node_x, start_node_y), (end_node_x, end_node_y)], dtype=[('x', int), ('y', int)])
# print(active_node_list)
#
# # populating matrix with line path cells while avoiding start and end nodes
# for cells in path_cells_arr:
#     if cells not in active_node_list:
#         initialized_zero_matrix[cells[0]][cells[1]] = 4
#
# # start_end_cells = np.array([target_cell_list[0], target_cell_list[-1]], dtype=[('x', int), ('y', int)]) # USE FOR FUNC
#
# ## OBSTACLE CREATION
# # for i in range(5):
# #     initialized_zero_matrix[9 + i][16] = 4
#
# # printing map
# # print(initialized_zero_matrix)
# visualizer(initialized_zero_matrix, MAT_WIDTH)
