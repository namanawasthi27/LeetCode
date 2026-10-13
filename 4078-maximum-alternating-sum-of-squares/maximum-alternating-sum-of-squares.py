class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        summ=[]
        
        for i in range(0,len(nums)):
            summ.append(nums[i]*nums[i])
        summ.sort()
        mini=0
        maxx=0
        n=len(summ)
        for i in range(0,n//2):
            mini+=summ[i]
        for i in range(n//2,n):
            maxx+=summ[i]
        return maxx-mini