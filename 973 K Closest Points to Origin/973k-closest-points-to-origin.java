class Solution {
    public int[][] kClosest(int[][] points, int k) {

        if(points.length == k)
            return points;

        
        int [][] ans = new int[k][2];
        PriorityQueue<Pair<Integer, int[]>> pq = new PriorityQueue<>(k, (p1, p2) -> p2.getKey() - p1.getKey());
        

        for(int [] point : points) {

            Integer dist = (point[0] * point[0]) + (point[1] * point[1]);
            // System.out.println(dist);

            if(pq.size() < k){
                pq.offer(new Pair(dist, point));

            } else {
                if( dist < pq.peek().getKey()){
                    pq.remove();
                    pq.offer(new Pair(dist, point));
                }

            }

            // System.out.println(pq);
        }

        for(int [] point : ans){
            int [] closestPoint = pq.remove().getValue();

            point[0] = closestPoint[0];
            point[1] = closestPoint[1];
        }

        return ans;

    }
}