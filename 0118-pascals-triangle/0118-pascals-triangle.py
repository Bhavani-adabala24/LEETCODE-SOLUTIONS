class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        l=[]
        for i in range(numRows):
            l.append((i+1)*[1])
        for j in range(2,len(l)):
            for k in range(len(l[j-1])-1):
                l[j][k+1]=l[j-1][k]+l[j-1][k+1]
        return l