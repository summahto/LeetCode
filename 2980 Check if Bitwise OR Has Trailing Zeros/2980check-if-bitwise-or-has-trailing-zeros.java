class Solution {
    public boolean hasTrailingZeros(int[] nums) {
        
        int n = nums.length, count = 0;
        
        for(int num: nums){
            if(num % 2 == 0)
                count++;
            
            if(count >= 2)
                return true;
        }
        
        return false;
    }
}