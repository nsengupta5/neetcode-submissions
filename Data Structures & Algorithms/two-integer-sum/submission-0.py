class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = {}

        for n, val in enumerate(nums):
            difference = target - val
            if val in result:
                return [result[val], n]
            result[difference] = n

        return []