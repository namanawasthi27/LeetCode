class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        j=[]
        if len(nums2)>len(nums1):
            for i in range(0,len(nums1)):
                if nums1[i] in nums2:
                    j.append(nums1[i])
                    nums2.remove(nums1[i])
        else:
            for i in range(0,len(nums2)):
                if nums2[i] in nums1:
                    j.append(nums2[i])
                    nums1.remove(nums2[i])
        return j