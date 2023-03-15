# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
    
    def add_node(self, data):
        curr_node = self.head
        node = ListNode()
        node.val = data

        if curr_node is None:
            self.head = node
            return
        
        if node.val < curr_node.val:
            node.next = curr_node
            self.head = node
            return

        while curr_node.next is not None:
            if curr_node.next.val > node.val:
                break
            curr_node = curr_node.next

        node.next = curr_node.next    
        curr_node.next = node
        return
    
    def output(self):
        return self.head

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        linked_list = LinkedList()
        for list_node in lists:
            curr_node = list_node
            while curr_node is not None:
                linked_list.add_node(curr_node.val)
                curr_node = curr_node.next
        answer = linked_list.output()
        return answer