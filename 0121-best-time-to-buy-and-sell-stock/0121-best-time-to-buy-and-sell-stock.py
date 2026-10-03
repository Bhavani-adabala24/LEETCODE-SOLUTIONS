class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prof=0
        maxi=prices[-1]       
        for i in range(len(prices)-2,-1,-1):
            if prices[i]<maxi:
                diff=maxi-prices[i]
                if diff>prof:
                    prof=diff
            else:
                maxi=prices[i]
        return prof