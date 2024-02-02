class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        numbers = "123456789"
        length = len(str(low))
        start_idx = 0
        res = []
        while True:
            if start_idx + length > len(numbers):
                start_idx = 0
                length += 1
            if length > len(numbers):
                break
            curr = int(numbers[start_idx:start_idx+length]) 
            if curr < low:
                start_idx += 1
                continue
            if curr > high:
                break
            res.append(curr)
            start_idx += 1
        return res
