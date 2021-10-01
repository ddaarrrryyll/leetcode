class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        # first column first row needs to be 0
        DP = [[0 for _ in range(len(text2)+1)] for _ in range(len(text1)+1)]
        
        for i in range(len(text1)):
            for j in range(len(text2)):
                # if same char, add 1 to the ans to prev subproblem (DP[i][j])
                if text1[i] == text2[j]:
                    DP[i+1][j+1] = 1 + DP[i][j]
                # else carry the max of prev values
                else:
                    DP[i+1][j+1] = max(DP[i][j+1], DP[i+1][j])
        for x in DP:
            print(x)
        # final cell is max value
        return DP[i+1][j+1]        
        
        # # NAIVE RECURSION + TLE
        # # print(text1, text2)
        # if text1 == "" or text2 == "":
        #     return 0
        # # check last element
        # if text1[-1] == text2[-1]:
        #     # if same means we have +1 to longest, check the elements infront
        #     return 1 + self.longestCommonSubsequence(text1[0:len(text1)-1], text2[0:len(text2)-1])
        # else:
        #     # if different means we decrement each side progressively and choose the maximum
        #     # i.e. 'ab' and 'a'
        #     # decrement 'ab' to compare 'a' and 'a' = 1 
        #     # vs 
        #     # decrementing 'a' to get 'ab' and '' = 0
        #     # choose max(1, 0) = 1
        #     return max(self.longestCommonSubsequence(text1[0:len(text1)-1], text2), self.longestCommonSubsequence(text1, text2[0:len(text2)-1]))
