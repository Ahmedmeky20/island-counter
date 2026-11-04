import unittest

from island_counter import count_islands


class TestCountIslands(unittest.TestCase):
    def test_example_from_lecture(self):
        grid = [
            [1, 1, 0, 0, 0],
            [1, 1, 0, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 0, 1, 1],
        ]
        self.assertEqual(count_islands(grid), 3)

    def test_empty_grid(self):
        self.assertEqual(count_islands([]), 0)

    def test_all_water(self):
        self.assertEqual(count_islands([[0, 0], [0, 0]]), 0)

    def test_all_land_is_one_island(self):
        self.assertEqual(count_islands([[1, 1], [1, 1]]), 1)

    def test_diagonal_cells_are_separate(self):
        self.assertEqual(count_islands([[1, 0], [0, 1]]), 2)

    def test_single_cell_land(self):
        self.assertEqual(count_islands([[1]]), 1)

    def test_single_cell_water(self):
        self.assertEqual(count_islands([[0]]), 0)

    def test_non_rectangular_grid_raises(self):
        with self.assertRaises(ValueError):
            count_islands([[1, 0], [1]])

    def test_invalid_cell_raises(self):
        with self.assertRaises(ValueError):
            count_islands([[1, 2]])


if __name__ == "__main__":
    unittest.main()
