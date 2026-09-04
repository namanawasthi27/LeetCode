class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack=[]
        for x in num:
            while stack and k>0 and stack[-1]>x:
                stack.pop()
                k-=1
            stack.append(x)
        while k>0:
            stack.pop()
            k-=1

        ans="".join(stack).lstrip("0")
        if ans:
            return ans
        else:
            return "0"