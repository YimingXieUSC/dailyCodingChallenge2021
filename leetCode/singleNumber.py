class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        index = 0
        while(len(nums) != 0):
            if(len(nums) == 1):
                return nums[0]
            currentnum = nums[0]
            nums.remove(currentnum)
            if(currentnum in nums):
                nums.remove(currentnum)
                continue
            else:
                return currentnum
