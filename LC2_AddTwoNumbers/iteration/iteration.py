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
    total = 0 # the result after addition
    isNextOne = 0 # if next digit is one
    result = ListNode()
    curr = result

    while(l1 != None and l2 != None):
        total = l1.val + l2.val + isNextOne
        isNextOne = total // 10 # if next digit is one
        curr.next = ListNode(total % 10) # current digit
        curr = curr.next # update the pointer
        l1 = l1.next
        l2 = l2.next
    
    # if length of two linkedlist are not the same
    while l1 != None:
        total = l1.val + isNextOne
        isNextOne = total // 10 # if next digit is one
        curr.next = ListNode(total % 10) # current digit
        curr = curr.next # update the pointer
        l1 = l1.next
    
    while l2 != None:
        total = l2.val + isNextOne
        isNextOne = total // 10 # if next digit is one
        curr.next = ListNode(total % 10) # current digit
        curr = curr.next # update the pointer
        l2 = l2.next
    
    # check if a new digit is needed when ends both linkedlist
    if isNextOne != 0:
        curr.next = ListNode(isNextOne)
    
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

        
        