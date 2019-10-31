import unittest
import min_heap


class MyTestCase(unittest.TestCase):
    def test_first(self):
        input_str = ["add 8 10 \n",
                     "add 4 14 \n",
                     "add 7 15 \n",
                     "set 8 11 \n",
                     "add 3 13 \n",
                     "add 5 16 \n",
                     "add 10 10 \n",
                     "search 88 \n",
                     "search 7 \n",
                     "delete 4 \n",
                     "extract\n",
                     "print\n"]
        answer = "0\n" \
                 "1 2 15\n" \
                 "3 13\n" \
                 "[5 16]\n" \
                 "[8 11 5] [7 15 5]\n" \
                 "[10 10 8] _ _ _\n"
        h = min_heap.Handler(input_str)
        output_str = h.parse()
        self.assertEqual(answer, output_str)


if __name__ == '__main__':
    unittest.main()
