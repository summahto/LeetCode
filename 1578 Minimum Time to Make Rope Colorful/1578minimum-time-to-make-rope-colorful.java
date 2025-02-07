class Solution {
    public int minCost(String s, int[] cost) {
        int max_cost = 0, sum_cost = 0, res = 0, n = s.length();
        
        for(int i = 0 ; i < n; i++){
            
            if(i > 0 && s.charAt(i) != s.charAt(i-1)){
                res+= sum_cost - max_cost;
                sum_cost = max_cost = 0;
            }
            
            sum_cost += cost[i];
            max_cost = Math.max(max_cost, cost[i]);
        }
        
        res+= sum_cost - max_cost;
        return res;
    }
}