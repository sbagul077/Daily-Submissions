class Solution {
    public int maximumElementAfterDecrementingAndRearranging(int[] arr) {
        Arrays.sort(arr);
        
        int prev = 0;
        
        for(int i = 0; i< arr.length; i++){
            prev = Math.min(prev + 1, arr[i]);
            
        }
        
        return prev;
    }
}

