class Solution {
    public int maxProductDifference(int[] nums) {

        int n = nums.length;
        int max1 = 0, max2 = 0;
        int min1 = Integer.MAX_VALUE, min2 = Integer.MAX_VALUE;
        
        for(int i = 0; i< n ; i++){
            
            if(nums[i] > max1){
                max2 = max1;
                max1 = nums[i] ;

            }else
                max2 = Math.max(max2, nums[i]);
            
            if(nums[i] < min1){
                min2 = min1;
                min1 = nums[i] ;
            }
            else
                min2 = Math.min(min2, nums[i]);


        }
        // System.out.println(max1 + "  " + max2 + " " + min1 + " " + min2);

        return (max2 * max1) - (min2 * min1); 
    }
}