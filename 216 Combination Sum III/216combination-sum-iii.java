class Solution {
    public List<List<Integer>> combinationSum3(int k, int n) {
        int [] nums = {1,2,3,4,5,6,7,8,9};

        List<List<Integer>> outer = new ArrayList<>();
        backtrack(outer, new ArrayList<>(), nums, 0, 0, k, n);
        return outer;
    }

    private void backtrack(List<List<Integer>> outer, List<Integer> inner, int [] nums, int sum, int start, int k, int n) {

        if(sum > n || inner.size() > k){
            return;

        } else if(inner.size() == k && sum == n){
            outer.add(new ArrayList<>(inner));
            return;

        } else if(inner.size() < k && sum < n){

            for(int i = start; i< nums.length ; i++){

                inner.add(nums[i]);

                backtrack(outer, inner, nums, sum + nums[i], i+1, k, n);
                inner.remove(inner.size() -1);
            }

        }
            
    }
}