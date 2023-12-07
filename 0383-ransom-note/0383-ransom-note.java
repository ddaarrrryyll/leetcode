class Solution {
    public boolean canConstruct(String ransomNote, String magazine) {
        
        if (ransomNote.length() > magazine.length()) return false;
        
        HashMap<Character, Integer> avail_chars = new HashMap<Character, Integer>();
        int count;
        char c;
        
        for (int i = 0; i < magazine.length(); i++) {
            c = magazine.charAt(i);
            if (avail_chars.get(c) == null) {
                avail_chars.put(c, 1);
            } else {
                count = avail_chars.get(c);
                avail_chars.remove(c);
                avail_chars.put(c, count+1);
            }
        }
        
        for (int j = 0; j < ransomNote.length(); j++) {
            c = ransomNote.charAt(j);
            if (avail_chars.get(c) == null || avail_chars.get(c) <= 0) return false;
            else {
                count = avail_chars.get(c);
                avail_chars.remove(c);
                avail_chars.put(c, count-1);
            }
        }
        
        return true;
    }
}