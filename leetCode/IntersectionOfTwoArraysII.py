class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        common = []
        while(len(nums1) > 0):
            currentnum = nums1[0]
            if(currentnum in nums2):
                common.append(currentnum)
                nums2.remove(currentnum)
                nums1.remove(currentnum)
            else:
                nums1.remove(currentnum)
        return(common)
                
