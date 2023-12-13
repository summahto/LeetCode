class Solution {
    public int numSpecial(int[][] mat) {
        int m = mat.length;
        int n = mat[0].length, ans =0;
        int [] rowCount = new int[m];
        int [] colCount = new int[n];

        for(int i=0; i<m; i++){
            for(int j=0; j< n; j++){
                if(mat[i][j] == 1){

                    rowCount[i]++;
                    colCount[j]++;
                }
            }
        }

        // System.out.println(Arrays.toString(rowCount));
        // System.out.println(Arrays.toString(colCount));

        for(int i=0; i<m; i++){
            for(int j=0; j< n; j++){
                if(mat[i][j] == 1){
                    if(rowCount[i]== 1 && colCount[j] == 1)
                        ans++;
                }
                
            }
        }
        
        return ans;


        //My solution : One mistake,did not use indices preoperly
        // Map<String, Integer> rcData = new HashMap<>();

        // int spCount = 0;
        
        // for(int i= 0 ; i< mat.length; i++){
            
        //     int rSum = 0;
        //     for(int j= 0; j< mat[i].length ; j++){
        //         rSum+= mat[i][j];
        //     }

        //     rcData.put("i:" + String.valueOf(i), rSum);
        // }

        
        // for(int j= 0 ; j< mat[0].length; j++){
            
        //     int cSum = 0;
        //     for(int i= 0; i< mat.length ; i++){
        //         cSum += mat[i][j];
        //     }
        //     rcData.put("j:" + String.valueOf(j), cSum);
        // }

        // for(int i= 0 ; i< mat.length; i++){
            
        //     for(int j= 0; j< mat[i].length ; j++){
        //         if(mat[i][j] == 1){
                    
        //             if(rcData.get("j:" + String.valueOf(j)) == 1 && rcData.get("i:" + String.valueOf(i)) == 1)
        //                 spCount++;
        //         }
            
        //     }

        // }

        // return spCount;

    }
}