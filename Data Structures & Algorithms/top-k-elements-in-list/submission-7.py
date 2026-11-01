class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #possible solution, time: O(n + m log m), space O(m)
        """
        counts = {}
        for n in nums:
            counts[n] = counts.get(n, 0) + 1
        
        desc = {m: v for m, 
        v in sorted(counts.items(), key=lambda item: item[1], reverse = True)}

        first_k_keys = list(islice(desc, k))
        return first_k_keys
      

        # good solution, time: O(n), space O(n)
        count = {}
        freq = [[] for i in range (len(nums) + 1)]

        for n in nums:
            count[n] = count.get(n, 0) + 1
        
        for n, c in count.items():
            freq[c].append(n)
        
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res

  """   
        counts = {}

        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        
        freq = [[] for i in range(len(nums) + 1)]

        for n, c in counts.items():
            freq[c].append(n)
        
        res = []
        for i in range(len(nums), 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res







    






    


