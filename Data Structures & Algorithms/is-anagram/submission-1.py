class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_map = {}
        t_map = {}

        for c in s:
            if c in s_map:
                s_map[c] += 1
            else:
                s_map[c] = 0

        for c in t:
            if c in t_map:
                t_map[c] += 1
            else:
                t_map[c] = 0

        for c, val in s_map.items():
            if c not in t_map.keys():
                return False
            
            if s_map[c] != t_map[c]:
                return False

        return True