class Solution {
    public int missingNumber(int[] nums) {

        int i =0;
        while(i < nums.length){
            
            int correct = nums[i];
            if(nums[i] < nums.length && nums[correct] != nums[i]){
                int temp = nums[i];
                nums[i] = nums[correct];
                nums[correct] = temp;
            } else 
                i++;
        }

        for(int j=0 ; j< nums.length ; j++){
            if(j != nums[j])
                return j;
        }

        return nums.length;

    }
}