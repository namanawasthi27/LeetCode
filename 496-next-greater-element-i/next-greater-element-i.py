class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        stack=[]
        d={}
        for i in range(len(nums2)):
            while stack and nums2[i]>=stack[-1]:
                d[stack.pop()]=nums2[i]
            stack.append(nums2[i])
        for i in range(len(nums1)):
            if nums1[i] in d:
                nums1[i]=d[nums1[i]]
            else:
                nums1[i]=-1
        return nums1

