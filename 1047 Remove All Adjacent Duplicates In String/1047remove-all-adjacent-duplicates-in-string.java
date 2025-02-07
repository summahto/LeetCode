class Solution {
    public String removeDuplicates(String s) {
        
        int i = 0, n = s.length();
        char [] result = s.toCharArray();
        
        for(int j = 0; j<n ; j++, i++){
            result[i] = result[j];
            
            if(i>0 && result[i-1] == result[i]) {
                i = i-2;
            }
        }
        
        return new String(result, 0, i);
    }
}