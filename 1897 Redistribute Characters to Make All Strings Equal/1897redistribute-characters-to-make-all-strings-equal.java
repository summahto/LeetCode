class Solution {
    public boolean makeEqual(String[] words) {
        
        int n = words.length, total = 0;

        if (n == 1)
            return true;

        int [] charCount = new int [26];

        for(String word : words){
            
            char [] arr = word.toCharArray();
            total += arr.length;

            for(int i =0 ; i< arr.length ; i++){
                charCount[arr[i] - 'a']++;

            }
        }

        // System.out.println("total : " + total + ", charCount : " + Arrays.toString(charCount));

        if(total % n != 0)
            return false;

        for(int i=0; i< 26; i++){
            if(!(charCount[i] % n == 0)){
                return false;
            }
        }

        return true;
    }
}