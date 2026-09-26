class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        l=[]
        k=[]
        for i in s:
            if i=='#':
                if l:
                    l.pop()
            else:
                l.append(i)
        for i in t:
            if i=='#':
                if k:
                    k.pop()
            else:
                k.append(i)
        return l==k
                