class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        
        if(nums.length == 1 ) return new int []{ nums [0]};

        Map<Integer, Integer> countMap = new HashMap<>();

        for(int n : nums){
            if(!countMap.containsKey(n))
                countMap.put(n, 1);
            else
                countMap.put(n, countMap.get(n) + 1);
        }

        List<Map.Entry<Integer, Integer>> list = new ArrayList<>(countMap.entrySet());
        list.sort(Map.Entry.comparingByValue(Comparator.reverseOrder()));

        int [] res = new int[k];


        for(int i = 0; i< k; i++){
            res[i] = list.get(i).getKey();
        }

        return res;
    }
}