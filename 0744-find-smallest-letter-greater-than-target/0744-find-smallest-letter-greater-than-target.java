class Solution {
    public char nextGreatestLetter(char[] letters, char target) {
        int n = letters.length;
        int low = 0;
        int high = n - 1;
        char result = letters[0];

        while(low <= high){
            int mid = low + (high - low) / 2;

            if(target < letters[mid]){
                result = letters[mid];
                high = mid - 1;
            }
            else{
                low = mid + 1;
            }
        }

        return result;
    }
}