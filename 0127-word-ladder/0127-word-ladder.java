class Solution {
    public int ladderLength(String beginWord, String endWord, List<String> wordList) {
        if(beginWord == null || endWord == null){
            return 0;
        }        
        if(beginWord == endWord){
            return 0;
        }
        boolean exist = false;
        for(int i = 0; i< wordList.size(); i++){
            if(beginWord.equals(wordList.get(i))){
                exist = true;
                break;
            }
        }
        if(exist == false){
            wordList.add(beginWord);
        }
        HashMap<String, List<String>> map = new HashMap<>();
        
        for(int i = 0; i< wordList.size(); i++){
            String word = wordList.get(i);

            for(int j = 0; j < word.length(); j++){
                String newWord = word.substring(0, j) + '*' + word.substring(j + 1, word.length());
                if(!map.containsKey(newWord)){
                    map.put(newWord, new ArrayList<>());
                }
                map.get(newWord).add(word);
            }
        }

        Queue<String> q = new LinkedList<>();
        int level = 0;
        q.add(beginWord);
        // level++;
        HashMap<String, Boolean> visited = new HashMap<>();
        visited.put(beginWord, true);

        while(!q.isEmpty()){
            int size = q.size();
            level++;
            for(int i = 0; i< size; i++){
                String word = q.poll();

                if (word.equals(endWord)){
                    return level;
                }
                for(int j = 0; j < word.length(); j++){
                    String newWord = word.substring(0, j) +  '*' + word.substring(j + 1, word.length());
                    List<String> li = map.getOrDefault(newWord, new ArrayList<>());
                    for(String adjWord: li){
                        if(!visited.containsKey(adjWord)){
                            visited.put(adjWord,true);
                            q.add(adjWord);
                        }
                    }
                }
            }
        }
                        return 0;
    }
}