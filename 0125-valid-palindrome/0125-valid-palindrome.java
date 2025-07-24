class Solution {
    public boolean isPalindrome(String s) {
        if(s == null || s.length() == 0){
            return false;
        }

        int left = 0;
        int right = s.length() - 1;

        while(left <= right){
            if(!Character.isAlphabetic(s.charAt(left)) && !Character.isDigit(s.charAt(left))){
                left++;
            }
            else if(!Character.isAlphabetic(s.charAt(right)) && !Character.isDigit(s.charAt(right))){
                right--;
            }
            else if(Character.toLowerCase(s.charAt(left)) == Character.toLowerCase(s.charAt(right))){
                left++;
                right--;
            }
            else{
                return false;
            }
        }

        return true;

    }
}