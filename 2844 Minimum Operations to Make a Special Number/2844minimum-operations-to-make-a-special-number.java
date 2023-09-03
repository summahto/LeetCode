class Solution {
    public int minimumOperations(String num) {
        
        Map<Character, Integer> map = new HashMap<>();
        int e = num.length() -1;
        int i = -1, j = -1, k = -1;

        while(e >= 0){
            char c = num.charAt(e);
            
            if(map.containsKey(c)){
                i = e;
                j = map.get(num.charAt(e));
                break;
                
            }else {
                if(c == '0' || c == '5'){
                    if(c == '0'){
                        k = e;
                        map.put('5', e);
                        map.put('0', e);
                        
                    } else {
                        map.put('7', e);
                        map.put('2', e);
                        
                    }
                        
                }    
            }
            
            // System.out.println(c + " :" + map);
            
            e-- ;
            
        }

        if(i == -1 && j == -1 && k != -1){
            return num.length() - 1; 
        }

        if(i == -1 && j == -1){
            return num.length(); 
        }
        

        return num.length() - i - 2;
        
        
//         for(int k = i+1; k < num.length() ; k++ ){
//             if(k!= j){
                
//             }
//         }
        
        
        
    }
}