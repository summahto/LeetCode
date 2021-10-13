class Solution {
    public boolean canConstruct(String ransomNote, String magazine) {
        
        int count [] = new int[26];
        
        for(int i=0 ; i< ransomNote.length() ; i++){
            count[ransomNote.charAt(i) - 'a']++;
        }
        
        for(int i=0 ; i< magazine.length(); i++){
            count[magazine.charAt(i)- 'a']--;
        }
        
        // for(int j : count)
        //     System.out.print(j + " ");
        
        for(int i: count){
            if(i >= 1){
                return false;
            }
        }
        
        return true;
            
    }
}