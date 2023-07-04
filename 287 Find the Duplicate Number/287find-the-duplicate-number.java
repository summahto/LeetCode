class Solution {
    public int findDuplicate(int[] nums) {
        
        int slow = 0, fast = 0;
        while(fast < nums.length){
            slow = nums[slow];
            fast = nums[nums[fast]];

            if(slow == fast){
                slow = 0;
                
                while(slow != fast){
                    slow = nums[slow];
                    fast = nums[fast];

                }

                if(slow == fast)
                    return slow;
            }
        }

        return slow;

    }
}