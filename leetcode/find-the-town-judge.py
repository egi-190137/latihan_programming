class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1:
            return 1
        if not trust:
            return -1

        people = dict()
        for i in range(len(trust)):
            people[trust[i][0]] = people.get(trust[i][0], []) + [trust[i][1]]

        for i in range(1, n + 1):
            if i in people.keys():
                continue

            is_trusted_by_everybody = True
            for j in range(1, n + 1):
                if i == j:
                    continue

                if j not in people.keys():
                    is_trusted_by_everybody = False
                    break

                if i not in people[j]:
                    is_trusted_by_everybody = False
                    break

            if is_trusted_by_everybody:
                return i
        return -1


solution = Solution()
print(solution.findJudge(n=2, trust=[]))
