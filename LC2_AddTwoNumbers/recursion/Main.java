/* You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
* You may assume the two numbers do not contain any leading zero, except the number 0 itself.
*/

/* Input: l1 = [2,4,3], l2 = [5,6,4]
* Output: [7,0,8]
* Explanation: 342 + 465 = 807.
* Input: l1 = [0], l2 = [0]
* Output: [0]
* Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
* Output: [8,9,9,9,0,0,0,1]
*/

/* iteration
* Time Complexity: O(max(len(l1),len(l2)))
* Space Complexity: O(max(len(l1),len(l2)))
*/
public class Main{
    public static void main(String[] args){
        ListNode l1 = new ListNode(2);
        l1.next = new ListNode(4);
        l1.next.next = new ListNode(3);

        ListNode l2 = new ListNode(5);
        l2.next = new ListNode(6);
        l2.next.next = new ListNode(4);

        ListNode result = addTwoNumbers(l1, l2);
        while(result != null){
            System.out.println(result.val);
            result = result.next;
        }
    }

    private static ListNode addTwoNumbers(ListNode l1, ListNode l2){
        int total = l1.val + l2.val;
        int isNextOne = total / 10;
        ListNode result = new ListNode(total % 10);

        if(l1.next != null || l2.next != null || isNextOne != 0){
            l1 = l1.next ==null? new ListNode(0) : l1.next;
            l2 = l2.next ==null? new ListNode(0) : l2.next;

            l1.val = l1.val + isNextOne;
            result.next = addTwoNumbers(l1, l2);

        }
        return result;
    }
}