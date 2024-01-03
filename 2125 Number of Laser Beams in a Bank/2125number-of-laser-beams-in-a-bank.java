class Solution {
    public int numberOfBeams(String[] bank) {
        
        String prev = bank[0];

        int prevCount = 0;
        for(int j=0; j< prev.length(); j++){
            
            if(prev.charAt(j) == '1')
                prevCount++;
        }


        int total = 0;
        for(int i=1; i< bank.length ; i++){
            String curr = bank[i];

            int currCount = 0;
            for(int k=0; k < curr.length(); k++){
                if(curr.charAt(k) == '1')
                    currCount++;
            }

            if(currCount == 0)
                continue;

            total += (prevCount * currCount);
            prevCount = currCount;

        }

        return total;

    }
}