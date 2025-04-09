class Solution {
    public int maximalSquare(char[][] matrix) {
        if(matrix == null || matrix.length == 0){
            return 0;
        }
        int max = Integer.MIN_VALUE;
        int m = matrix.length;
        int n = matrix[0].length;
        boolean flag = false;
        for(int i = 0; i < m; i++){
            for(int j = 0; j < n; j++){
                if(matrix[i][j] == '1'){
                    flag = true;
                    int curr = 1;
                    // i + curr ,  j + curr
                    while(i + curr < m && j + curr < n && flag){
                        //same row of i + curr and j + curr
                        for(int k = j; k <= j + curr; k++){
                            if(matrix[i + curr][k] == '0'){
                                flag = false;
                                break;
                            }
                        }

                        //same col of i+ curr and j + curr
                        for(int k = i; k <= i + curr; k++){
                            if(matrix[k][j + curr] == '0'){
                                flag = false;
                                break;
                            }
                        }
                        if(flag == true){
                            curr++;
                        }                        
                    }
                    max = Math.max(max, curr);
                }
            }
        }
        return max* max;
    }
}
//brute force
//time complexity :O(m*n)^2
//Space Complexity: O(1)