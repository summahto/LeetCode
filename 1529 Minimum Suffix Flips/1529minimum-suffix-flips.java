class Solution {
    public int minFlips(String target) {
        
        int count = 0;
        if(target.charAt(0) == '1')
            count++;

        int i = 0;
        while(i < target.length() - 1){
            if(target.charAt(i) != target.charAt(i+1))
                count++;

            i++;
        }

        return count;
    }
}