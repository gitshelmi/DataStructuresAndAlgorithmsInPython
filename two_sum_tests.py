import unittest
from two_sum import TwoSum

class TwoSumTests(unittest.TestCase):
    def test_WithProperValues_ShouldReturnCorrectIndices(self):
		# arrange
        input = [2, 7, 11, 15]
        target = 9
        expected_output = [ 0, 1 ]

        # act
        actual_output = TwoSum().two_sum_solver(input, target)

        # assert
        self.assertListEqual(expected_output, actual_output)
       
        
    def test_WithFewInputs_ShouldReturnNone(self):
		# arrange
        input = [2]
        target = 9
        expected_output = None

        # act
        actual_output = TwoSum().two_sum_solver(input, target)

        # assert
        self.assertEqual(expected_output, actual_output),
        
        
    def test_WithNoAnswer_ShouldReturn00(self):
		# arrange
        input = [2,3,4]
        target = 9
        expected_output = [0, 0]

        # act
        actual_output = TwoSum().two_sum_solver(input, target)

        # assert
        self.assertListEqual(expected_output, actual_output)


if __name__ == '__main__':
    unittest.main()

