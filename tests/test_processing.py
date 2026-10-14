import unittest

from processing import find_valid_columns, is_valid_column


class ProcessingTests(unittest.TestCase):
    def test_column_all_multiples_of_5_or_7(self):
        self.assertTrue(is_valid_column([5, 7, 35, 14]))

    def test_column_with_invalid_element(self):
        self.assertFalse(is_valid_column([5, 14, 11]))

    def test_find_valid_columns(self):
        matrix = [
            [5, 10, 11],
            [7, 14, 21],
            [35, 20, 28],
        ]
        self.assertEqual(find_valid_columns(matrix), [1, 2])

    def test_no_valid_columns(self):
        matrix = [
            [3, 11],
            [8, 13],
        ]
        self.assertEqual(find_valid_columns(matrix), [])

    def test_single_element_matrix(self):
        self.assertEqual(find_valid_columns([[7]]), [1])


if __name__ == "__main__":
    unittest.main()
