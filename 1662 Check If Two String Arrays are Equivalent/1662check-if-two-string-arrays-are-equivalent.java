class Solution {
    public boolean arrayStringsAreEqual(String[] word1, String[] word2) {
        
        int i = 0, m = 0;
        int j = 0, n = 0;

        while(i < word1.length && m < word2.length){

            if(word1[i].charAt(j) != word2[m].charAt(n))
                return false;

            j++;
            n++;

            if(j == word1[i].length()){
                i++;
                j = 0;
            }
            
            if(n == word2[m].length()){
                m++;
                n = 0;
            }

        }

        // System.out.println(i + " : " + j + " : " + m + " : " + n);
        

        if(i < word1.length){
            // if(j < word1[i].length())
                return false;
        }

        if(m < word2.length){
            // if(n < word2[m].length())
                return false;
        }

        return true;


    }


}