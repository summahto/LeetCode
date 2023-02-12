class Solution {
    public int[] maxSlidingWindow(int[] nums, int k) {
        
        int i = 0, j = 0;
        Deque<Integer> dq = new ArrayDeque<>();
        int [] ans = new int[nums.length- k +1];

        while(i < nums.length){

            while(!dq.isEmpty() && (i-k+1) > dq.peek()){
                dq.poll();
            }

            while (!dq.isEmpty() && nums[i] > nums[dq.peekLast()]){
                dq.pollLast();
            }

            dq.offer(i);

            if( i >= k-1){
                ans[j++] = nums[dq.peek()];
            }

            i++;

        }

        return ans;
    }
}