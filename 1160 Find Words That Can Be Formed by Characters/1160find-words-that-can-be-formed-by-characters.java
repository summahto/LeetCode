class Solution {
    public int countCharacters(String[] words, String chars) {
        
        int [] availChars = new int [26];

        for(char c : chars.toCharArray()){
            availChars[c - 'a']++;
        }

        // System.out.println(Arrays.toString(availChars));
        
        int count = 0;
        for(String word : words){
            int [] copy = availChars.clone();
            
            if(checkWord(copy, word)){
                count += word.length();
            }
            
            // System.out.println(Arrays.toString(availChars) + " : " + word);
            
        }

        return count;

    }

    public boolean checkWord(int [] availChars, String word){

        for(int i = 0; i< word.length(); i++){

            int idx = word.charAt(i) - 'a';
            
            if(availChars[idx] == 0){
                return false;
            }else 
                availChars[idx]-- ;
        }

        return true;
    }
}