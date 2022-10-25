class Solution {
    public boolean arrayStringsAreEqual(String[] word1, String[] word2) {
        String combined1 = "";
        String combined2 = "";
        for (int i = 0; i < word1.length; i++) combined1 += word1[i];
        for (int j = 0; j < word2.length; j++) combined2 += word2[j];
        return combined1.equals(combined2);
    }
}