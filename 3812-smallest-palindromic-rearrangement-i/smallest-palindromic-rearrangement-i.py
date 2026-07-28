from collections import Counter
class Solution:
    def smallestPalindrome(self, s: str) -> str:
        freq=Counter(s)
        left=""
        middle=""
        for ch in sorted(freq.keys()):
            left+=ch*(freq[ch]//2)
            if freq[ch]%2==1:
                middle=ch
        right=left[::-1]
        return left+middle+right
        