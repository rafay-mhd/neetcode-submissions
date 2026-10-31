class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #initial solution (bad space and time complexity)
        """
        res = []
        inserted = False
        for word in strs:
            inserted = False
            for lst in res:
                if Counter(word) == Counter(lst[0]):
                    lst.append(word)
                    inserted = True
                    break
            if (not inserted):        
                res.append([word])
        return res   
        """
        
        d = defaultdict(list)
        for word in strs:
            arr = [0] * 26
            for c in word:
                arr[ord(c) - ord('a')] += 1
            tup = tuple(arr)
            d[tup].append(word)
        return list(d.values())
            

