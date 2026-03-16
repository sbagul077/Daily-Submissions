class Solution {
    List<List<Integer>> result;
    public List<List<Integer>> subsets(int[] nums) {
        result = new ArrayList<>();
        // if(nums == null || nums.length == 0){
        //     return result;
        // }
        helper(nums, 0, new ArrayList<>());
        return result;
    }

    private void helper(int[] nums, int index, List<Integer> path){
        result.add(new ArrayList<>(path));

        for(int i = index; i < nums.length; i++){
            path.add(nums[i]);
            helper(nums, i + 1, path);
            path.remove(path.size() - 1);
        }
    }
}

// #For loop Recursion with Backtracking
// #TC : O(2^n)
// #SC :O(2^n)