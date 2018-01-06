import heapq

import sys


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def reverse(l):
    prev = None
    cur = l
    while cur:
        nxt = cur.next
        cur.next = prev
        prev = cur
        cur = nxt

    return prev


def getmid(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow


def isPalindrome(head):
    mid = getmid(head)
    rev = reverse(mid)
    while rev and rev.val == head.val:
        rev = rev.next
        head = head.next

    return rev == None


def print_list(l):
    while l:
        print l.val
        l = l.next


# head = ListNode(1)
# head.next = ListNode(2)
# head.next.next = ListNode(3)
# head.next.next.next = ListNode(2)
# head.next.next.next.next = ListNode(2)
# print_list(head)
# print isPalindrome(head)


def copy_list(l):
    cur = l
    done = {}
    while cur:
        done[cur] = ListNode(l.val)
        cur = cur.next

    for (k, v) in done.iteritems():
        new_node = v
        new_node.next = done[k.next] if k.next != None else None
        new_node.arb = done[k.arb]

    return done[l]


def mergeKLists(head_list):
    k_heap = []
    new_list = ListNode(None)
    new_head = new_list
    for head in head_list:
        heapq.heappush(k_heap, (head.val, head))

    while k_heap[0][1]:
        min_val, head = heapq.heappop(k_heap)
        new_list.next = ListNode(min_val)
        nxt = head.next
        new_list = new_list.next
        new_val = nxt.val if nxt else sys.maxint
        heapq.heappush(k_heap, (new_val, nxt))

    return new_head.next


# head = ListNode(1)
# head.next = ListNode(10)
# head.next.next = ListNode(20)
#
# head1 = ListNode(4)
# head1.next = ListNode(11)
# head1.next.next = ListNode(13)
#
# head2 = ListNode(3)
# head2.next = ListNode(8)
# head2.next.next = ListNode(9)
#
# print_list(head)
# print_list(mergeKLists([head, head1, head2]))
def remove_all_n(head, n):
    # Fill in the logic here
    new_head = ListNode(-1)
    tmp = new_head
    while head:
        if head.val != n:
            tmp.next = head
            tmp = tmp.next
        print tmp.val
        head = head.next

    tmp.next = None
    return new_head.next


head = ListNode(1)
head.next = ListNode(2)
head.next = ListNode(3)

print_list(remove_all_n(head, 2))
