from math import prod
class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        while True:
            arr=list(map(int,str(n)))
            if prod(arr)%t==0:
                return n
            n+=1