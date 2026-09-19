class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        l=[]
        for i in range(len(nums1)):
            if nums1[i] in nums2:
                n=nums2.index(nums1[i])
            for j in range(n+1,len(nums2)):
                if nums2[j]>nums1[i]:
                    l.append(nums2[j])
                    break
            else:
                l.append(-1)
        return l