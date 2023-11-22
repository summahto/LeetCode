class Solution {
    public int countNicePairs(int[] nums) {
        
        Map<Integer, Integer> countMap = new HashMap<>();
        long count = 0;
        for(int n : nums){
            int diff = n - reverse(n);
            countMap.put(diff, countMap.getOrDefault(diff, 0) + 1);
        }

        // countMap.entrySet().stream().

        for(Map.Entry<Integer, Integer> e: countMap.entrySet()){
            long numOfOcc = e.getValue();
            count += (numOfOcc * (numOfOcc -1))/2 ;
        }

        

        return (int)(count % (Math.pow(10, 9) + 7));
    }

    public int reverse(int n){
        int rev = 0, i = 0, numOfDigits = 0;
        // int copyOfN = n;
        // while(copyOfN > 0){
        //     numOfDigits++;
        //     copyOfN = copyOfN /10;
        // }

        while(n > 0){
            rev = rev * 10 + n % 10;
            n = n/10;
        }

        return rev;

    }
}