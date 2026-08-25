class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # map:
        """
        my_map = {}
        for x in nums:
            if x not in my_map:
                my_map[x] = 1
            else:
                return True
        return False
        """
        # set:
        """
        seen = set()
        for x in nums:
            if x in seen:
                return True
            seen.add(x)
        return False
        """
        # best solution with set:
        return len(set(nums)) != len(nums)
        