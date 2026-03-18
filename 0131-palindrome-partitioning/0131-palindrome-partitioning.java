class Solution {
    List<List<String>> result;
    public List<List<String>> partition(String s) {
        result = new ArrayList<>();

        helper(s, 0, new ArrayList<>());

        return result;
    }

    private void helper(String s, int index, List<String> path){
        // System.out.println(path);
        if(index == s.length()){
            result.add(new ArrayList<>(path));
            return;
        }

        for(int i = index; i < s.length(); i++){
            if(isPalindrome(s, index, i) == true){
                // StringBuilder temp = new StringBuilder(s.substring(index, i));
                path.add(s.substring(index, i+1));
                helper(s, i + 1, path);
                path.remove(path.size() - 1);

            }
        }
    }

    private boolean isPalindrome(String s, int left, int right){

        while(left < right){
            if(s.charAt(left) != s.charAt(right)){
                return false;
            }
            left++;
            right--;
        }

        return true;
    }
}

//For Loop backtrack Recursion 
