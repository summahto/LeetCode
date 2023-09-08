class Trie {

    TrieNode root ;

    class TrieNode{
        Character ch;
        TrieNode [] children;
        boolean isEndNode;

        public TrieNode(Character ch){
            this.ch = ch;
            this.children = new TrieNode[26];
        }
    }

    public Trie() {
        this.root = new TrieNode('\u0000');
        // root.ch = '\u0000';
        // root.children = new TrieNode[26];
        
    }
    
    public void insert(String word) {
        char [] charArr = word.toCharArray();
        TrieNode curr = root;
        
        for (int i=0 ; i< charArr.length; i++){    
            
            if(curr.children[charArr[i] - 'a'] == null){
                TrieNode node = new TrieNode(charArr[i]);
                // node.ch = charArr[i];
                // node.children = new TrieNode[26];
                
                curr.children[charArr[i] - 'a'] = node;
                
            } 

            curr = curr.children[charArr[i] - 'a'];
            
            //differentiate between words and prefixes
            // if(i == charArr.length -1)
        }

        curr.isEndNode = true;
        
    }
    
    public boolean search(String word) {
        TrieNode curr = root;

        char [] arr = word.toCharArray();

        for(int i =0; i< arr.length ; i++){
            
            if(curr.children[arr[i]- 'a'] == null)
                return false;

            if(curr.children[arr[i] - 'a'].ch != arr[i])
                return false;
            
            curr = curr.children[arr[i] - 'a'];
        }

        if(curr.isEndNode == true)
            return true;
        else
            return false;

    }
    
    public boolean startsWith(String prefix) {
        TrieNode curr = root;

        char [] arr = prefix.toCharArray();

        for(int i =0; i< arr.length ; i++){
            
            if(curr.children[arr[i]- 'a'] == null)
                return false;

            if(curr.children[arr[i] - 'a'].ch != arr[i])
                return false;
            
            curr = curr.children[arr[i] - 'a'];
        }

        return true;
    }
}

/**
 * Your Trie object will be instantiated and called as such:
 * Trie obj = new Trie();
 * obj.insert(word);
 * boolean param_2 = obj.search(word);
 * boolean param_3 = obj.startsWith(prefix);
 */