class Solution {
    public int[] getSumAbsoluteDifferences(int[] nums) {
        
        // Map<String, Integer> diffMap = new HashMap<>();
        int n = nums.length ;
        int [] res = new int[n];
        // int [] prefix = new int [n];

        // prefix[0] = nums[0];
        int sum = 0;
        for(int i = 0; i< n ; i++){
            // prefix[i] = prefix[i -1] + nums[i];
            sum += nums[i];
        }

        // System.out.println(Arrays.toString(prefix));
        int leftSum = 0;
        
        for(int i = 0; i< n ; i++) {
            
            // int leftSum = prefix[i] - nums[i];
            int rightSum = sum - leftSum - nums[i];

            int leftCount = i;
            int rightCount = n - i -1;

            int leftTotal = (nums[i] * leftCount) - leftSum;
            int rightTotal = rightSum - (nums[i] * rightCount) ;

            res[i] = leftTotal + rightTotal;
            leftSum += nums[i];

        }

        // res[i] = total  

        return res;
    }
}