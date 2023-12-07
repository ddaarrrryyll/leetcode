class Solution {
    public int longestPalindrome(String s) {
        
        if (s.isEmpty()) return 0;
        
        HashMap<Character, Integer> map = new HashMap<Character, Integer>();
        
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            map.put(c, map.getOrDefault(c, 0) + 1);
        }
        
        int res = 0;
        boolean odd = false;
        
        for (HashMap.Entry<Character, Integer> k_v : map.entrySet()) {
            // System.out.println(k_v);
            if (k_v.getValue() % 2 == 0) {
                res += k_v.getValue();
            } else {
                res += k_v.getValue()-1;
                odd = true;
            }
        }
        
        if (odd) return res + 1;
        else return res;
    }
}