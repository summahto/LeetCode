class Solution {
    public String sortVowels(String s) {
        
        PriorityQueue<Character> p = new PriorityQueue<>((a,b) -> (a - 'A') - (b - 'A'));
        char[] arr = s.toCharArray();
        
        for(char c : arr){
            if(c == 'a' || c == 'e' || c == 'i' || c== 'o' || c == 'u'
                || c == 'A' || c == 'E' || c == 'I' || c== 'O' || c == 'U') {

                    p.add(c);
                }
        }

        // System.out.println(p);

        for(int i=0 ; i< s.length() ; i++){
            if(arr[i] == 'a' || arr[i] == 'e' || arr[i] == 'i' || arr[i]== 'o' || arr[i] == 'u'
                || arr[i] == 'A' || arr[i] == 'E' || arr[i] == 'I' || arr[i]== 'O' || arr[i] == 'U'){

                    arr[i] = p.poll();
                }
        }

        return new String(arr);

    }
}