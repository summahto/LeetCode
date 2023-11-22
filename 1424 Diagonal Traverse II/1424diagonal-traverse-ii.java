class Solution {
    public int[] findDiagonalOrder(List<List<Integer>> nums) {
        
        int c = 0;
        Map<Integer, List<Integer>> rowMap = new HashMap<>();
        // int maxCols = maxColumnSize(nums);

        // int j = 0;
        boolean found = true;

        for(int i= nums.size() -1; i >= 0 ; i-- ){

            for(int j = 0 ; j< nums.get(i).size(); j++){
                rowMap.computeIfAbsent(i+j, (key) -> new ArrayList<>()).add(nums.get(i).get(j));
                c++;

            }
        }            
                    

        // System.out.println(rowMap);
        
        int res [] = new int[c];
        int idx = 0;
        int curr = 0;
        while(rowMap.containsKey(curr)){
            for(int num : rowMap.get(curr)){
                res[idx++] = num;
            }
            curr++;
        }
        
        return res;

    }

}   