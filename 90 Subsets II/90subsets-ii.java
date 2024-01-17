class Solution {
    public List<List<Integer>> subsetsWithDup(int[] nums) {
        
        // Set<List<Integer>> used = new HashSet<>(); 
        List<List<Integer>> outer = new ArrayList<>();
        Arrays.sort(nums);
        backtrack(outer, new ArrayList<>(), nums, 0);
        return outer;

    }


    private void backtrack(List<List<Integer>> outer, List<Integer> inner, int [] nums, int start) {

        
        outer.add(new ArrayList<>(inner));
            // used.add(new ArrayList<>(inner));   

        
        for(int i = start; i< nums.length; i++){
            
            if(start != i && nums[i] == nums[i-1]) continue;
            
            inner.add(nums[i]);
            
            backtrack(outer, inner, nums, i+1);
            inner.remove(inner.size() - 1);
        }
    }
}