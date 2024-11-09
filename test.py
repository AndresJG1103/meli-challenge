import numpy as np
from lambda_function.lambda_function import dna_to_matrix, is_square_matrix, search_mutant
import unittest

MUTANT_DNA = ["ATGCGA", "CAGTGC", "TTATGT", "AGAAGG", "CCCCTA", "TCACTG"]
MUTANT_DNA_MATRIX = np.array([
        ['A', 'T', 'G', 'C', 'G', 'A'],
        ['C', 'A', 'G', 'T', 'G', 'C'],
        ['T', 'T', 'A', 'T', 'G', 'T'],
        ['A', 'G', 'A', 'A', 'G', 'G'],
        ['C', 'C', 'C', 'C', 'T', 'A'],
        ['T', 'C', 'A', 'C', 'T', 'G'],
    ])

class TestCase(unittest.TestCase):
    def test_dna_to_matrix(self):
        np.testing.assert_array_equal(
            dna_to_matrix(
                MUTANT_DNA,
            ),
            MUTANT_DNA_MATRIX
        )
    
    def test_is_square_matrix(self):
        self.assertTrue(is_square_matrix(MUTANT_DNA_MATRIX))

    def test_search_mutant(self):
        self.assertTrue(search_mutant(MUTANT_DNA_MATRIX))


if __name__ == '__main__':
    unittest.main()