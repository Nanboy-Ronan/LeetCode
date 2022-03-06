
var MinStack = function() {
    this.stack = []
    this.minStack = []
};

/** 
 * @param {number} val
 * @return {void}
 */
MinStack.prototype.push = function(val) {
    // Time Complexity: O(1)
    this.stack.push(val)
    if(this.minStack.length === 0 || this.minStack[this.minStack.length-1] >= val){
        this.minStack.push(val)
    }
};

/**
 * @return {void}
 */
MinStack.prototype.pop = function() {
    // Time Complexity: O(1)
    let retVal = this.stack.pop()
    if(retVal === this.minStack[this.minStack.length-1]){
        this.minStack.pop()
    }
    return retVal
};

/**
 * @return {number}
 */
MinStack.prototype.top = function() {
    // Time Complexity: O(1)
    return this.stack[this.stack.length-1]
};

/**
 * @return {number}
 */
MinStack.prototype.getMin = function() {
    // Time Complexity: O(1)
    return this.minStack[this.minStack.length-1]
};

/** 
 * Your MinStack object will be instantiated and called as such:
 * var obj = new MinStack()
 * obj.push(val)
 * obj.pop()
 * var param_3 = obj.top()
 * var param_4 = obj.getMin()
 */