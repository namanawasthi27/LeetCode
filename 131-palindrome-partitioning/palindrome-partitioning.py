class Solution:
    def partition(self, s: str) -> list[list[str]]:
        n=len(s)
        ans=[]
        def ispalindrome(x):
            return x == x[::-1]
        def generate(start,path):
            if start==n:
                ans.append(path[:])
                return
            for end in range(start,n):
                part=s[start:end+1]
                if ispalindrome(part):
                    path.append(part)
                    generate(end+1,path)
                    path.pop()
        generate(0,[])
        return ans