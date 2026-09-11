from itertools import permutations
class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        s=list(permutations(digits,3))        
        ans=[]
        for i in range(len(s)):
            if s[i][0]==0:
                continue
            if s[i][-1]%2==0:
                ans.append(s[i])
        ans=list(set(ans))
        return len(ans)