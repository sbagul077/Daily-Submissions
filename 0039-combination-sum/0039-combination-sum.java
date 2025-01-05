class Solution {
    List<List<Integer>> result;
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        result = new ArrayList<>();
        if(candidates == null || candidates.length == 0){
            return result;
        }

        helper(candidates, 0, target, new ArrayList<>());

        return result;
    }

    private void helper(int[] candidates, int index, int target, List<Integer> path){
        if(target == 0){
            result.add(new ArrayList<>(path));
            return;
        }

        if((target < 0) || index == candidates.length){
            return;
        }

        for(int i = index; i< candidates.length; i ++){
            // #action
            path.add(candidates[i]);
            // recurse
            helper(candidates, i, target- candidates[i], path);
            // backtrack
            path.remove(path.size() - 1);
        }
    
    }
}