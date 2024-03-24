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
    def mergeInBetween(
        self, list1: ListNode, a: int, b: int, list2: ListNode
    ) -> ListNode:
        curr = list1
        for _ in range(a - 1):
            curr = curr.next

        temp = curr.next
        for _ in range(b - a + 1):
            temp = temp.next
        curr.next = list2
        while curr.next:
            curr = curr.next
        curr.next = temp
        return list1


def listToLinkedList(data):
    if not data:
        return None
    return ListNode(val=data[0], next=listToLinkedList(data[1:]))


solution = Solution()
print(
    solution.mergeInBetween(
        list1=listToLinkedList([10, 1, 13, 6, 9, 5]),
        a=3,
        b=4,
        list2=listToLinkedList([1000000, 1000001, 1000002]),
    )
)
