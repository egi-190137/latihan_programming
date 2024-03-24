class Solution:
    def pivotInteger(self, n: int) -> int:
        sum1 = sum([x for x in range(1, n + 1)])
        sum2 = n
        res = n
        while sum1 >= sum2:
            if sum1 == sum2:
                return res
            sum1 -= res
            res -= 1
            sum2 += res
        return -1
