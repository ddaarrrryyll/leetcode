class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        left = nums1[:m]
        # traverse nums1 and nums2 from the back (biggest)
        while m > 0 and n > 0:
            if nums2[n-1] > left[m-1]:
                nums1[m+n-1] = nums2[n-1]
                n -= 1
                
            else:
                nums1[m+n-1] = left[m-1]
                nums1[m-1] = nums2[n-1]
                m -= 1
        # if we move all the m to the back of nums1, the remaining positions in front should be given to remaining numbers in nums2
        if n > 0:
            nums1[:n] = nums2[:n]
        
        