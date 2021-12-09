class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        # queue of index
        queue = collections.deque([])
        queue.append(start)
        
        while queue:
            idx = queue.popleft()
            # base case
            if arr[idx] == 0:
                return True
            
            # if visited
            if arr[idx] < 0:
                continue
            
            # go right if allowed
            if idx + arr[idx] < len(arr):
                queue.append(idx + arr[idx])
            
            # go left if allowed
            if idx - arr[idx] >= 0:
                queue.append(idx - arr[idx])
            
            # mark as visited
            arr[idx] *= -1
        
        return False