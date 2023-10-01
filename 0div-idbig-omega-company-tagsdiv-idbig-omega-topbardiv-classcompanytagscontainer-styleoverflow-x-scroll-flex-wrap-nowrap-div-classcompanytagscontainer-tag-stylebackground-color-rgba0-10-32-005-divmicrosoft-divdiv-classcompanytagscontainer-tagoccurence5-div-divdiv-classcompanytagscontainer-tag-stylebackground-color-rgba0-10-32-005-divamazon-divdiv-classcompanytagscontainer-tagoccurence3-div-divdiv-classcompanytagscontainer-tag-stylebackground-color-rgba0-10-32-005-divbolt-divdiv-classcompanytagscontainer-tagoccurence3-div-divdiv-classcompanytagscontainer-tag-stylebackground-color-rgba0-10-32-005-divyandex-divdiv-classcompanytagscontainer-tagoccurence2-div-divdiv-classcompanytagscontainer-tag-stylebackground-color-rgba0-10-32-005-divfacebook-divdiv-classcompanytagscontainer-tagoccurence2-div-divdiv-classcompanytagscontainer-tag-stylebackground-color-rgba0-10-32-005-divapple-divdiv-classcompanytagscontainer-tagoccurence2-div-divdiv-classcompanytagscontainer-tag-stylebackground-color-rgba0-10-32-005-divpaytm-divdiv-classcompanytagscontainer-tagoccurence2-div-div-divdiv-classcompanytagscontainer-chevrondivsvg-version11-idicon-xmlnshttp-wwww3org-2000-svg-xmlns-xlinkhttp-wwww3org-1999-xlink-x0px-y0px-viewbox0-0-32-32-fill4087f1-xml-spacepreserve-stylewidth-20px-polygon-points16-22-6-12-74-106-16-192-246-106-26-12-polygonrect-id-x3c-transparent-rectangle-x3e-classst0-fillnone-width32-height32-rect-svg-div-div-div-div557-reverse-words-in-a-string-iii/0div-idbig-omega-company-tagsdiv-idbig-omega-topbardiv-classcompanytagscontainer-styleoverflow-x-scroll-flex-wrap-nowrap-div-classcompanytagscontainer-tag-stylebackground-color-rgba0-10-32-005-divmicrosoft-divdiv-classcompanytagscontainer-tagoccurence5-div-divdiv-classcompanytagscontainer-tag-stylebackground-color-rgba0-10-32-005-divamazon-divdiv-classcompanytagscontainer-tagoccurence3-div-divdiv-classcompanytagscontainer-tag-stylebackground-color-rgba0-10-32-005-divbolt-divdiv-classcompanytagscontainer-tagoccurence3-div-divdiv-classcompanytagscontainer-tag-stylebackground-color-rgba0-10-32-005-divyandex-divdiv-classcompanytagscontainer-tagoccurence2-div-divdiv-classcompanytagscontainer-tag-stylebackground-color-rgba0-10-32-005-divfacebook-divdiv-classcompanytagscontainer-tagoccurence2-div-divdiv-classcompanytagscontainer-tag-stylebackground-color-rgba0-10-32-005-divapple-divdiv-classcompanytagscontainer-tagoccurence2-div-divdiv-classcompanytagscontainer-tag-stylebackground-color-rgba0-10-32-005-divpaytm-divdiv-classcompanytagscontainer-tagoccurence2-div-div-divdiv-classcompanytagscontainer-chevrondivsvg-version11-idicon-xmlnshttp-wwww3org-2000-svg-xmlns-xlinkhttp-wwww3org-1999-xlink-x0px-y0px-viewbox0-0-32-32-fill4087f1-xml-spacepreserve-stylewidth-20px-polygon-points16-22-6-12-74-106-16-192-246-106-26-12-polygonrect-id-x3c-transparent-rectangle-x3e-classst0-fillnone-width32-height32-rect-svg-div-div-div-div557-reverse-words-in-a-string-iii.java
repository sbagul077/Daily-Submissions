class Solution {
    public String reverseWords(String s) {
        int left = 0;
        
        char[] chArray = s.toCharArray();
        int len = s.length();
        
        for(int right = 0; right < len; right++){
            if(chArray[right] == ' ' || right == (len - 1)){
                int temp_left = left;
                int temp_right = right - 1;
                
                if(right == (len - 1)){
                    temp_right = right;
                }
                
                while(temp_left < temp_right){
                    char temp = chArray[temp_left];
                    chArray[temp_left] = chArray[temp_right];
                    chArray[temp_right] = temp;
                    
                    temp_left ++;
                    temp_right --;
                }
                
                left = right + 1;
                
            }
        }        
        return new String(chArray);
    }
}

//Two Pointers 
//Time Complexity: O(n)
//Space Complexity: O(1)