# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self) -> str:
        return f"{self.val} {self.next.__str__()}"


def makeLinkedList(nums, idx=0):
    if idx == len(nums) - 1:
        return ListNode(nums[0], next=None)
    return ListNode(nums[0], next=makeLinkedList(nums, idx + 1))


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        length = 0
        temp = head
        while temp.next:
            temp = temp.next
            length += 1

        print(length)
        beforeRemovedIdx = length - n
        node = head
        temp = head
        for _ in range(beforeRemovedIdx):
            temp = temp.next

        temp.next = temp.next.next
        return node


solution = Solution()
print(solution.removeNthFromEnd(makeLinkedList([1, 2, 3, 4, 5]), 2))
