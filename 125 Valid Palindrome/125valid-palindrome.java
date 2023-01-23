class Solution {
    public boolean isPalindrome(String s) {
        
        String str = s.toLowerCase();
        // str.strip();

//        System.out.println(str);
//        System.out.println(str.length());

        int i = 0, j = s.length()-1;
//        int i = mid, j = mid;
//        Cannot use this approach because the mid is not guaranteed to be a valid character
        while(i <= j){
            // System.out.println("i= " + str.charAt(i) + " j = " + str.charAt(j));


            if(!Character.isLetterOrDigit(str.charAt(i))) {
                i++;
                continue;
            }

            if(!Character.isLetterOrDigit(str.charAt(j))) {
                j--;
                continue;
            }

            if(str.charAt(i) != str.charAt(j)) {
                return false;
            }

            i++;
            j--;
        }

        return true;
    
    }
}