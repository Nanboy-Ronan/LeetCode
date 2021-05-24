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
        int total = 0;
        int isNextOne = 0;
        ListNode result = new ListNode();
        ListNode curr = result;
        ListNode l1Curr = l1;
        ListNode l2Curr = l2;

        while(l1Curr != null && l2Curr != null){
            total = l1Curr.val + l2Curr.val + isNextOne;
            isNextOne = total / 10;
            curr.next = new ListNode(total % 10);
            // update all pointers
            curr = curr.next;
            l1Curr = l1Curr.next;
            l2Curr = l2Curr.next;
        }

        while(l1Curr != null){
            total = l1Curr.val + isNextOne;
            isNextOne = total / 10;
            curr.next = new ListNode(total % 10);
            curr = curr.next;
            l1Curr = l1Curr.next;
        }

        while(l2Curr != null){
            total = l2Curr.val + isNextOne;
            isNextOne = total / 10;
            curr.next = new ListNode(total % 10);
            curr = curr.next;
            l2Curr = l2Curr.next;
        }

        if(isNextOne != 0){
            curr.next = new ListNode(isNextOne);
        }

        return result.next;
    }
}