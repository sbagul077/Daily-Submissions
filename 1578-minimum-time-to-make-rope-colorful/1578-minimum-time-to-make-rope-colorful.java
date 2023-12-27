class Solution {
    public int minCost(String colors, int[] neededTime) {
        int result = 0;
        int left = 0;
        
        for(int right = 1; right < colors.length(); right++){
            if(colors.charAt(left) == colors.charAt(right)){
                if(neededTime[left] < neededTime[right]){
                    result += neededTime[left];
                    left = right;
                }
                else{
                    result += neededTime[right];
                }
            }
            
            else{
                left = right;
            }
        }        
        return result;
        
    }
}

// Two Pointers
//Time Complexity: O(n)
//Space Complexity: O(1)