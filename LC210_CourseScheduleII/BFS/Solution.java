import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;
import java.util.LinkedList;
import java.util.Queue;

class Solution {
    public int[] findOrder(int numCourses, int[][] prerequisites) {
        // The number of prerequisite courses for each node
        HashMap<Integer,Integer> outNum = new HashMap<>();
        // The courses that has this node as prerequisite
        HashMap<Integer, ArrayList<Integer>> inNodes = new HashMap<>();

        HashSet<Integer> set = new HashSet<>();

        for(int i =0; i < prerequisites.length; i++){
            int curr = prerequisites[i][0];
            int currPrerequisite = prerequisites[i][1];

            set.add(curr);
            set.add(currPrerequisite);

            // Initialize the row of the outNum
            if(!outNum.containsKey(curr)){
                outNum.put(curr, 0);
            }
            if(!outNum.containsKey(currPrerequisite)){
                outNum.put(currPrerequisite, 0);
            }

            // Increment the curr if meet 
            int temp = outNum.get(curr);
            outNum.put(curr, temp+1);

            if(!inNodes.containsKey(currPrerequisite)){
                inNodes.put(currPrerequisite, new ArrayList<>());
            }

            ArrayList<Integer> list = inNodes.get(currPrerequisite);
            list.add(curr);
        }

        Queue<Integer> queue = new LinkedList<>();
        for(int k: set){
            if(outNum.get(k) == 0) queue.offer(k);
        }
        int[] result = new int[numCourses];
        int count = 0;
        while(!queue.isEmpty()){
            int temp = queue.poll();

            result[count++] = temp;

            ArrayList<Integer> list = inNodes.getOrDefault(temp, new ArrayList<>());

            for(int k : list){
                int num = outNum.get(k);

                if(num == 1){
                    queue.offer(k);
                }

                outNum.put(k, num-1);
            }   
        }

        for(int k : set){
            if(outNum.get(k) != 0){
                return new int[0];
            }
        }

        HashSet<Integer> resultSet = new HashSet<>();
        for(int i = 0; i < count; i++){
            resultSet.add(result[i]);
        }

        for(int i = 0; i < numCourses; i++){
            if(!resultSet.contains(i)){
                result[count++] = i;
            }
        }

        return result;
    }
}