class Solution {
    public String minWindow(String s, String t) {
        
        if(t.length() > s.length() || s.length() ==0 || t.length() == 0)
            return "";
        

        int start = 0, end = 0, minLength = Integer.MAX_VALUE, validStart = 0;
        int [] countTracker = new int[128];

        //initialized with the characters of t and it's char count
        for(int i = 0; i< t.length(); i++){
            countTracker[t.charAt(i)]++;
        }

        int count = t.length(); //track the number of chars in t

        while (end < s.length()) {
            //if the character in t exists in s then reduce it's count
            if (countTracker[s.charAt(end)] > 0)
                count--;

            //reduce the count of character everytime, if it exists in t count for that char will be 0, else -ve
            countTracker[s.charAt(end)]--;
            end++;

            //if all the chars in t are present in s, then record the minLength
            while (count == 0) {
                if(minLength > end - start){
                    minLength = end - start;
                    validStart = start;  // update the start only if the minimumLength was found, NOT always
//                    System.out.println("Current  Min Substring  : " + s.substring(validStart, validStart+ minLength));
                }
                
                countTracker[s.charAt(start)]++;

                if (countTracker[s.charAt(start)] > 0)
                    count++;

                start++;

            }
        }

        if(minLength != Integer.MAX_VALUE)
            return s.substring(validStart, validStart + minLength);

        return "";

        
    }
}