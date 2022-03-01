public class Main {
    public static void main(String[] args){
        Solution soln = new Solution();
        int[] nums = new int[] {3,2,1,5,6,4};
        int k = 2;
        int result = soln.findKthLargest(nums, k);
        System.out.println(result);
    }
}
