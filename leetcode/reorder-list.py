from collections import deque


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
    def reorderList(self, head) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # find middle
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse second half
        second = slow.next
        slow.next, prev = None, None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        # merge two halfs
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2
        # temp = head.next
        # nodes = deque()
        # while temp:
        #     nodes.append(temp)
        #     temp = temp.next
        #
        # while nodes:
        #     head.next = nodes.pop()
        #     head = head.next
        #     if not nodes:
        #         break
        #     head.next = nodes.popleft()
        #     head = head.next
        # print(list(nodes))
        # head.next = None


def listToLinkedList(data):
    if not data:
        return None
    return ListNode(val=data[0], next=listToLinkedList(data[1:]))


solution = Solution()

head = listToLinkedList([1, 2, 3, 4])
solution.reorderList(head)
print(head)
