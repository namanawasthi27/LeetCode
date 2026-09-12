class Solution:
    def removeStars(self, s: str) -> str:
        sta=[]
        for i in range(len(s)):
            if s[i]=="*":
                sta.pop()
            else:
                sta.append(s[i])
        return "".join(sta)