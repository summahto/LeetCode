class Solution {
    public int buyChoco(int[] prices, int money) {
        
        int min1 = Integer.MAX_VALUE;
        int min2 = Integer.MAX_VALUE;

        for(int i=0 ; i< prices.length; i++){

            if(prices[i] < min1){
                min2 = min1;
                min1 = prices[i];
            
            } else {
                min2 = Math.min(prices[i], min2);
            }
        }

        return money - (min1 + min2) >=0 ? money - (min1 + min2): money;
    }
}