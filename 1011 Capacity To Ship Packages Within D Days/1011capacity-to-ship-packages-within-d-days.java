class Solution {
    public int shipWithinDays(int[] weights, int days) {
        int minCap = Integer.MIN_VALUE;
        int maxCap = 0;

        for(int w : weights){
            minCap = Math.max(minCap, w);
            maxCap += w;
        }

        int low = minCap, high = maxCap, res = 0;
        //applying binary search on the sample space

        while(low < high){
            
            int mid = low + (high - low)/2;
            int sum = 0, currDays = 0;

            for(int i = 0; i< weights.length ; i++){
                if(sum + weights[i] > mid) {
                    currDays++;
                    sum = 0;

                }
                sum += weights[i];

            // System.out.println("sum : " + sum + " current days : "+ currDays);
            }

            if(sum > 0)
                currDays++;
            // System.out.println("sum : " + sum + " current days : "+ currDays);

            if(currDays > days){
                // res = high;
                low = mid + 1;
            } else {
                high = mid;
            }
        }

        return low;
    }
}