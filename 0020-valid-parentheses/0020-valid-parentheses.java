import java.util.Stack;

class Solution {
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<>(); // (

        for (Character c : s.toCharArray()) {
            if (c.equals('(') || c.equals('{') || c.equals('[')) {
                stack.push(c);
            } else {
                if (stack.isEmpty()) return false;
                Character bracket = stack.pop();
                if (c.equals(')')) {
                    if (!bracket.equals('(')) return false;
                } else if (c.equals('}')) {
                    if (!bracket.equals('{')) return false;
                } else if (c.equals(']')) {
                    if (!bracket.equals('[')) return false;
                }    
            }
        }
        return stack.isEmpty();
    }
}
