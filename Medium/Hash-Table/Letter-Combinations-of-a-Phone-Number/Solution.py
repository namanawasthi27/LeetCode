class Solution:
  def letterCombinations(self, digits: str) -> list[str]:
    if not digits:
        return []
    else:
        d={
           "2":"abc",
           "3":"def",
           "4":"ghi",
           "5":"jkl",
           "6":"mno",
           "7":"pqrs",
           "8":"tuv",
           "9":"wxyz"}
        ans=[""]
        for digit in digits:
            tempp=[]
            for s in ans:
                
                for ch in d[digit]:
                    tempp.append(s+ch)
            ans=tempp
        return ans

