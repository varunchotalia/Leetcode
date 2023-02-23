class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) == 0:
            return None
        hasj = {}
        for x in range(len(nums)):
            if nums[x] not in hasj:
                hasj[nums[x]] = x
            if target - nums[x] in hasj and hasj[target-nums[x]] != x:
                return [hasj[target-nums[x]], x]
    
        
