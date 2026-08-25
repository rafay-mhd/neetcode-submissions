class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        #initial solution:
        """
        map1 = {}
        for x in s:
            if x in map1:
                map1[x] += 1
            else:
                map1[x] = 1

        map2 = {}
        for y in t:
            if y in map2:
                map2[y] += 1
            else:
                map2[y] = 1

        # map1 = dict(sorted(map1.items(), key = lambda item:item[0]))
        # map2 = dict(sorted(map2.items(), key = lambda item:item[0]))

        return map1 == map2
        """

        #neetcode style:
        """
        if len(s) != len(t):
            return False
        
        map1, map2 = {}, {}

        #building the maps
        for i in range(len(s)):
            map1[s[i]] = map1.get(s[i], 0) + 1
            map2[t[i]] = map2.get(t[i], 0) + 1

        for c in map1:
            if map1[c] != map2.get(c, 0):
                return False
        return True
        """


        #shortcut:
        #return Counter(s) == Counter(t)
        # but still no O(1) space complexity

        #other solution
        return sorted(s) == sorted(t)

        #for O(1) space comple

        

    










