class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tracker = {}
        for idx, n in enumerate(nums):
            difference = target - n
            if n in tracker:
                return [tracker[n], idx]
        
            tracker[difference] = idx

        return []