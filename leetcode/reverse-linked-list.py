# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self) -> str:
        if not self.next:
            return f"{self.val}"
        return f"{self.val} {self.next}"

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev_node = None
        current_node = head

        while current_node is not None:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node

        return prev_node       
def listToLinkedList(data):
    if not data:
        return None
    return ListNode(val=data[0], next=listToLinkedList(data[1:]))

solution = Solution()
print(solution.reverseList(head = listToLinkedList([1,2,3,4,5])))
