class Solution {
    public boolean isValidSudoku(char[][] board) {
        if(board ==  null || board.length == 0){
            return false;
        }        

        //row
        for(int i = 0; i < board.length; i++){
            boolean[] numbers = new boolean[9];
            for(int j = 0; j < board[0].length; j++){
                if (board[i][j] != '.'){

                    if(numbers[board[i][j] - '1'] == true){
                        // System.out.println("Failed in rows");
                        return false;
                    }
                    numbers[board[i][j] - '1'] = true;
                }
            }
        }

        //column
        for(int j = 0; j < board[0].length; j++){
            boolean[] numbers = new boolean[9];
            for(int i = 0; i< board.length; i++){
                if(board[i][j] != '.'){
                    if(numbers[board[i][j] - '1'] == true){

                        return false;
                    }
                    numbers[board[i][j] - '1'] = true;
                }
            }
        }

        //blocks
        for(int b = 0; b < 9; b++){
            boolean[] numbers = new boolean[9];
            for(int i = b /3 * 3; i < (b / 3 * 3 + 3); i++){
                for(int j = b % 3 * 3; j <(b % 3 * 3 + 3); j++){
                    if(board[i][j] != '.'){


                        if(numbers[board[i][j] - '1'] == true){

                            return false;
                        }
                        numbers[board[i][j] - '1'] = true;
                    }
                }
            }
        }
    
    return true;
    }
}

//Time Complexity: O(1) - 9x9 grid means constant time.
//Space Complexity: O(1) - Only 27 sets used (constant space), each holds up to 9 elements.