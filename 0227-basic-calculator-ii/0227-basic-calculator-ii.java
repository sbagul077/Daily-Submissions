class Solution {
    public int calculate(String s) {
        s = s.trim();
        int curr = 0; // main curr number
        int calc = 0;
        Stack<Integer> st = new Stack<>();
        char lastSign = '+';

        for(int i = 0; i < s.length(); i++){
            char ch = s.charAt(i);

            if(Character.isDigit(ch)){
                curr = curr * 10 + ch - '0';
            }

            if(ch != ' ' && (!Character.isDigit(ch) || i == s.length() - 1)){
                if(lastSign == '+'){
                    st.push(curr);
                }
                else if(lastSign == '-'){
                    st.push(-curr);
                }
                else if(lastSign == '*'){
                    st.push(st.pop() * curr);
                }
                else if(lastSign == '/'){
                    st.push(st.pop() / curr);
                }

                lastSign = ch;
                curr = 0;
            }
        }

        while(!st.empty()){
            calc += st.pop();
        }
        return calc;
    }
}
// Stack
// Time Complexity: O(n)
// Space Complexity: O(n)