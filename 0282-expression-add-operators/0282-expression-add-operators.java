class Solution {
    List<String> result;
    public List<String> addOperators(String num, int target) {
        result = new ArrayList<>();

        helper(num, target, 0, 0, 0, new StringBuilder());
        return result;
    }

    private void helper(String num, int target, int index, long calc, long tail, StringBuilder path){
        if(index == num.length()){
            if(target == calc){
                result.add(path.toString());
            }
        return;        
        }

        for(int i = index; i < num.length(); i++){
            if(i != index && num.charAt(index) == '0'){
                continue;
            }
            long curr = Long.parseLong(num.substring(index, i + 1));
            int le = path.toString().length();
            if(index == 0){
                path.append(curr); // action
                helper(num, target, i + 1, curr, curr, path); //recurse
                path.setLength(le);
            }
            else{
                //+
                path.append("+");//action
                path.append(curr);//action
                helper(num, target, i + 1, calc + curr, curr, path); // recurse
                path.setLength(le); //backtrack
                // -
                path.append("-"); //action
                path.append(curr); //action
                helper(num, target, i + 1, calc - curr, -curr, path); //recurse
                path.setLength(le); //backtrack
                //*
                path.append("*"); // action
                path.append(curr); //action
                helper(num, target, i + 1, calc - tail + (tail * curr), tail * curr, path); // recurse
                path.setLength(le); //backtrack
            }
        }
    }
}