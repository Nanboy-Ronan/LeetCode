/**
 * @param {number[]} nums
 * @param {number} target
 * @return {boolean}
 */
 var search = function(nums, target) {
    var left = 0, right = nums.length - 1
    while(left <= right) {
        let mid = parseInt((left + right) / 2)
        if(nums[mid] === target){
            return true
        }

        if(nums[left] === nums[mid]){
            left++;
        }else if(nums[left] < nums[mid]){
            if(target >= nums[left] && target < nums[mid]){
                right = mid - 1
            }else{
                left = mid + 1
            }
        }else{
            if(target <= nums[right] && target > nums[mid]){
                left = mid + 1
            }else{
                right = mid - 1
            }
        }
    }

    return false
};