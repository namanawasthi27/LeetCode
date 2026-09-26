class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        d=dict(knowledge)
        i=0
        ans=""
        word=""
        while i<len(s):
            if s[i]=="(":
                j=i+1
                while s[j]!=")":
                    j+=1
                word=s[i+1:j]
                if word in d:
                    ans+=d[word]
                else:
                    ans+="?"
                i=j+1
            else:
                ans+=s[i]
                i+=1
        return ans