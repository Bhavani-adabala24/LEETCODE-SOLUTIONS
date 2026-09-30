class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        l=[]
        for i in range(rowIndex+1):
            l.append((i+1)*[1])
        for j in range(2,len(l)):
            for k in range(len(l[j-1])-1):
                l[j][k+1]=l[j-1][k]+l[j-1][k+1]
        return l[-1]