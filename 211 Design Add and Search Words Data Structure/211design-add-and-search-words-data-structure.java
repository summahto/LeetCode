class WordDictionary {
    TrieNode root;

    class TrieNode {
        private Character ch;
        private TrieNode [] children;
        boolean isWordEnd;

        public TrieNode(Character ch){
            this.ch = ch;
            this.children = new TrieNode[26];
        }
    }

    public WordDictionary() {
        this.root = new TrieNode('\u0000');
    }
    
    public void addWord(String word) {

        TrieNode curr = root;
        char [] charArr = word.toCharArray();

        for(char c : charArr){

            if(curr.children[c - 'a'] == null){
                TrieNode node = new TrieNode(c);
                curr.children[c- 'a'] = node;
            }

            curr = curr.children[c - 'a'];
        }

        curr.isWordEnd = true;
        
    }

    public boolean search(String word) {
        
        return searchHelper(word, root, 0);
    }
    
    public boolean searchHelper(String word, TrieNode curr, int index) {
        
        for(int i = index; i< word.length() ; i++){
            char c = word.charAt(i);

            if(c == '.'){

                for(TrieNode node : curr.children){
                    if(node != null && searchHelper(word, node, i+1) ) {
                        return true;    
                    }

                }
                //for searches which ends at '.' eg. "ma."
                //if all the nodes are null at i = 2 return false
                //for searches which have . anywhere else eg. "m.p"
                // for all cases where i = 0, 1 are satisfied but the 3rd char is null or not a word
                return false;
            }
            
            //if not '.' it has to be any other valid char, so no need to check it
            if(curr.children[c - 'a'] == null)
                return false;

            curr = curr.children[c - 'a'];

        }

        return curr.isWordEnd;


    }
}

/**
 * Your WordDictionary object will be instantiated and called as such:
 * WordDictionary obj = new WordDictionary();
 * obj.addWord(word);
 * boolean param_2 = obj.search(word);
 */