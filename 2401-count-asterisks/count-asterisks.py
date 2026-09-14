class Solution:
    def countAsterisks(self, s: str) -> int:
        d=s.split("|")
        count=0
        for i in range(len(d)):
            if i%2==0:
                count+=d[i].count("*")
            else:
                continue
        return count

