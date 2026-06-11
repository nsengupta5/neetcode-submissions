class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_map = {}
        for idx, num in enumerate(nums):
            diff = target - num
            if diff in index_map:
                if index_map[diff] != idx:
                    return [index_map[diff], idx]
            index_map[num] = idx
        return []