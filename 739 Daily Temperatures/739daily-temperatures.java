class Solution {
    public int[] dailyTemperatures(int[] temperatures) {
        
        int [] days = new int[temperatures.length];
        int i = temperatures.length -1;
        Deque<Integer> s = new ArrayDeque<>();

        while(i >= 0){

            while(!s.isEmpty() && temperatures[i] >= temperatures[s.peek()])
                s.pop();
            
            if(!s.isEmpty()){
                if(temperatures[i] < temperatures[s.peek()])
                    days[i] = s.peek() - i;
            }

            s.push(i--);

        }

        return days;

    }
}