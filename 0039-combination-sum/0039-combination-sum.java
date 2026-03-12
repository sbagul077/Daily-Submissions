class Solution {
    List<List<Integer>> result;
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        result = new ArrayList<>();

        if(candidates == null || candidates.length == 0) return result;
        helper(candidates, 0, target, new ArrayList<>());
        return result;
    }


    private void helper(int[] candidates, int index, int target, List<Integer> path){
        //base
        if(target == 0){
            result.add(path);
            return;
        }
        if(target < 0 ||index == candidates.length) return;
        //logic
        // choose
        path.add(candidates[index]);
        helper(candidates, index, target - candidates[index], new ArrayList<>(path));
        path.remove(path.size() - 1);
        //not choose
        helper(candidates, index + 1, target, new ArrayList<>(path));   
    }
}

// Backtracking