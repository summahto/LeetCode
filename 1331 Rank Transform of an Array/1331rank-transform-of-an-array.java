class Solution {
    public int[] arrayRankTransform(int[] arr) {
        
        TreeMap<Integer, List<Integer>> indexMap = new TreeMap<>();

        for(int i= 0; i< arr.length; i++){
             
            if(!indexMap.containsKey(arr[i])) {
                List<Integer> indexes = new ArrayList<>();
                indexes.add(i);
                indexMap.put(arr[i], indexes);

            } else {
                List<Integer> indexes = indexMap.get(arr[i]);
                indexes.add(i);
                indexMap.put(arr[i], indexes);
            }
        }

        int [] result = new int[arr.length];

        int n = indexMap.size();
        
        Iterator<Map.Entry<Integer, List<Integer>>> iter = indexMap.entrySet().iterator();
        
        int rank = 1;
        while (iter.hasNext()) {
            Map.Entry<Integer, List<Integer>> entry = iter.next();
            int mapKey = entry.getKey();
            List<Integer> indexList = entry.getValue();
            
            for(int index: indexList){
                result[index] = rank;
            }
            rank++;
        }

        return result;
    }
}