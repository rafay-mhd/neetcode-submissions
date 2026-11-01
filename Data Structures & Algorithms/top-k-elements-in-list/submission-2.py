class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for n in nums:
            counts[n] = counts.get(n, 0) + 1
        
        desc = {m: v for m, v in sorted(counts.items(), key=lambda item: item[1], reverse = True)}

        res = []
        first_k_keys = list(islice(desc, k))
        return first_k_keys

