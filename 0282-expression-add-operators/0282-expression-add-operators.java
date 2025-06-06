class Solution {
    List<String> result;
    public List<String> addOperators(String num, int target) {
        result = new ArrayList<>();

        helper(num, target, 0, 0, 0, "");
        return result;
    }

    private void helper(String num, int target, int index, long calc, long tail, String path){
        if(index == num.length()){
            if(target == calc){
                result.add(path);
            }
        return;        
        }

        for(int i = index; i < num.length(); i++){
            if(i != index && num.charAt(index) == '0'){
                continue;
            }
            long curr = Long.parseLong(num.substring(index, i + 1));

            if(index == 0){
                helper(num, target, i + 1, curr, curr, path + curr);
            }
            else{
                //+
                helper(num, target, i + 1, calc + curr, curr, path + "+" + curr);
                // -
                helper(num, target, i + 1, calc - curr, -curr, path + "-"+ curr);
                //*
                helper(num, target, i + 1, calc - tail + (tail * curr), tail * curr, path + "*" + curr);
            }
        }
    }
}