class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        i, j = 0, 0
        minheap = [(nums1[i] + nums2[j], i, j)]
        out = []
        visited = set()
        
        # adding all the possible combinations to minheap and popping them out max k times
        while minheap and len(out) < k:
            _, i, j = heappop(minheap)
            out.append([nums1[i], nums2[j]])
            
            if i+1 < len(nums1):
                temp1 = (nums1[i+1] + nums2[j], i+1, j)
            else:
                temp1 = None
                
            if temp1 and temp1 not in visited:
                visited.add(temp1)
                heappush(minheap, temp1)
                
            if j+1 < len(nums2):
                temp2 = (nums1[i] + nums2[j+1], i, j+1)
            else:
                temp2 = None
                
            if temp2 and temp2 not in visited:
                visited.add(temp2)
                heappush(minheap, temp2)
                        
        return out
                