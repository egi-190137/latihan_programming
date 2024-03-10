class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        dict_num = {}
        for num in arr:
            dict_num[num] = dict_num.get(num, 0) + 1

        count_values = list(dict_num.values())
        count_removed = 0
        for i in range(len(count_values) - 1):
            min_idx = 0
            for j in range(i + 1, len(count_values)):
                if count_values[min_idx] > count_values[j]:
                    min_idx = j

            count_values[i], count_values[min_idx] = (
                count_values[min_idx],
                count_values[i],
            )
            if count_values[i] > k:
                break
            else:
                k -= count_values[i]
                count_removed += 1
        # while k > 0:
        #     unique_nums = list(dict_num.keys())
        #     removed_num = unique_nums[0]
        #     for i in range(1, len(unique_nums)):
        #         if dict_num[removed_num] > dict_num[unique_nums[i]]:
        #             removed_num = unique_nums[i]
        #
        #         if dict_num[removed_num] == 1:
        #             break
        #
        #     if dict_num[removed_num] == 1:
        #         del dict_num[removed_num]
        #     else:
        #         dict_num[removed_num] -= 1

        return len(count_values) - count_removed
