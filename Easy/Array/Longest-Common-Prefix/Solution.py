class Solution:
  def longestCommonPrefix(self, strs: list[str]) -> str:
    if not strs:
        return ""
    pre=strs[0]
    for word in strs[1:]:
        while not word.startswith(pre):
            pre=pre[:-1]
            if not pre:
                return ""
    return pre
