class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for idx, num in enumerate(nums):
            target_pair = target - num
            for i in range(idx + 1, len(nums)):
                if nums[i] == target_pair:
                    return [idx, i]