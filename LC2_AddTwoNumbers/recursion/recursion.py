# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.
# Input: l1 = [0], l2 = [0]
# Output: [0]
# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]

class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next

def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    # recurtion
    # Time Complexity: O(max(len(l1),len(l2)))
    # Space Complexity: O(max(len(l1),len(l2)))

    # base case
    total = l1.val + l2.val
    isNextOne = total // 10
    result = ListNode(total % 10)

    if l1.next or l2.next or isNextOne: # l1 and l2 are not end or there is another one
        l1 = l1.next if l1.next else ListNode(0)
        l2 = l2.next if l2.next else ListNode(0)

        l1.val = l1.val + isNextOne
        result.next = addTwoNumbers(l1, l2)

    return result

class test1:
    def __init__(self) -> None:
        self.l1 = ListNode(2)
        self.l1.next = ListNode(4)
        self.l1.next.next = ListNode(3)

        self.l2 = ListNode(5)
        self.l2.next = ListNode(6)
        self.l2.next.next = ListNode(4)
    
    def main(self) -> None:
        result = addTwoNumbers(self.l1, self.l2)
        while(result != None):
            print(result.val)
            result = result.next

test = test1()
test.main()