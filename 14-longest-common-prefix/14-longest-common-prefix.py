class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""
        n = len(strs)
        # sort array according to string len
        self.sort_arr(strs)
        
        temp = ""
        
        # length of shortest string in array
        for i in range(len(strs[0])):
            
            temp += strs[0][i]
            # print(f"{temp=}")
            
            # for each word in strs, check prefix
            for j in range(1, n):
                # print(strs[j][:i+1])
                
                # break once not equal
                if strs[j][:i+1] != temp:
                    return ans
            ans = temp
        return ans
        
    def sort_arr(self, arr):
        for i in range(1, len(arr)):
            temp = arr[i]
            j = i-1
            while j >= 0 and len(temp) < len(arr[j]):
                arr[j+1] = arr[j]
                j -= 1
                
            arr[j+1] = temp