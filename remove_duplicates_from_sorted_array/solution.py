class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        c1 = 0
        c2 = 0
        if(len(nums)==0):
            return 0
        k = 1
        while(c2<len(nums)):
            if(nums[c1] == nums[c2]):
                c2 +=1
            else:
                c1 +=1
                nums[c1] = nums[c2]
                c2 +=1
                k+=1
        return k


        