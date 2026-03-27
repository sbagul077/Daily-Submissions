class TrieNode{
    TrieNode[] children;
    boolean isEnd;
    String currWord;
    public TrieNode(){
        this.children = new TrieNode[26];
        this.isEnd = false;
        currWord = "";
    }
}
class Solution {
    TrieNode root;

    public Solution(){
        this.root = new TrieNode();
    }
    public String replaceWords(List<String> dictionary, String sentences) {

        for(String word: dictionary){
            insert(word, root);
        }
        StringBuilder result = new StringBuilder();

        String[] sentence = sentences.split(" ");

        for(int j = 0; j < sentence.length; j++){
            if(j != 0){
                result.append(" ");
            }

            String word = sentence[j];
            StringBuilder replacement = new StringBuilder();
            TrieNode curr = root;

            for(int i = 0; i < word.length(); i++){
                char ch = word.charAt(i);

                if(curr.children[ch - 'a'] == null || curr.isEnd == true){
                    break;
                }

                replacement.append(ch);
                curr = curr.children[ch - 'a'];
                
            }
            if(curr.isEnd == true){
                result.append(replacement.toString());
            }else{
                result.append(word);
            }
        }

        return result.toString();
    }


    private void insert(String word, TrieNode curr){
        
        for(int i = 0; i < word.length(); i++){
            char ch = word.charAt(i);

            if(curr.children[ch - 'a'] == null){
                curr.children[ch - 'a'] = new TrieNode();
            }

            curr = curr.children[ch - 'a'];
        }

        curr.isEnd = true;
        curr.currWord = word;
    }
}


// TrieNode
//