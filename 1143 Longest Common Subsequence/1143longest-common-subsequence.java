class Solution {
    public int longestCommonSubsequence(String text1, String text2) {
        int m = text1.length();
        int n = text2.length();
        Integer [][] memo = new Integer[m+1][n+1];
        
        return helper(text1, text2, m, n, memo);
    }
    
    public int helper(String x, String y, int m, int n, Integer memo[][] ){
        
        if(m == 0 || n == 0)
            return 0;
        
        if(memo[m][n] != null)
            return memo[m][n];
        
        if(x.charAt(m-1) == y.charAt(n-1))
            return memo[m][n] = 1+ helper(x, y, m-1, n-1, memo);
        else
            return memo[m][n] = Math.max(helper(x, y, m, n-1, memo), 
                                        helper(x, y, m-1, n, memo));
    }
}