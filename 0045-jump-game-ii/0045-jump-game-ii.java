class Solution {
    public int jump(int[] nums) {
        if(nums == null || nums.length < 2){
            return 0;
        }

        int jumps = 1;
        int nextInt = nums[0];
        int currInt = nums[0];

        for(int i = 1; i< nums.length - 1; i++){
            nextInt = Math.max(nextInt, nums[i] + i);

            if(i == currInt){
                jumps += 1;
                currInt = nextInt;
            }
        }

        return jumps;
    }
}