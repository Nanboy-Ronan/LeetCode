import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

// Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

class Solution {
    // Sort
    // Time Complexity: O(nlogn)
    // Space Complexity: O(1)
    public int[][] merge(int[][] intervals) {
        if(intervals.length == 0 || intervals.length == 1){
            return intervals;
        }

        List results = new ArrayList<>();

        Arrays.sort(intervals, ((o1, o2) -> o1[0] == o2[0]? 0 : o1[0] - o2[0]));
        int start = intervals[0][0];
        int end = intervals[0][1];
        for(int i = 1; i < intervals.length; i++){
            // Have overlap
            if(end >= intervals[i][0]){
                end = Math.max(end, intervals[i][1]);
            }else{
                results.add(new int[] {start, end});
                start = intervals[i][0];
                end = intervals[i][1];
            }
        }
        results.add(new int[] {start, end});

        int[][] retVal = new int[results.size()][2];
        for(int i = 0; i < retVal.length; i++){
            retVal[i] = (int[]) results.get(i);
        }
        return retVal;
        
    }
}