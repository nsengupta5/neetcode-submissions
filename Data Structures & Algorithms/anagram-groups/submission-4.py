class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        tracker = {}
        for s in strs:
            sorted_s = str(sorted(s))
            if sorted_s in tracker:
                tracker[sorted_s].append(s)
            else:
                tracker[sorted_s] = [s]

        return list(tracker.values())