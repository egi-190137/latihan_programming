import unittest


class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        for token in tokens:
            if token not in ('+', '-', '*', '/'):
                stack.append(int(token))
                continue

            operand2 = stack.pop()
            operand1 = stack.pop()

            if token == '+':
                stack.append(operand1 + operand2)
            elif token == '-':
                stack.append(operand1 - operand2)
            elif token == '*':
                stack.append(operand1 * operand2)
            else:
                stack.append(int(operand1 / operand2))
        return stack[0]


class MyTest(unittest.main):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.evalRPN(tokens = ["2","1","+","3","*"]), 9)

    def test_example_2(self):
        self.assertEqual(self.solution.evalRPN(tokens = ["4","13","5","/","+"]), 6)

    def test_example_3(self):
        self.assertEqual(self.solution.evalRPN(tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]), 22)

if __name__ == '__main__':
    unittest.main()








