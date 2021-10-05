# this is like calculation in cz1107, where we use a stack to track asteroids
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        
        # push all -ve values into stack until you meet first +ve value
        i = 0
        while i < len(asteroids) and asteroids[i] < 0:
            stack.append(asteroids[i])
            i += 1
        
        for j in range(i, len(asteroids)):
            # while asteroids[j] is +ve, push it to stack
            if asteroids[j] > 0 or len(stack) == 0:
                stack.append(asteroids[j])
            # else if asteroids[j] is -ve
            else:
                # pop the top of the stack while top of stack (must be +ve) + asteroids[j] <= 0 (i.e. asteroids[j] is bigger)
                while stack[len(stack)-1] > 0 and stack[len(stack)-1] + asteroids[j] <= 0:
                    top = stack.pop()
                    if top + asteroids[j] == 0:
                        break
                    if len(stack) == 0:
                        stack.append(asteroids[j])
                        break
                else:
                    # append if top of stack is -ve
                    if stack[len(stack)-1] < 0:
                        stack.append(asteroids[j])
                    # explode -ve asteroid and break out of while loop
                    elif stack[len(stack)-1] + asteroids[j] > 0:
                        continue
            
        return stack