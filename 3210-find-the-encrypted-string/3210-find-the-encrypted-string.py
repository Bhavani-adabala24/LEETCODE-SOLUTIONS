class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        s2=""
        s1=s+s
        k=k%len(s)
        if len(s)<k:
            return s2
        for x in range(len(s)):
            s2+=s1[x+k]
        return s2