class Solution {
    public int countSubstrings(String s) {
        
        int total = 0, n = s.length();
        boolean dp [] [] = new boolean [n][n];

        for(int i=0; i<n; i++){

            dp[i][i] = true;
            total++;
        }

        for(int i=0; i+1<n ; i++){

            if(s.charAt(i) == s.charAt(i+1)){
                dp[i][i+1] = true;
                total++;
            }
        }

        for(int diff = 2; diff< n; diff++){

            for(int i=0 ; i< n - diff; i++){

                int j = i+ diff;

                if(dp[i+1][j-1] && s.charAt(i) == s.charAt(j)){
                    dp[i][j] = true;
                    total++;
                }
            }
        }

        return total;
    }
}