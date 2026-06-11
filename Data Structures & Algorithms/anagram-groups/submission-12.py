class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        tracker = {}
        for s in strs:
            counter = [0] * 26
            for c in s:
                position = ord(c) - 97
                counter[position] = counter[position] + 1
            
            counter_str = ",".join([str(c) for c in counter])
            if counter_str in tracker:
                tracker[counter_str].append(s)
            else:
                tracker[counter_str] = [s]
            print(tracker)

        return list(tracker.values())