from collections import Counter
import operator

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        sorted_counts = {k: v for k, v in sorted(counts.items(), key=operator.itemgetter(1), reverse=True)}
        return list(sorted_counts.keys())[:k]