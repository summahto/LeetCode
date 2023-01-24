class Solution {
    public int maxSubArray(int[] nums) {

        if(nums.length == 1)
            return nums[0];

        int maxSumEndingAtI = 0, gMaxSum = Integer.MIN_VALUE;

        int i = 0;
        while(i < nums.length){

            maxSumEndingAtI = Math.max(maxSumEndingAtI + nums[i], nums[i]);
            gMaxSum = Math.max(gMaxSum, maxSumEndingAtI);

            // System.out.println(maxSumEndingAtI + " " + gMaxSum);
            i++;
        }


        return gMaxSum;
    }
}