/**
 * @param {number} x
 * @param {number} y
 * @return {number}
 */
 var hammingDistance = function(x, y) {
    // Bit Wise
    // Time Complexity: O(logx+logy)
    // Space Complexity: O(1)
    diff = x ^ y
    let result = 0
    while(diff){
        result += diff & 1
        diff >>>= 1
    }
    return result
};