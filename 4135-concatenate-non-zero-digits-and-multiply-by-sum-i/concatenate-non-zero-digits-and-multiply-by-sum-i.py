class Solution:
    def sumAndMultiply(self, n: int) -> int:
        x=[]
        n=str(n)
        for i in range(len(n)):
            if n[i]!="0":
                x.append(int(n[i]))
        if not x:
            return 0
        summ=sum(x)
        num=int("".join(map(str,x)))
        return num*summ
        