class Solution {
    public List<String> buildArray(int[] target, int n) {

        Deque<Integer> stack = new ArrayDeque<>();
        int i = 0, j = 1, count = 0;
        List<String> operations = new ArrayList<>();

        do {
            // System.out.println(stack + " : " + count);
            
            if(target[i] == j) {

                while(count > 0){
                    stack.pop();
                    operations.add("Pop");
                    count--;
                }
            
                stack.push(j);
                operations.add("Push");
                i++;
                j++;

            } else{

                stack.push(j);
                operations.add("Push");
                count++;
                j++;
            }

            

        } while(stack.peek() != target[target.length -1]);

        return operations;
    }
}