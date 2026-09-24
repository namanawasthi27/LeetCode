class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            som=0
            for j in range(len(str(nums[i]))):
                som+=int(str(nums[i])[j])
            if som==i:
                return i
                break
        else:
                return -1