class Solution {
    public int garbageCollection(String[] garbage, int[] travel) {
        
        int sum = 0, i = 0;
        int gc=0, pc = 0, mc =0, g =0, p = 0, m= 0;
        
        // Map<Character, List<Pair<Integer, Integer>>> gMap = new HashMap<>();
        for(int j =1 ; j< travel.length; j++){
            travel[j] += travel[j-1];
        }

        while(i < garbage.length){

            char [] carr = garbage[i].toCharArray();

            for(int j=0; j< carr.length; j++){

                if(carr[j] == 'G'){
                    gc++;
                    if(i > 0)
                        g = travel[i-1];

                }
                
                if(carr[j] == 'P'){
                    pc++;
                    if(i > 0)
                        p = travel[i-1];

                }

                if(carr[j] == 'M'){
                    mc++;
                    if(i > 0)
                        m = travel[i-1];

                }
                
            }
            i++;
        }

        return g + p + m + gc + pc + mc;

    }
}