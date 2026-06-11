class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        tracker = {}
        for s in strs:
            counter = [0] * 26
            for c in s:
                position = ord(c) - 97
                counter[position] += 1
            
            if tuple(counter) in tracker:
                tracker[tuple(counter)].append(s)
            else:
                tracker[tuple(counter)] = [s]
            print(tracker)

        return list(tracker.values())