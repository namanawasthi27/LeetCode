class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        f=[]
        for i in range(1,n+1):
            if i in target:
                f.append("Push")
            else:
                f.append("Push")
                f.append("Pop")
            if i==target[-1]:
                break
        return f

