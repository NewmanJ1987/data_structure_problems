import unittest
from boggle_board_problem.boggle_board_problem import search_boggle, all_characters_indexed, check_adjaceny


class TestBoggleBoardProblem(unittest.TestCase):
    def test_boggle_board_found(self):
        words = ["quiz", "geeks", "for", "go"]
        board = [['g', 'i', 'z'], ['u', 'e', 'k'], ['q', 's', 'e']]
        found = search_boggle(words, board)
        self.assertEqual(['quiz', 'geeks'], found)

    def test_boggle_board_not_found(self):
        words = ["blah"]
        board = [['g', 'i', 'z'], ['u', 'e', 'k'], ['q', 's', 'e']]
        found = search_boggle(words, board)
        self.assertEqual([], found)

    def test_all_characters_indexed(self):
        word = "quiz"
        board = [['g', 'i', 'z'], ['u', 'e', 'k'], [''
                                                    'q', 's', 'e']]
        index_char_map = all_characters_indexed(word, board)
        self.assertEqual(index_char_map.get('q'), (2, 0))
        self.assertEqual(index_char_map.get('u'), (1, 0))
        self.assertEqual(index_char_map.get('i'), (0, 1))
        self.assertEqual(index_char_map.get('z'), (0, 2))

    def test_check_adjaceny_adjacent(self):
        character_index = {
            "q": (2, 0),
            "u": (1, 0),
            "i": (0, 1),
            'z': (0, 2)

        }
        self.assertTrue(check_adjaceny([], "quiz", character_index))

    def test_check_adjaceny_not_adjacent(self):
        character_index = {
            "q": (2, 0),
            "u": (1, 0),
            "i": (0, 1),
            'z': (0, 3)

        }
        self.assertFalse(check_adjaceny([], "quiz", character_index))

    def test_check_adjaceny_double_letter_in_end(self):
        character_index = {
            "q": (2, 0),
            "u": (1, 0),
            "z": (0, 1),

        }
        self.assertFalse(check_adjaceny([], "quzz", character_index))

    def test_check_adjaceny_double_letter_in_middle(self):
        character_index = {
            "q": (2, 0),
            "u": (1, 0),
            "z": (0, 1),

        }
        self.assertFalse(check_adjaceny([], "quuz", character_index))
