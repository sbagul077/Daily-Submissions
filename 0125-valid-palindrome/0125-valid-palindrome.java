class Solution {
    public boolean isPalindrome(String s) {
        StringBuilder sb = new StringBuilder();

        for(int i = 0; i< s.length(); i++){
            char ch = s.charAt(i);
                if(Character.isLetter(ch) || Character.isDigit(ch)){
                    sb.append(ch);
                }                
                       
        }
        int left = 0;
        int right = sb.length() - 1;
        System.out.println(sb);
        while(left <= right){
            char charLeft = sb.charAt(left);
            char charRight = sb.charAt(right);

            if(Character.toLowerCase(charLeft) != Character.toLowerCase(charRight)){
                // System.out.println(charLeft);
                // System.out.println(charRight);
                // System.out.println(left);
                // System.out.println(right);
                return false;
            }
            left++;
            right--;
        }
        return true;
    }
}