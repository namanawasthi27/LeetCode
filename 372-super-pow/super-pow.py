class Solution:
    def superPow(self, a: int, b: list[int]) -> int:
        result=1
        a=a%1337
        for i in range(0,len(b)):
            result=(result**10*a**b[i])%1337
        return result