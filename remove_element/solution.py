class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        c1 = 0
        c2 = len(nums)-1
        k = 0
        while(c1<=c2):
            if((nums[c1]==val)):
                nums[c1] = nums[c2]
                nums[c2] = val
                c2-=1
            else:
                c1+=1
                k+=1
        return k