class Solution:
    def countDominantElements(self, nums: list[int]) -> int:
        c=0
        if len(nums)>1:
            if nums[0]>=nums[1]:
                c+=1
            if nums[-2]<=nums[-1]:
                c+=1
            for i in range(1,len(nums)-1):
                if ((nums[i-1]+nums[i+1])/2)<=nums[i]:
                    c+=1
            return c
        return 1
