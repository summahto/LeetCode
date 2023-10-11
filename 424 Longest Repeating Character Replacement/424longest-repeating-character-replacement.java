class Solution {
    public int characterReplacement(String s, int k) {
        
        
        int start = 0, end = 0;
        int maxCount = 0;
//        int otherCharsCount = 0;
        int maxLength = 0;
        int [] count = new int[26];
//        int i = 0;
//      0 1 2 3 4 5 6
//      A A B A B B A - this test case
        while (end < s.length()){
//            System.out.println("--------");
//            System.out.println("iteration " + (++i));


            count[s.charAt(end) - 'A']++;
            maxCount = Math.max(maxCount, count[s.charAt(end) - 'A']);


            if( (end - start + 1) <= (maxCount + k) ){
                maxLength = Math.max(maxLength, end - start +1);


            } else {
                count[s.charAt(start) - 'A']--;
                start++;
            }

            end++;
        }
        return end -start;
    }
}