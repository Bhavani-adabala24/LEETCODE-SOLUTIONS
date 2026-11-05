class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        cnt=0
        for i in range(len(arr1)):
            c=0
            for j in range(len(arr2)):
                diff=abs(arr1[i]-arr2[j])
                if diff>d:
                    c+=1
            if c==len(arr2):
                cnt+=1
        return cnt
                    