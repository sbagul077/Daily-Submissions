class Solution {
    public List<Integer> findAnagrams(String s, String p) {
        HashMap<Character, Integer> map = new HashMap<>();
        List<Integer> result = new ArrayList<>();

        for(int i = 0; i < p.length(); i++){
            char ch = p.charAt(i);

            map.put(ch, map.getOrDefault(ch, 0) + 1);
        }
        int match = 0;
        for(int i = 0; i < s.length(); i++){
            char incoming = s.charAt(i);

            if(map.containsKey(incoming)){
                int cnt = map.get(incoming);
                cnt -= 1;
                map.put(incoming, cnt);
                if(cnt == 0) match++;
            }

            if(i >= p.length()){
                char outgoing = s.charAt(i - p.length());
                if(map.containsKey(outgoing)){
                    int cnt = map.get(outgoing);
                    cnt += 1;
                    map.put(outgoing, cnt);
                    if(cnt == 1) match--;
                }
            }

            if(match == map.size()){
                result.add(i - p.length() + 1);
            }
        }

        return result;
    }
}

// Sliding Window
// Time Complexity: O(n)
// Space Complexity: O(1)