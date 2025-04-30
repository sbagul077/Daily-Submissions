class Solution {
    public int findNumbers(int[] nums) {
        if(nums == null) return 0;

        int count = 0;

        for(int num: nums){
            if(hasEvenCount(num + "")){
                count += 1;
            }
        }
        return count;
    }

    private boolean hasEvenCount(String num){
        if(num.length() % 2 == 0){
            return true;
        }

        return false;
        }
}

//Coding
//Time Complexity: O(n * LogV)
//Space Complexity: O(1)