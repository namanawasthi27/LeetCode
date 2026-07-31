class Solution:
    def kthCharacter(self, k: int) -> str:
        word='a'
        while len(word)<k:
            temp=""
            for ch in word:
                if ch=='z':
                    temp+='a'
                else:
                    temp+=chr(ord(ch)+1)
            word+=temp
        return word[k-1]