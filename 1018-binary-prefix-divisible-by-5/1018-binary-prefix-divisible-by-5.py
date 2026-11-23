class Solution:
    def prefixesDivBy5(self, nums: list[int]) -> list[bool]:
        num=""
        l=[]
        for x in nums:
            num+=str(x)
        for x in range(len(num)):
            s=num[:x+1]
            b=int(s,2)
            if b%5==0:
                l.append(True)
            else:
                l.append(False)
        return l