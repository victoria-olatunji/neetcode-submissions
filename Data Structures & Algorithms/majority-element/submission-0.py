class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums) / 2
        dit = {}
        for x in nums:
            dit[x] = nums.count(x)
        for t in dit:
            if dit[t] > n:
                return t