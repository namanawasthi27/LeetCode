class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        d = {0: -1}
        s = 0

        for i in range(len(nums)):
            s += nums[i]
            r = s % k

            if r in d:
                if i - d[r] >= 2:
                    return True
            else:
                d[r] = i

        return False