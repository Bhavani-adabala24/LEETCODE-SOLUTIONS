class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
        divisors=sorted(divisors)
        l=[]
        for x in divisors:
            c=0
            for y in nums:
                if y%x==0:
                    c+=1
            l.append(c)
        return divisors[l.index(max(l))]
            