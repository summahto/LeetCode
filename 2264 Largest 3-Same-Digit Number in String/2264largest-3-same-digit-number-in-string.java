class Solution {
    public String largestGoodInteger(String num) {
        
        int i = 0, j =2;
        String max = "";
        // Set<Character> uniq = new HashSet<>();

        while(j < num.length()){

            StringBuilder sb = new StringBuilder();

            for(int k = i; k < j+1; k++) {
                
                if(k+1 < j+1){
                    if(num.charAt(k+1) != num.charAt(k))
                        break;
                }
                sb.append(num.charAt(k));
            }

            if(sb.length() == 3){
                if("".equals(max) || sb.charAt(0) > max.charAt(0))
                    max = sb.toString();

            }
            
            i++;
            j++;
        }

        return max;
    }
}