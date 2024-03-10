class Solution:
    def bagOfTokensScore(self, tokens: list[int], power: int) -> int:
        if len(tokens) == 1:
            return 1 if tokens[0] <= power else 0

        tokens.sort()
        idx_face_up = 0
        idx_face_down = len(tokens) - 1
        score = 0
        while idx_face_up <= idx_face_down:
            if power >= tokens[idx_face_up]:
                power -= tokens[idx_face_up]
                idx_face_up += 1
                score += 1
            elif idx_face_up != idx_face_down and score > 0:
                power += tokens[idx_face_down]
                idx_face_down -= 1
                score -= 1
            else:
                break
        return score


solution = Solution()
print(solution.bagOfTokensScore(tokens=[100, 200, 300, 400], power=200))
