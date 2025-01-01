class Solution {
    public String decodeString(String s) {
        if(s == null  || s.length() == 0){
            return "";
        }

        Stack <Integer> numSt = new Stack<>();
        Stack <String> strSt = new Stack<>();
        String curr = "";
        int num = 0;

        for(int i = 0; i < s.length(); i++){
            char c = s.charAt(i);

            if(Character.isDigit(c)){
                num = num * 10 + c - '0';
            }
            else if(c == '['){
                numSt.add(num);
                strSt.add(curr);
                curr = "";
                num = 0;
            }
            else if (c == ']'){
                int times = numSt.pop();
                StringBuilder newStr = new StringBuilder();
                for(int time = 0; time < times; time++){
                    newStr.append(curr);
                }
                curr = strSt.pop();
                curr += newStr;
            }
            else{
                curr += c;
            }
        }

        return curr;
    }
}


//Iterative Approach
//Time Complexity: O(n)
//Space Complexity: O(n)