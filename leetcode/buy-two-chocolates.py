import unittest


class Solution:
    def buyChoco(self, prices: list[int], money: int) -> int:
        lowest_price = sorted(prices[:2])
        for i in range(2, len(prices)):
            if prices[i] < lowest_price[0]:
                lowest_price[1] = lowest_price[0]
                lowest_price[0] = prices[i]
            elif prices[i] < lowest_price[1]:
                lowest_price[1] = prices[i]

        return money if sum(lowest_price) > money else money - sum(lowest_price)

 
class MyTest(unittest.main):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.buyChoco([1,2,2]), 0)

    def test_example_2(self):
        self.assertEqual(self.solution.buyChoco([3,2,3]), 3)

if __name__ == '__main__':
    unittest.main()