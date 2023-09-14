class Solution {
    public int lastStoneWeight(int[] stones) {

        if(stones.length == 1)
            return stones[0];
        
        PriorityQueue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder());

        for(int stone : stones){
            pq.offer(stone);

        }

        while(pq.size() > 1){
        
            int s1 = pq.remove();
            int s2 = pq.remove();

            if(Math.abs(s1 - s2) > 0){
                pq.offer(Math.abs (s1- s2));
            }

        }

        return pq.size() == 1 ? pq.peek() : 0;
    }
}