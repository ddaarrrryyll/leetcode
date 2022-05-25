class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        # if index of 1 is >= max of sublist before 1 start checking AP
            # if sum of all elements on the left including flex[i] corresponds to sum from 1 to i, +1
        # if index of 1 is < max of sublist before 1, do the same thing
        ans = 0
        i = 0
        curr_max = 0
        curr_sum = 0
        flag1 = False
        flag_consec = False
        while i < len(flips):
            curr_sum += flips[i]
            # check if we already passed 1
            if (not flag1 and flips[i] != 1):
                i += 1
                continue
            flag1 = True
            
            # if consecutive, don't have to sum 
            if flag_consec and flips[i] == curr_max + 1:
                ans += 1
                curr_max = flips[i]
            # no longer consecutive
            else:
                flag_consec = False
                curr_max = max(curr_max, flips[i])
            
                # AP = n(n+1)/2
                
                            # no.ele * (last + 1) // 2
                if curr_sum == ((i+1) * (i+1 + 1)//2):
                    ans += 1
                    flag_consec = True
                    curr_max = max(flips[0:i+1])

            i += 1
        return ans