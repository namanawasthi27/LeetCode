class Solution:
    def findWords(self, words: list[str]) -> list[str]:
        q="QWERTYUIOPqwertyuiop"
        a="asdfghjklASDFGHJKL"
        z="zxcvbnmZXCVBNM"
        l=[]
        for i in range(len(words)):
            if words[i][0] in q:
                row=q
            elif words[i][0] in a:
                row=a
            else:
                row=z
            count=0
            for k in range(len(words[i])):
                    if words[i][k] in row:
                        count+=1
        
            if count==len(words[i]):
                l.append(words[i])
        return l
