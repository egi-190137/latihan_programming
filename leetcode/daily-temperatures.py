import unittest


class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        answers = [0] * len(temperatures)
        warm_temperatures = set()
        for i in range(len(temperatures)):
            if temperatures[i] in warm_temperatures:
                continue
            if warm_temperatures:
                if temperatures[i] > min(warm_temperatures):
                    continue
            if i > 0:
                if temperatures[i] == temperatures[i-1]:
                    answers[i] = answers[i-1] - 1
                    continue
            isFound = False
            for j in range(i + 1, len(temperatures)):
                answers[i] += 1
                if temperatures[i] < temperatures[j]:
                    isFound = True
                    break
            if not isFound:
                answers[i] = 0
                warm_temperatures.add(temperatures[i])

        return answers

class MyTest(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.dailyTemperatures(temperatures = [73,74,75,71,69,72,76,73]), [1,1,4,2,1,1,0,0])

    def test_example_2(self):
        self.assertEqual(self.solution.dailyTemperatures(temperatures = [30,40,50,60]), [1,1,1,0])

    def test_example_3(self):
        self.assertEqual(self.solution.dailyTemperatures(temperatures = [30,60,90]), [1,1,0])


if __name__ == '__main__':
    unittest.main()
