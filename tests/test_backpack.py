import unittest
import Knapsack_problem


class MyTestCase(unittest.TestCase):
    def test_first(self):
        input_str = """165
23 92
31 57
29 49
44 68
53 60
38 43
63 67
85 84
89 87
82 72
"""
        W, weight_and_price_list = Knapsack_problem.handler([x + '\n' for x in input_str.split('\n')])
        ans = Knapsack_problem.get_answer(W, weight_and_price_list)
        sum_weight = sum([tup[0] for tup in weight_and_price_list][x - 1] for x in ans)
        sum_price = sum([tup[1] for tup in weight_and_price_list][x - 1] for x in ans)
        list_of_numbers = [1, 2, 3, 4, 6]
        self.assertEqual(sum_weight, 165)
        self.assertEqual(sum_price, 309)
        self.assertEqual(ans, list_of_numbers)

    def test_second(self):
        input_str = """13
3 1
4 6
5 4
8 7
9 6
"""
        W, weight_and_price_list = Knapsack_problem.handler([x + '\n' for x in input_str.split('\n')])
        ans = Knapsack_problem.get_answer(W, weight_and_price_list)
        sum_weight = sum([tup[0] for tup in weight_and_price_list][x - 1] for x in ans)
        sum_price = sum([tup[1] for tup in weight_and_price_list][x - 1] for x in ans)
        list_of_numbers = [2, 4]
        self.assertEqual(sum_weight, 12)
        self.assertEqual(sum_price, 13)
        self.assertEqual(ans, list_of_numbers)


if __name__ == '__main__':
    unittest.main()
