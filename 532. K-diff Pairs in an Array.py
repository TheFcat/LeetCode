class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        count_dict = {}
        for i in nums:
            count_dict[i] = count_dict.get(i, 0) + 1

        result = 0
        if k == 0:
            for value in count_dict.values():
                if value > 1:
                    result += 1
        else:
            for key in count_dict:
                if key + k in count_dict:
                    result += 1
                if key - k in count_dict:
                    result += 1

            result = result // 2

        return result