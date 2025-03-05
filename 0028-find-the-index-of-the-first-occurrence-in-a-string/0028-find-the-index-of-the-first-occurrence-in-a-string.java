class Solution {
    public int strStr(String haystack, String needle) {
        if (needle.length() == 0)
            return 0;

        int m = haystack.length();
        int n = needle.length();

        for (int i = 0; i <= m - n; i++) {
            if (haystack.charAt(i) == needle.charAt(0)) {
                int k = i;
                int j = 0;

                while (k < m && j < n) {
                    char hay = haystack.charAt(k);
                    char need = needle.charAt(j);
                    if (hay == need) {
                        k++;
                        j++;
                    } else {
                        break;
                    }
                    if (j == n) {
                        return i;
                    }
                }
            }

        }

        return -1;
    }
}