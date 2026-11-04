class Solution:
    def minMergedInteger(self, nums: list[int]) -> int:
        min=int(str(nums[0])+str(nums[1]))
        for i in range(0,len(nums),2):
            mini=int(str(nums[i])+str(nums[i+1]))
            if mini<min:
                min=mini
        return min
