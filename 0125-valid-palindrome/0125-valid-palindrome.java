class Solution {
    public boolean isPalindrome(String s) {

        if (s == null || s.length() == 0) {
            return true;
        }

        int left = 0;
        int right = s.length() - 1;
        System.out.println(right);
        while (left < right) {
            char charLeft = s.charAt(left);
            char charRight = s.charAt(right);
            System.out.println(charLeft);
            System.out.println(charRight);

            if (!Character.isAlphabetic(charLeft) && !Character.isDigit(charLeft)) {
                left++;
            } else if (!Character.isAlphabetic(charRight) && !Character.isDigit(charRight)) {
                right--;
            } else if (Character.toLowerCase(charLeft) != Character.toLowerCase(charRight)) {

                return false;
            } else {
                left++;
                right--;
            }

        }

        return true;
    }
}