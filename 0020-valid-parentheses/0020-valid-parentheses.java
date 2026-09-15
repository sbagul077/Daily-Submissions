class Solution {
    public boolean isValid(String s) {
        if(s.length() == 0 || s == null){
            return false;
        }

        Stack<Character> st = new Stack<>();

        for(int i = 0; i < s.length(); i++){
            char ch = s.charAt(i);

            if(ch == '{'){
                st.add('}');
            }
            else if(ch == '('){
                st.add(')');
            }
            else if(ch == '['){
                st.add(']');
            }else if(st.isEmpty() || st.pop() != ch){
                return false;
            }
        }

        return st.size() == 0;
    }
}

// Stack
// Time Complexity: O(n)
// Space Complexity: O(n)