class Solution {
    public int maximumElementAfterDecrementingAndRearranging(int[] arr) {

        Arrays.sort(arr);
        
        // System.out.println(Arrays.toString(arr));
        int prev = 0;

        // int i = 1;
        for(int n : arr) {
            prev = Math.min(prev+1, n);
        }

        return prev;   
    }
}