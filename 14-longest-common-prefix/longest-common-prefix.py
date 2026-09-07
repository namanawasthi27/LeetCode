class Solution:
  def longestCommonPrefix(self, strs: list[str]) -> str:
    if not strs:
        return ""
    s=""
    for i in range(len(strs[0])):
        ch=strs[0][i]
        for x in strs:
            if i>=len(x) or x[i]!=ch:
                return s
        s+=ch
    return s

