class Solution {
    public String decodeString(String s) {
        if(s == null || s.length() == 0){
            return "";
        }

        Stack<Integer> numSt = new Stack<>();
        Stack<String> strSt = new Stack<>();
        String curr = "";
        int num = 0;

        for(int i = 0; i < s.length(); i++){
            char ch = s.charAt(i);

            if(Character.isDigit(ch)){
                num = num * 10 + ch - '0';
            }
            else if (ch == '['){
                numSt.add(num);
                strSt.add(curr);
                curr = "";
                num = 0;
            }
            else if(ch == ']'){
                int times = numSt.pop();
                StringBuilder newStr = new StringBuilder();
                for(int time = 0; time < times; time++){
                    newStr.append(curr);
                }
                curr = strSt.pop();
                curr += newStr;
            }
            else{
                curr += ch;
            }
        }

        return curr;

    }
}