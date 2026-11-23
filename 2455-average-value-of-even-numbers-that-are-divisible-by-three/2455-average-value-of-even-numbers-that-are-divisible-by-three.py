class Solution:
    def averageValue(self, nums: list[int]) -> int:
        sum=c=0
        for x in nums:
            if x%6==0:
                sum+=x
                c+=1
        if c:
            return sum//c
        return 0