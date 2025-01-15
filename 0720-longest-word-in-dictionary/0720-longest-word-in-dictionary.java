class TrieNode{
    TrieNode[] children;
    // String c;
    boolean isEnd;

    public TrieNode(){
        children = new TrieNode[26];
        // c = "";
        isEnd =  false;
    }
}
class Solution {
    private String result ="";
    TrieNode root;;
    public void insert(String word, TrieNode root){
        TrieNode curr = root;

        for(int i = 0; i < word.length(); i++){
            char ch = word.charAt(i);

            if(curr.children[ch - 'a'] == null){
                curr.children[ch - 'a'] = new TrieNode();
            }
            curr = curr.children[ch - 'a'];
            // curr.c = ch;
        }
        curr.isEnd = true;
    }

    public String longestWord(String[] words) {
        root = new TrieNode();
 
        for(String word: words){
            insert(word, root);
        }

        dfs(root, new StringBuilder(""));
        return result;
    }

    public void dfs(TrieNode curr, StringBuilder path){
        if( path.length() >= result.length()){
            result =  path.toString();
        }

        for(int i = 25; i >= 0; i--){
            if(curr.children[i] != null && curr.children[i].isEnd == true){
                int le = path.length();
                path.append((char)(i + 97));
                dfs(curr.children[i], path);
                path.setLength(le);
            }
        }
    }
}