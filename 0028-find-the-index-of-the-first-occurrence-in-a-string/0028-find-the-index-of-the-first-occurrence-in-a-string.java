class Solution {
    public int strStr(String haystack, String needle) {
        if (needle.length() == 0)
            return 0;

        int m = haystack.length();
        int n = needle.length();
        int i = 0; //source
        int j = 0; //pattern

        int[] lps = lps(needle);

        while(i < m){
            if(haystack.charAt(i) == needle.charAt(j)){
                i += 1;
                j += 1;
               
                if(j == n){
                    return i - n;
                }
            }
            else if(haystack.charAt(i) != needle.charAt(j) && j > 0){
                j = lps[j - 1];
            }else if(haystack.charAt(i) != needle.charAt(j) && j == 0){
                i++;
            }
        }

        return -1;
    }

    private int[] lps(String needle){
        int[] lps = new int[needle.length()];
        lps[0] = 0;
        int i = 1;
        int j = 0;

        while(i < needle.length()){
            if(needle.charAt(i) == needle.charAt(j)){
                j +=1;
                lps[i] = j;
                i++;
            }
            else if(needle.charAt(i) != needle.charAt(j) && j > 0){
                j = lps[j - 1];
            }else if(needle.charAt(i) != needle.charAt(j) && j == 0){
                lps[i] = 0;
                i++;
            }
        }
        return lps;
    }
}