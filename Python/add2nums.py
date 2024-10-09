# Extremely inefficient solution to a leetcode puzzle
# I double checked and its actually O(n+m) which is good
# Definition for singly-linked list.
# If you want to check this solution go to leetcode #2
class Node:
    def __init__(self, data=None):
        # Data stored in the node
        self.data = data
        # Reference to the next node in the singly linked list
        self.next = None

class Solution:
    def llta(self, head):
        arr = []
        curr = head

        while curr is not None:
            arr.append(curr.val)
            curr = curr.next

        return arr
    def print_array(self, arr):
        for i in arr:
            print(i, end=" ")
        print()

    def lst2link(self, lst):
        cur = dummy = ListNode(0)
        for e in lst:
            cur.next = ListNode(e)
            cur = cur.next
        return dummy.next

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        arr1 = self.llta(l1)
        arr2 = self.llta(l2)
        num1 = int(''.join(map(str, arr1))[::-1])
        num2 = int(''.join(map(str, arr2))[::-1])
        num3 = num1 + num2
        num3 = str(num3)
        
    
        lst = []
        for i in str(num3)[::-1]:
            lst.append(int(i))
        print(lst)
        return self.lst2link(lst)