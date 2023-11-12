class Solution {
    public boolean checkInclusion(String s1, String s2) {
        
        if(s1.length() > s2.length())
            return false;

        int i = 0, j = 0;
        int [] result = new int[26];
        int [] current = new int[26];

        for(int k =0 ; k< s1.length(); k++){
            result[s1.charAt(k) - 'a']++;
        }

        while (j < s2.length()){

            while(j < s1.length()){
                current[s2.charAt(j) - 'a']++;
                j++;
            }
            
            if(Arrays.equals(result, current)){
                return true;
            }
            else {
                current[s2.charAt(i) - 'a']--;
                i++;
                if(j < s2.length()) 
                    current[s2.charAt(j) - 'a']++;
                j++;
            }

        }

        if(Arrays.equals(result, current))
            return true;

        return false;
    }
}