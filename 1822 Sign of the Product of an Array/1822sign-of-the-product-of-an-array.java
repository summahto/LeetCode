class Solution {
    public int arraySign(int[] nums) {
        
        
        int i = 0;
        int prod = 1;
        while(i < nums.length){
            if(nums[i] < 0)
                prod = prod * (-1) ;
            else if(nums[i] == 0)
                return 0;

            i++;
            
        }

        return prod;


    }
}