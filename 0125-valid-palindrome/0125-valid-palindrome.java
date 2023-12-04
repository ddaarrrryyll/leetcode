class Solution {
    public boolean isPalindrome(String s) {
        int left = 0;
        int right = s.length()-1;
        while (left < right) {
            boolean skip = false;
            char left_char = Character.toLowerCase(s.charAt(left));
            char right_char = Character.toLowerCase(s.charAt(right));
            
            // System.out.println(left_char + " | " + right_char);
            
            if (!Character.isLetter(left_char) && !Character.isDigit(left_char)) {
                left++;
                skip = true;
            }
            if (!Character.isLetter(right_char) && !Character.isDigit(right_char)) {
                right--;
                skip = true;
            }
            
            if (!skip) {
                if (left_char == right_char) {
                    left++;
                    right--;
                } else {
                    return false;
                }   
            }
        }
        return true;
    }
}