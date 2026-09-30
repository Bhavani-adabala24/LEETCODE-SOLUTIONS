class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        d={}
        l=[]
        for x in nums:
            if x in d:
                d[x]+=1
            else:
                d[x]=1
        for p,q in d.items():
            if q>len(nums)//3:
                l.append(p)
        return l