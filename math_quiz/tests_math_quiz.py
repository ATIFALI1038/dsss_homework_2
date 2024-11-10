import unittest
from math_quiz import generate_random_number, generate_random_operator, calculate_answer

class TestMathGame(unittest.TestCase):

    def test_generate_random_number(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = generate_random_number(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_generate_random_operator(self):
        # Test if the function returns one of the valid operators
        valid_operators = ['+', '-', '*']
        for _ in range(1000):  # Test a large number of times
            operator =generate_random_operator()
            self.assertIn(operator, valid_operators)

    def test_calculate_answer(self):
        # Test different cases to ensure the function returns expected results
        test_cases = [
            (5, 2, '+', '5 + 2', 7),  # Correct addition case
            (5, 2, '-', '5 - 2', 3),  # Correct subtraction case
            (5, 2, '*', '5 * 2', 10)  # Correct multiplication case
        ]

        for num1, num2, operator, expected_problem, expected_answer in test_cases:
            problem, answer = calculate_answer(num1, num2, operator)
            self.assertEqual(problem, expected_problem)
            self.assertEqual(answer, expected_answer)

if __name__ == "__main__":
    unittest.main()
