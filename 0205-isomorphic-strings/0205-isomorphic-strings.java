class Solution {
    public boolean isIsomorphic(String s, String t) {
        if(s == null || s.length() == 0 || t == null || t.length() == 0){
            return true;
        }

        if(s.length() != t.length()){
            return false;
        }

        Map<Character, Character> sMap = new HashMap<>();
        Map<Character, Character> tMap = new HashMap<>();

        for(int i = 0; i < s.length(); i++){
            char sChar = s.charAt(i);
            char tChar = t.charAt(i);

            if(!sMap.containsKey(sChar)){
                sMap.put(sChar, tChar);
            }
            else{
                if(sMap.get(sChar) != tChar){
                    return false;
                }
            }

            if(!tMap.containsKey(tChar)){
                tMap.put(tChar, sChar);
            }
            else{
                if(tMap.get(tChar) != sChar){
                    return false;
                }
            }
        }

        return true;

    }
}

// #Time Complexity: O(n)
// #Space Complexity: O(n)