from collections import Counter


class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        times = 0
        counts = list(Counter(tasks).values())
        while True:
            counts.sort(reverse=True)
            if counts[0] == 0:
                break
            count_task = 0
            for i in range(len(counts)):
                if counts[i] == 0 or count_task > n:
                    break
                counts[i] -= 1
                count_task += 1

            if counts[0] == 0:
                idle_time = 0
            else:
                idle_time = n - count_task + 1

            if idle_time < 0:
                idle_time = 0

            times += count_task + idle_time
        return times


solution = Solution()
print(
    solution.leastInterval(
        ["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"], 1
    )
)
print(solution.leastInterval(tasks=["A", "C", "A", "B", "D", "B"], n=1))
print(solution.leastInterval(tasks=["A", "A", "A", "B", "B", "B"], n=3))
