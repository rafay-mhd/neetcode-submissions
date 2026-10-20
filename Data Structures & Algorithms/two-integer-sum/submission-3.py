class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        for i, n in enumerate(nums):
            for m in range(i+1, len(nums)):
                if (n + nums[m] == target):
                    return [i, m]
