class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
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

        map1 = dict(sorted(map1.items(), key = lambda item:item[0]))
        map2 = dict(sorted(map2.items(), key = lambda item:item[0]))

        return map1 == map2