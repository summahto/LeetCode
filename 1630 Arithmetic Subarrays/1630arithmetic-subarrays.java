class Solution {
    public List<Boolean> checkArithmeticSubarrays(int[] nums, int[] l, int[] r) {
        
        List<Boolean> ans = new ArrayList<>();

        for(int i= 0 ; i< l.length; i++){
            // int li = l[i], ri = r[i];
            
            int [] sub = Arrays.copyOfRange(nums, l[i], r[i]+1);
            // System.out.println(Arrays.toString(sub));
            
            ans.add(checkWithoutSorting(sub));

        }

        return ans;

    }

    // public boolean check(int [] sub){
    //     Arrays.sort(sub);
    //     // System.out.println(Arrays.toString(sub));            
    //     int prevCd = sub[1] - sub[0];

    //     // boolean isAdded = false;
    //     for(int j=2; j< sub.length; j++){

    //         if(prevCd != sub[j] - sub[j-1]) 
    //             return false;
            
    //     }
        
    //     return true;
        
    // }

    public boolean checkWithoutSorting(int [] sub){

        int min = Integer.MAX_VALUE;
        int max = Integer.MIN_VALUE;
        Set<Integer> set = new HashSet<>();

        for(int n : sub){
            min = Math.min(min, n);
            max = Math.max(max, n);
            set.add(n);
        }

        if((max - min) % (sub.length -1) != 0)
            return false;
        
        int diff = (max - min)/ (sub.length -1);
        int curr = min + diff;

        // curr <= max will cause the loop to go into infinite loop if all the numbers are same in it
        // eg. [0, 0, 0 ,0] , so think about it.
        while(curr < max){
            if(!set.contains(curr))
                return false;
            
            curr += diff;
        }

        return true;
    }
}