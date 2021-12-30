class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        
        # fix positions (longer, shorter)
        if len(str1) < len(str2):
            str1, str2 = str2, str1
        
        # if shorter string is empty (usually it's the original longer string) means that the longer string can be partitioned into k x original shorter (now longer) string
        if str2 == "":
            print(str1, str2)
            return str1
        
        # if first n chars of longer string is same as shorter string, check the remaining chars
        if str1[:len(str2)] == str2:
            str1_part = str1[len(str2):]
            
        # if they are different, there is no gcd
        else:
            return "" 
        
        return self.gcdOfStrings(str1_part, str2)