class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        odd=[]
        for x in nums1:
            if x%2!=0:
                odd.append(x)
        if len(odd)==0:
            return True
        smallest=min(odd)
        for x in nums1:
            if x%2==0:
                if x<smallest:
                    return False
        return True