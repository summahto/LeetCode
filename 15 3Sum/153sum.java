class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        
        Set<List<Integer>> superSet = new HashSet<>();
        Map<Integer, Integer> tripletMap = new HashMap<>();
        //{-1,0,1,2,-1,-4}
        Arrays.sort(nums);

        for(int i=0; i< nums.length -2; i++){
            int j = i+1, k = nums.length -1;

            while(j < k){

                if(nums[i] + nums[j] + nums[k] < 0){
                    j++;
                } else if (nums[i] + nums[j] + nums[k] > 0) {
                    k--;
                } else {
                    List<Integer> ans = new ArrayList<>();
                    ans.add(nums[i]);
                    ans.add(nums[j]);
                    ans.add(nums[k]);
                    superSet.add(ans);
                    j++;
                    k--;
                }

            }
        }

        return new ArrayList<>(superSet);
    }
}