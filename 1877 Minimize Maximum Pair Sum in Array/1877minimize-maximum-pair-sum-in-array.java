class Solution {
    public int minPairSum(int[] nums) {
        
        int maxSum = 0, pSum = 0;
        Arrays.sort(nums);
        
        int i = 0, j = nums.length -1;
        
        while(i < j){
            pSum = nums[i] + nums[j];
            maxSum = Math.max(maxSum, pSum);

            i++;
            j--;
        }

        return maxSum;
    }
}