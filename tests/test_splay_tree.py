import unittest
import splay_tree


class MyTestCase(unittest.TestCase):
    def test_first(self):
        input_str = ["add 8 10 \n",
                     "add 4 14 \n",
                     "add 7 15 \n",
                     "set 8 11 \n",
                     "add 3 13 \n",
                     "add 5 16 \n",
                     "search 88 \n",
                     "search 7 \n",
                     "delete 5 \n",
                     "print\n"]
        answer = "0\n" \
                 "1 15\n" \
                 "[4 14]\n" \
                 "[3 13 4] [7 15 4]\n" \
                 "_ _ _ [8 11 7]\n"
        h = splay_tree.Handler(input_str)
        output_str = h.parse()
        self.assertEqual(answer, output_str)


if __name__ == '__main__':
    unittest.main()
