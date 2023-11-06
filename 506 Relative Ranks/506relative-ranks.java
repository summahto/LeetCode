class Solution {
    public String[] findRelativeRanks(int[] score) {

        String [] ans = new String [score.length];
        PriorityQueue<Pair<Integer, Integer>> pq = new PriorityQueue<>((a, b) -> b.getKey() - a.getKey());

        for(int i=0 ; i<score.length ; i++){
            pq.offer(new Pair<>(score[i], i));
        }

        int i =1;
        
        while(!pq.isEmpty()){
            Pair<Integer, Integer> p = pq.poll();

            if(i == 1){
                ans[p.getValue()] = "Gold Medal";
            } 
            else if(i == 2){
                ans[p.getValue()] = "Silver Medal";
            } 
            else if(i == 3){
                ans[p.getValue()] = "Bronze Medal";

            } else {
                ans[p.getValue()] = String.valueOf(i);
            }
            
            i++;
        }

        return ans;
    }
}