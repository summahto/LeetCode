class Solution {
    public String maxValue(String n, int x) {
        boolean isNegative = false;
        StringBuilder sb = new StringBuilder(n);
        if(n.startsWith("-")){
            isNegative = true;
        }
        
        for(int i=0 ; i< n.length() ; i++){
            int cur = n.charAt(i) - '0';
            if(!isNegative && x > cur || ( i>0 && isNegative && x< cur )){
                sb.insert(i, String.valueOf(x));
                return sb.toString();
            }
            
        }
        return sb.append(String.valueOf(x)).toString();
        
    }
}