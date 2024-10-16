class Solution {
    public int[] findDiagonalOrder(int[][] mat) {
        if (mat == null || mat.length == 0){
            return new int[0];
        }
        
        int m = mat.length;
        int n = mat[0].length;
        int i = 0;
        int direction = 1;
        int r = 0;
        int c = 0;
        int[] result = new int[m *n];
        
        while(i <= m * n-1){
            result[i] = mat[r][c];
            i += 1;
            //upwards
            if(direction == 1){
                if(c == n - 1){
                    r += 1;
                    direction = -1;
                }
                else if(r == 0){
                    c += 1;
                    direction = -1;
                }
                else{
                    r -= 1;
                    c += 1;
                }
            }
            else{
                if(r == m - 1){
                    c += 1;
                    direction = 1;
                }
                else if(c == 0){
                    r++;
                  direction = 1;
                }
                else{
                   r++; 
                   c--; 
                }
            }
                
        }
        
        return result;
            
    }
}

// Time Complexity: O(n)
// Space Compelxity: O(1)