'''
link: https://www.youtube.com/watch?v=wgFPrzTjm7s
Given two nono-empty linked lists representing two non-negative integers.
The digits are stored in reverse order and each of their nodes contain a single digit.
Add the two numbers and return it as a linked lists.
'''
# Definition of singly-linked list
class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class solution:
    # def addTwoNum(self, l1: ListNode, l2: ListNode) -> ListNode:
    #     dummy = ListNode()
    #     cur = dummy

    #     carry = 0
    #     while l1 or l2 or carry:
    #         v1 = l1.val if l1 else 0
    #         v2 = l2.val if l2 else 0

    #         # New Value
    #         val = v1 + v2 + carry

    #         carry = val//10
    #         val = val % 10
    #         cur.next = ListNode(val)

    #         # Update
    #         cur = cur.next
    #         l1 = l1.next if l1 else None
    #         l2 = l2.next if l2 else None

    #     return dummy.next
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        added = ListNode(val = (l1.val + l2.val) % 10)
        carry_over = (l1.val + l2.val) // 10
        current_node = added

        while(l1.next and l2.next):
            l1 = l1.next
            l2 = l2.next
            current_node.next = ListNode(val = (l1.val + l2.val + carry_over) % 10)
            carry_over = (l1.val + l2.val + carry_over) // 10
            current_node = current_node.next
        
        while(l1.next):
            l1 = l1.next
            current_node.next = ListNode(val = (l1.val + carry_over) % 10)
            carry_over = (l1.val + carry_over) // 10
            current_node = current_node.next
        
        while(l2.next):
            l2 = l2.next
            current_node.next = ListNode(val = (l2.val + carry_over) % 10)
            carry_over = (l2.val + carry_over) // 10
            current_node = current_node.next
        
        if carry_over > 0:
            current_node.next = ListNode(val = carry_over)
        
        return added

    

    

# Test case
# Create two linked lists: 2 -> 4 -> 3 and 5 -> 6 -> 4
l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

result = solution().addTwoNumbers(l1, l2)

# Print the result
while result:
    print(result.val, end=" ")
    result = result.next

