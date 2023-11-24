class Solution {
    public int maxCoins(int[] piles) {
        
        Arrays.sort(piles);
        int n = piles.length/3, sum = 0;
        
        int i = piles.length -2;

        while(n > 0 && i >= 0) {
            sum += piles[i];
            i-= 2;
            n--;
        }

        return sum;
    }
}