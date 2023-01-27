import java.util.AbstractMap;

class MinStack {

    private Stack<AbstractMap.SimpleEntry<Integer, Integer>> minStack;
    
    public MinStack() {
        minStack = new Stack<>();
    }

    public void push(int val) {
        int minSoFar ;

        if(minStack.isEmpty()){
            minSoFar = val;
        }else {
            minSoFar = this.getMin();
            if(val < minSoFar)
                minSoFar = val;
        }
        minStack.push(new AbstractMap.SimpleEntry<>(val, minSoFar));
    }

    public void pop() {
        minStack.pop();
    }

    public int top() {
        return minStack.peek().getKey();
    }

    public int getMin() {
        return minStack.peek().getValue();
    }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.push(val);
 * obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.getMin();
 */