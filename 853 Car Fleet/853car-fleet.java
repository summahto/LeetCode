class Solution {
    public int carFleet(int target, int[] position, int[] speed) {

        Map<Integer, Double> map = new TreeMap<>(Collections.reverseOrder());

        for(int i=0 ; i< position.length ; i++){
            map.put(position[i], (double)(target - position[i]) / speed[i]);
        }

        int res = 0;
        double cur = 0;

        for(Double time : map.values()){
            if(time > cur){
                cur = time;
                res++;
            }
        }

        return res;
    }

    
}