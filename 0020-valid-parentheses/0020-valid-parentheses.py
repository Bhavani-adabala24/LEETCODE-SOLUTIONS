class Solution:
    def isValid(self, s: str) -> bool:
        l=[]
        a="([{"
        for x in s:
            if x in a:
                l.append(x)
            elif (l and(l[-1]=="("and x==")")):
                l.pop() 
            elif (l and l[-1]=="["and x=="]"):
                l.pop() 
            elif (l and l[-1]=="{"and x=="}"):
                l.pop()
            else:
                l.append(x)
        if len(l)==0:
            return True
        else:
            return False