class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #keep track of the lowest and highest maybe with pntrs?
        i = 0
        j = 0
        maxProfit = 0
        minPrice = prices[0]
        for i in range(1,len(prices)):
            if(prices[i]<minPrice):
                minPrice = prices[i]
            else:
                if(prices[i]-minPrice>maxProfit):
                    maxProfit = prices[i]-minPrice
        return maxProfit