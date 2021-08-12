class Solution {
    public int removeDuplicates(int[] nums) {
        if(nums == null || nums.length == 0)
            return 0;
        int n = nums.length;
        int i=0, j=1;
        while(j <n ){
            
            if(nums[j] != nums[i]){
                i++;
                nums[i] = nums[j];
            }
            else 
                j++;
        }
        return i+1;
    }
}