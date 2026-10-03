class Solution:
    def maximumSum(self, arr: list[int]) -> int:
        onedelete=float('-inf')
        nodelete=arr[0]
        ans=arr[0]
        for i in range(1,len(arr)):
            onedelete=max(onedelete+arr[i],nodelete)
            nodelete=max(arr[i],nodelete+arr[i])
            ans=max(ans,onedelete,nodelete)
        return ans        