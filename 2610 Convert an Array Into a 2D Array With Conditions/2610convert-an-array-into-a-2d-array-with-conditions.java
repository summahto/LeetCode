class Solution {
    public List<List<Integer>> findMatrix(int[] nums) {
        
        Map<Integer, Integer> freqMap = new HashMap<>();
        List<List<Integer>> ans = new ArrayList<>();

        for(int n : nums){

            int row = freqMap.getOrDefault(n, 0);
            // System.out.println(row);

            if( row ==  ans.size()) {
                ans.add(new ArrayList<>());
            }

            ans.get(row).add(n);
            
            freqMap.put(n , freqMap.getOrDefault(n, 0)+ 1);

        }
        
        return ans;
    }
}