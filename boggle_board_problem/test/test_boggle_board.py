import unittest
from boggle_board_problem.boggle_board import get_adjacent, solve_boggle


class TestBoggleBoard(unittest.TestCase):
    def test_get_adjacent_side(self):
        adjaceny = get_adjacent((0, 1), [], (3, 3))
        self.assertTrue((0, 0) in adjaceny)
        self.assertTrue((1, 0) in adjaceny)
        self.assertTrue((1, 1) in adjaceny)
        self.assertTrue((1, 2) in adjaceny)
        self.assertTrue((0, 2) in adjaceny)

    def test_get_adjacent_middle(self):
        adjaceny = get_adjacent((1, 1), [], (3, 3))
        self.assertTrue((0, 0) in adjaceny)
        self.assertTrue((0, 1) in adjaceny)
        self.assertTrue((0, 2) in adjaceny)
        self.assertTrue((1, 0) in adjaceny)
        self.assertTrue((1, 2) in adjaceny)
        self.assertTrue((2, 0) in adjaceny)
        self.assertTrue((2, 1) in adjaceny)
        self.assertTrue((2, 2) in adjaceny)

    def test_get_adjacent_corner(self):
        adjaceny = get_adjacent((0, 0), [], (3, 3))
        self.assertTrue((0, 1) in adjaceny)
        self.assertTrue((1, 1) in adjaceny)
        self.assertTrue((1, 0) in adjaceny)

    def test_get_adjacent_used(self):
        adjaceny = get_adjacent((0, 0), [(1, 0)], (3, 3))
        self.assertTrue((0, 1) in adjaceny)
        self.assertTrue((1, 1) in adjaceny)
        self.assertTrue((1, 0) not in adjaceny)
