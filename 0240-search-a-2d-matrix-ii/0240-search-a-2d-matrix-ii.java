class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        
        int m = matrix.length;
        int n = matrix[0].length;
        int i = m - 1;
        int j = 0;

        while(i >= 0 && j < n){

            int curr = matrix[i][j];
            System.out.print(curr);
            if(curr == target){
                return true;
            }
            else if(curr > target){
                i--;
            }
            else{
                j++;
            }
        }
        
        return false;    
        
    }
}


//Two Pointers
//TC: O(m) + O(n)
//SC: O(1)