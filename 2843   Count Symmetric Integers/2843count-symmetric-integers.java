class Solution {
    public int countSymmetricIntegers(int low, int high) {
        
        int i = low, total = 0;
        while(i <= high){
            
            int digits = 0, num = i;
            while(num != 0 ){
                digits++;
                num /= 10;
            }
            
            // System.out.println(i + " : " + digits);
            
            if(digits %2 == 0){
                String str = Integer.toString(i);
                // char[] arr = new char [str.length];
                
                int s = 0, e = str.length() - 1, lSum = 0, rSum = 0;
                // boolean isSym = true;
                while(s < e){
                    lSum += Character.getNumericValue(str.charAt(s++));
                    rSum += Character.getNumericValue(str.charAt(e--));
                    
                    
                }
                
                // System.out.println(i + " : " + lSum + " : " + rSum);
                
                if(lSum == rSum){
                    
                    total++;
                }
                    
            }
            
            
            
            i++;
            
        }
        
        return total;
    }
}