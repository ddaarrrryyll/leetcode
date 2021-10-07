class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        count = 0
        for i in range(len(s)):
            # count keeps track of the number of duplicate chars (essential if number < k) so that we can skip s[i]
            if count > 0:
                count-=1
                # print(f"skipping s[{i}] = {s[i]}")
                continue
                
            # if empty stack / prev char is different, then append to stack   
            if len(stack) == 0 or stack[len(stack)-1] != s[i]:
                stack.append(s[i])
            else:
                # get duplicate chars from top of stack
                temp = []
                while len(stack) > 0 and stack[len(stack)-1] == s[i]:
                    temp.append(stack[len(stack)-1])
                    stack.pop()
                    # print(f"{temp=} {stack=}")
                j = 0
                
                # while the following chars are duplicates, add to temp
                while i+j < len(s) and s[i+j] == temp [0] and temp.count(s[i]) <= k:
                    count += 1
                    temp.append(s[i+j])
                    # print(temp)
                    # if at any point we meet the requirements (k duplicates), then we break from loop and 'delete' the characters we took out from stack
                    if temp.count(s[i])== k:
                        break
                    j+=1
                # print(temp.count(s[i]))
                
                # if total count is not k then we add back the chars we took out as well as the following duplicate chars
                if temp.count(s[i]) != k:
                    for _ in temp:
                        stack.append(_)
                        
                # decrement count by 1 because we are moving on to the next char so we have to take it into account
                count -= 1
                
            # print(stack)
        return ''.join(stack)