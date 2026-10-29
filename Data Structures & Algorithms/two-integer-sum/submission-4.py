class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        for i in range (len(nums)):
            for j in range (i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        """

        prevMap = {}

        for i, word in enumerate(nums):
            diff = target - word
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[word] = i



        
