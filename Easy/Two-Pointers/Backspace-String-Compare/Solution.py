class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        a=list(s)
        b=list(t)
        i=0
        while i<len(a):
            if a[i]=='#':
                a.pop(i)
                if i>0:
                    a.pop(i-1)
                    i-=1
            else:
                i+=1
        j=0
        while j<len(b):
            if b[j]=='#':
                b.pop(j)
                if j>0:
                    b.pop(j-1)
                    j-=1
            else:
                j+=1
        if a==b:
            return True
        else:
            return False
                        
