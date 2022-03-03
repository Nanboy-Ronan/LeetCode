import java.util.Stack;

/*
Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).

Implement the MyQueue class:

void push(int x) Pushes element x to the back of the queue.
int pop() Removes the element from the front of the queue and returns it.
int peek() Returns the element at the front of the queue.
boolean empty() Returns true if the queue is empty, false otherwise.
*/

class MyQueue {
    private Stack<Integer> in;
    private Stack<Integer> out;

    public MyQueue() {
        this.in = new Stack<>();
        this.out = new Stack<>();
    }
    
    public void push(int x) {
        // Time Complexity: O(1)
        in.push(x);
    }
    
    public int pop() {
        // Time Complexity: O(n)
        inToOut();
        return out.pop();
    }
    
    public int peek() {
        // Time Complexity: O(n)
        inToOut();
        return out.peek();
    }
    
    public boolean empty() {
        return in.empty() && out.empty();
    }

    private void inToOut(){
        if(out.isEmpty()){
            while(!in.isEmpty()){
                int temp = in.pop();
                out.push(temp);
            }
        }
    }
}

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue obj = new MyQueue();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.peek();
 * boolean param_4 = obj.empty();
 */