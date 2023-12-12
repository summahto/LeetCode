class Solution {
    public int maxProduct(int[] nums) {
        
        int h1= 0, h2 =0, i =0;

        while(i < nums.length) {
            if (nums[i] >= h1){
                h2 = h1;
                h1 = nums[i];
                i++;
                continue;
            }

            if( nums[i] > h2){
                h2 = nums[i];
            }
            i++;
        }

        // System.out.println(h1 + " : " + h2);

        return (h1-1)* (h2 -1);

    }
}