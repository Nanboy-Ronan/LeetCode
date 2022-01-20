class Solution {
    // Two Pointers (backward)
    // Time Complexity: O(m+n)
    // Space Complexity: O(1)
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int curr = nums1.length - 1;
        int nums1_index = m - 1;
        int nums2_index = n - 1;

        while(curr >= 0){
            if(nums1_index < 0){
                // nums1 ends, copy nums2 to the rest
                nums1[curr] = nums2[nums2_index--];
            }else if(nums2_index < 0){
                // nums2 ends, copy nums1 to the rest
                nums1[curr] = nums1[nums1_index--];
            }else if(nums1[nums1_index] >= nums2[nums2_index]){
                nums1[curr] = nums1[nums1_index--];
            }else{
                nums1[curr] = nums2[nums2_index--];
            }
            curr--;
        }
    }
}