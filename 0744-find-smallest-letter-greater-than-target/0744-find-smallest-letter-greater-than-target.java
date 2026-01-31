class Solution {
    public char nextGreatestLetter(char[] letters, char target) {
        int[] primes =  {2, 3, 5, 7, 11, 13, 17, 19, 23, 29,
                            31, 37, 41, 43, 47, 53, 59, 61, 67, 71,
                            73, 79, 83, 89, 97, 101};
        
        char result = target;
        for(int i = 0; i< letters.length; i++){
            char currChar = letters[i];
            if(target - currChar < 0){
                result = currChar;
                break;
            }
        }

        if(result == target){
            result = letters[0];
        }
        return result;
    }
}