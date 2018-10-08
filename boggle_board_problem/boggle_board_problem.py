# Note problem from.
# https://practice.geeksforgeeks.org/problems/word-boggle/0


def search_boggle(words, board):
    found = []
    used = []
    for word in words:
        character_index = all_characters_indexed(word, board)
        if len(character_index.keys()) == len(word) and check_adjaceny(used, word, character_index):
            found.append(word)
    return found


def all_characters_indexed(word, board):
    to_return = {}
    for character in list(word):
        for i in range(len(board)):
            for j in range(len(board[0])):
                if character == board[i][j]:
                    to_return.update({character: (i, j)})
    return to_return


def check_adjaceny(used, word, character_index):
    for index, character in enumerate(word):
        if index < len(word) - 1:
            row_i, column_i = character_index.get(character)
            row_j, column_j = character_index.get(word[index + 1])
            if (row_i, column_i) in used:
                return False
            if abs(row_i - row_j) > 1 or abs(column_i - column_j) > 1:
                return False
        row_i, column_i = character_index.get(character)
        if (row_i, column_i) in used:
            return False
        used.append((row_i, column_i))
    return True
