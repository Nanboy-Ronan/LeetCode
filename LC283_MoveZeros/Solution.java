class Solution {
    // Two Pointers
    // Time Complexity: O(n)
    // Space Complexity: O(1)
    public void moveZeroes(int[] nums) {
        int i = 0;
        int j = 0;
        while(i < nums.length){
            if(nums[i] == 0){
                i++;
                continue;
            }else{
                nums[j] = nums[i];
                i++;
                j++;
            }
        }
        for(i = j; i < nums.length; i++){
            nums[i] = 0;
        }
    }
}