class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s)>k:
            s1=""
            for i in range(0,len(s),k):
                st=s[i:i+k]
                sum=0
                for i in st:
                    sum+=int(i)
                s1+=str(sum)
            s=s1
        return s
            