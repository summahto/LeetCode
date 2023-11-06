class SeatManager {

    boolean [] seatStatus ;
    PriorityQueue<Integer> pq;

    public SeatManager(int n) {
        seatStatus = new boolean[n] ;
        pq = new PriorityQueue<>();

        int i= 1;
        while(i <= n){
            pq.offer(i++);
        }
    }
    
    public int reserve() {

        //take out the samallest seat number available and set it to true
        int seat = pq.poll();
        seatStatus[seat -1] = true;

        return seat;
        
    }
    
    public void unreserve(int seatNumber) {

        //set the given seatNumber to false and then add that available seat to the queue
        seatStatus[seatNumber -1] = false;
        pq.offer(seatNumber);
    }
}

/**
 * Your SeatManager object will be instantiated and called as such:
 * SeatManager obj = new SeatManager(n);
 * int param_1 = obj.reserve();
 * obj.unreserve(seatNumber);
 */