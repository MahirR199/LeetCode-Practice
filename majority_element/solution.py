class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """can use a dictionary and just return the element with highest appearance but it isnt O(1) space"""
        maj_index = 0
        maj = 1
        for i in range(1, len(nums)):
            if(nums[i] == nums[maj_index]):
                maj+=1
            else:
                maj-=1
            if(maj==0):
                maj_index = i
                maj = 1
        return(nums[maj_index])