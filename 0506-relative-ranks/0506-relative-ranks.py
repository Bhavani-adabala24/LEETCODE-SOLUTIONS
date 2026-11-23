class Solution:
    def findRelativeRanks(self, score: list[int]) -> list[str]:
        s=sorted(score)
        d={}
        l=[]
        for x in range(len(score)-3):
            d[s[x]]=str(len(score)-x)
        if len(score)>=1:
            d[s[-1]]="Gold Medal"
        if len(score)>=2: 
            d[s[-2]]="Silver Medal"
        if len(score)>=3:
            d[s[-3]]="Bronze Medal"
        for x in score:
            l.append(d[x])
        return l
