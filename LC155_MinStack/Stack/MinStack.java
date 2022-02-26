import java.util.Stack;

class MinStack {
    Stack<Integer> s;
    Stack<Integer> minS;

    public MinStack() {
        this.s = new Stack<>();
        this.minS = new Stack<>();
    }
    
    public void push(int val) {
        s.push(val);
        if(minS.isEmpty() || minS.peek() >= val) minS.push(val);       
    }
    
    public void pop() {
        int temp = s.pop();
        if(minS.peek() == temp) minS.pop();
    }
    
    public int top() {
        return s.peek();
    }
    
    public int getMin() {
        return minS.peek();
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