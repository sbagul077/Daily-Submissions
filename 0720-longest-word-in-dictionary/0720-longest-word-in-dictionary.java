class TrieNode{
    TrieNode[] children;
    boolean isEnd;

    public TrieNode(){
        children = new TrieNode[26];
        isEnd = false;
    }
}
class Solution {
    private String result ="";
    TrieNode root;

    private void insert(TrieNode root, String word){
        TrieNode curr = root;


        for(int i = 0; i < word.length(); i++){
            char ch = word.charAt(i);

            if(curr.children[ch - 'a'] == null){
                curr.children[ch - 'a'] = new TrieNode();
            }
            curr = curr.children[ch - 'a'];
        }
        curr.isEnd = true;
        
    }

    public String longestWord(String[] words) {     
        if(words == null || words.length == 0){
            return "";
        }
        root = new TrieNode();
        for(String word: words){
            insert(root, word);
        }
        dfs(root, new StringBuilder(""));

        return result;
    }

    private void dfs(TrieNode curr, StringBuilder path){
        // System.out.println(path.toString())
        if (path.length() >= result.length()){
            result = path.toString();
        }

        for(int i = 25; i >= 0; i--){
            if(curr.children[i] != null && curr.children[i].isEnd == true){
                int le = path.length();
                path.append((char)(i + 97));
                // System.out.println(path.toString());
                dfs(curr.children[i], path);
                path.setLength(le);
            }
        }        
    }
}
