class Solution {
    public char nextGreatestLetter(char[] letters, char target) {
        char[] arr = new char[26];

        for(int i = 0; i < letters.length; i++){
            // System.out.println(letters[i] - 'a');
            arr[letters[i] - 'a'] = letters[i];
        }

        for(int i = 0; i < 26; i++){
            if(arr[i] != '\u0000' && target < arr[i]){
                return arr[i];
            }
        }

        return letters[0];        
    }
}