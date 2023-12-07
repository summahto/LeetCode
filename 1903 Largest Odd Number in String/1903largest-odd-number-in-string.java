class Solution {
    public String largestOddNumber(String num) {

        int i = num.length() -1 ;        
        while(i >= 0){
            int digit = Integer.valueOf(num.charAt(i));
            if(digit %2 != 0){
                return num.substring(0, i+1);
            }

            i--;
        }

        return "";
    }
}