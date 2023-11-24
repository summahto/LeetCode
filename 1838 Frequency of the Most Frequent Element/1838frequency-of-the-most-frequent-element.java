class Solution {
    public int maxFrequency(int[] nums, int k) {
        
        Arrays.sort(nums);
        int l = 0, r =0 ;
        long total = 0 ;
        
        while(r < nums.length){
            
            total += nums[r];
            // this is the main condition you need to think of..
            // since the array is sorted rightmost num of windows will the max.
            
            if(nums[r]* (r-l +1) > total + k){

                total -= nums[l];
                l++;
                // System.out.println(l + " :" + r + ": " + (r -l +1));
                

            } 
            
            // maxf = Math.max(maxf, (r-l+1));
            r++;

            
        }

        return nums.length - l;

    }
}