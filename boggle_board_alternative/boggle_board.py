import math

board = [
    list('quit'),
    list('ubwe'),
    list('ievd'),
    list('zand'),
]

words = ["ed", "quit", "blah", "and", "we"]


def norm(coordinate_1, coordinate_2):
    x1, y1 = coordinate_1
    x2, y2 = coordinate_2
    return math.sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2))


def find_character(character, board):
    coordinates = []
    num_rows = len(board)
    num_colums = len(board[0])
    for i in range(num_rows):
        for j in range(num_colums):
            if board[i][j] == character:
                coordinates.append((i, j))
    return coordinates


def solve_boggle(words, board):
    global_used = []
    found = []
    for word in words:
        used = []
        for coordinate in find_character(word[0], board):
            if coordinate not in global_used and find_word("", word, coordinate, used):
                global_used.extend(used)
                found.append(word)
    return found


def find_word(sub_string, word, coordinate, used):
    row, column = coordinate
    character = board[row][column]
    if sub_string + character == word:
        if coordinate not in used:
            used.append(coordinate)
        return True
    if sub_string not in word:
        return False
    if coordinate not in used:
        used.append(coordinate)
    acc = False
    for new_coordinate in get_adjacent(coordinate, used, (4, 4)):
        acc = acc or find_word(sub_string + character, word, new_coordinate, used)
    return acc


def is_neighbor(to_add, coordinate):
    return 1 <= norm(to_add, coordinate) <= math.sqrt(
        2)


def is_not_processed(to_add, coordinate, adjacenies, used):
    return to_add != coordinate and to_add not in adjacenies and to_add not in used


def is_within_dimension(dimension, to_add):
    num_rows, num_columns = dimension
    row, column = to_add
    return 0 <= row < num_rows and 0 <= column < num_columns


def get_adjacent(coordinate, used, dimension):
    adjacenies = []
    row, column = coordinate
    operations = [(+1, +1), (+1, -1), (-1, +1), (-1, -1)]
    for i in range(2):
        for j in range(2):
            for x, y in operations:
                to_add = (row + x * i, column + y * j)
                if is_neighbor(to_add, coordinate) and is_not_processed(to_add, coordinate, adjacenies,
                                                                        used) and is_within_dimension(dimension,
                                                                                                      to_add):
                    adjacenies.append(to_add)

    return adjacenies


print(solve_boggle(words, board))
