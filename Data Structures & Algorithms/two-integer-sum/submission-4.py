class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tracker = {}
        for idx, num in enumerate(nums):
            target_pair = target - num
            if target_pair in tracker.keys():
                return [tracker[target_pair], idx]
            tracker[num] = idx
            
