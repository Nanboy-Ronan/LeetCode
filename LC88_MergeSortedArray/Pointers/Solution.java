class Solution {
    // Two Pointers
    // Time Complexity: O(m+n)
    // Space Complexity: O(m+n)
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int[] temp = new int[m+n];
        int nums1_index = 0;
        int nums2_index = 0;

        for(int i = 0; i < m+n; i++){
            if(nums1_index == m){ // finish nums1, copy all nums2
                temp[i] = nums2[nums2_index++];
            }else if(nums2_index == n){ // finish nums2, copy all nums1
                temp[i] = nums1[nums1_index++];
            }else if(nums1[nums1_index] < nums2[nums2_index]){
                temp[i] = nums1[nums1_index++];
            }else{
                temp[i] = nums2[nums2_index++];
            }
        }

        for(int i = 0; i < m+n; i++){
            nums1[i] = temp[i];
        }
    }
}