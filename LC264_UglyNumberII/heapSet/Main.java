import java.util.HashSet;
import java.util.PriorityQueue;

/*
* An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.
* Given an integer n, return the nth ugly number.
* Input: n = 10
* Output: 12
* Explanation: [1, 2, 3, 4, 5, 6, 8, 9, 10, 12] is the sequence of the first 10 ugly numbers.
* Input: n = 1
* Output: 1
* Explanation: 1 has no prime factors, therefore all of its prime factors are limited to 2, 3, and 5.
*/

public class Main{
    public static void main(String[] args){
        System.out.println(nthUglyNumber(10)); // expected 12
        System.out.println(nthUglyNumber(1)); // expected 1
    }

    public static int nthUglyNumber(int n) {
        // Min Heap and HashSet
        // Time Compleity: O(nlogn)
        // Space Complexity: O(n)
        HashSet<Integer> hashSet = new HashSet<>();
        PriorityQueue<Integer> heap = new PriorityQueue<>();

        hashSet.add(1);
        heap.add(1);
        int[] factors = {2,3,5};
        int result = 1;

        for(int i = 0; i < n; i++){
            result = heap.poll();
            for (int factor : factors){
                int newNum = factor * result;
                if(!hashSet.contains(newNum)){
                    hashSet.add(newNum);
                    heap.add(newNum);
                }
            }
        }
        return result;
    }
}