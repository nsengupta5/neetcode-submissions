class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for idx, s in enumerate(strs):
            sorted_word = ''.join(sorted(s))
            if sorted_word in anagrams:
                anagrams[sorted_word].append(idx)
            else:
                anagrams[sorted_word] = [idx]

        result = []
        for anagram in anagrams.values():
            words = []
            for idx, value in enumerate(anagram):
               words.append(strs[value])
            result.append(words)
        
        return result