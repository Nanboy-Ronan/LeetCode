/*
Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).

Implement the MyQueue class:

void push(int x) Pushes element x to the back of the queue.
int pop() Removes the element from the front of the queue and returns it.
int peek() Returns the element at the front of the queue.
boolean empty() Returns true if the queue is empty, false otherwise.
*/
var MyQueue = function() {
    this.in = []
    this.out = []
};

/** 
 * @param {number} x
 * @return {void}
 */
MyQueue.prototype.push = function(x) {
    // Time Complexity: O(1)
    this.in.push(x)
};

/**
 * @return {number}
 */
MyQueue.prototype.pop = function() {
    // Time Complexity: O(n)
    if(this.out.length === 0){
        while(this.in.length){
            temp = this.in.pop()
            this.out.push(temp)
        }
    }
    return this.out.pop()
};

/**
 * @return {number}
 */
MyQueue.prototype.peek = function() {
    // Time Complexity: O(n)
    if(this.out.length === 0){
        while(this.in.length){
            temp = this.in.pop()
            this.out.push(temp)
        }
    }
    return this.out[this.out.length - 1]
};

/**
 * @return {boolean}
 */
MyQueue.prototype.empty = function() {
    // Time Complexity: O(1)
    return !this.in.length && !this.out.length
};

/** 
 * Your MyQueue object will be instantiated and called as such:
 * var obj = new MyQueue()
 * obj.push(x)
 * var param_2 = obj.pop()
 * var param_3 = obj.peek()
 * var param_4 = obj.empty()
 */