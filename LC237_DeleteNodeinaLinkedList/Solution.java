// Write a function to delete a node in a singly-linked list. You will not be given access to the head of the list, instead you will be given access to the node to be deleted directly.
// It is guaranteed that the node to be deleted is not a tail node in the list.

class Solution {
    // Copy the next node to current then delete the next node
    // Time Complexity: O(1)
    // Space Complexity: O(1)
    public void deleteNode(ListNode node) {
        ListNode next = node.next;
        node.val = next.val;
        node.next = next.next;
    }

    public class ListNode {
            int val;
            ListNode next;
            ListNode(int x) { val = x; }
        }
}