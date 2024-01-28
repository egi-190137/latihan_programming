class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        sub_sum = [[0] * COLS for _ in range(ROWS) ]
        
        for r in range(ROWS):
            for c in range(COLS):
                top = 0 if r == 0 else sub_sum[r-1][c] 
                left = 0 if c == 0 else sub_sum[r][c-1]
                top_left = 0 if min(r, c) == 0 else sub_sum[r-1][c-1]
                sub_sum[r][c] = matrix[r][c] + top + left - top_lest


        res = 0
        for r1 in range(ROWS):
            for r2 in range(r1, ROWS):
                count = defaultdict(int)
                count[0] = r-1
                for c in range(COLS):
                    cur_sum = sub_sum[r2][c] - (
                        sub_sum[r1-1][c] if r1 > 0 else 0
                    )
                    diff = cur_sum - target
                    res += count[diff]
                    count[cur_sum] += 1
        return res
