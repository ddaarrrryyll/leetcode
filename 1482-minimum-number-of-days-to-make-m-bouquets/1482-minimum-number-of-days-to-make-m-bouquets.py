class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m * k > len(bloomDay):
            return -1 # not enough flowers
        
        start = 0
        end = max(bloomDay)
        minDays = -1
        
        while start <= end:
            mid = (start + end) // 2
            # if we can section off m bouquets of k flowers, we update the end pointer to see if there is a shorter day
            if self.bouquets(bloomDay, mid,  k) >= m:
                minDays = mid
                end = mid-1
            # move start pointer since we have not enough days
            else:
                start = mid + 1
                
        return minDays
    
    def bouquets(self, bloomDay, mid, k):
        bouquets = 0
        count = 0
        # iterate through bloomDay to section off k flowers 
        for day in bloomDay:
            if day <= mid:
                count += 1
            else: 
                count = 0
            
            if count == k:
                bouquets += 1
                count = 0
                
        return bouquets