class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) return false;
        HashMap<Character, Integer> char_map = new HashMap<Character, Integer>();
        int count;
        
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (char_map.get(c) == null) {
                char_map.put(c, 1);
            } else {
                count = char_map.get(c);
                char_map.remove(c);
                char_map.put(c, count + 1);
            }
        }
        
        for (int j = 0; j < t.length(); j++) {
            char x = t.charAt(j);
            if (char_map.get(x) == null) {
                return false;
            } else {
                count = char_map.get(x)-1;
                if (count < 0) return false;
                char_map.remove(x);
                char_map.put(x, count);
            }
        }
        
        return true;
    }
}