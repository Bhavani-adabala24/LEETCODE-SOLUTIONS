class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        d={}
        for x in nums:
            if x in d:
                return x
            else:
                d[x]=1