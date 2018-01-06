from Queue import Queue
from collections import defaultdict

import sys


class Node:
    def __init__(self, d):
        self.data = d
        self.left = self.right = None


def maxDepth(root):
    if root:
        return 1 + max(maxDepth(root.left), maxDepth(root.right))
    return 0


def minDepth(root):
    if root:
        return 1 + max(minDepth(root.left), minDepth(root.right))
    return 0


def inorder(root):
    if root:
        inorder(root.left)
        print root.val
        inorder(root.right)


def isBalanced(root):
    return (maxDepth(root) - minDepth(root) <= 1)


# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# @param A : root node of tree
# @return an integer
def mirror_itself(self, t1, t2):
    if t1 == None or t2 == None:
        return t1 == None and t2 == None

    return t1.val == t2.val and self.mirror_itself(t1.left, t2.right) and self.mirror_itself(t1.right, t2.left)


def isSymmetric(self, t):
    if t == None:
        return 1
    return self.mirror_itself(t.left, t.right)


def make_heap_tree(A):
    if A:
        elt = max(A)
        i = A.index(elt)
        root = TreeNode(elt)
        root.left = make_heap_tree(A[:i])
        root.right = make_heap_tree(A[i + 1:])
        return root
    return None


def sortedArrayToBST(self, A):
    if len(A) == 0:
        return None
    mid = len(A) / 2
    root = TreeNode(A[mid])
    root.left = self.sortedArrayToBST(A[:mid])
    root.right = self.sortedArrayToBST(A[mid + 1:])
    return root


# inorder(make_heap_tree([1]))
def kthsmallest(root, k):
    def inorder(root):
        if root:
            inorder(root.left)
            kthsmallest.inorder_vec.append(root.val)
            inorder(root.right)

    kthsmallest.inorder_vec = []
    inorder(root)
    return kthsmallest.inorder_vec[k - 1]


# root = TreeNode(2)
# root.left = TreeNode(1)
# root.right = TreeNode(3)
#
# print kthsmallest(root, 2)

def invert(root):
    if root:
        root.right, root.left = root.left, root.right
        invert(root.left)
        invert(root.right)


def level_order(root):
    def level(root, l):
        if root:
            level_order.level_map[l].append(root.val)
            level(root.left, l + 1)
            level(root.right, l + 1)

    level_order.level_map = defaultdict(list)
    level(root, 0)
    ltr = True
    for level in level_order.level_map:
        if not ltr:
            level_order.level_map[level].reverse()
        ltr = not ltr

    return level_order.level_map.values()


def root_to_leaf(root, sum, path):
    if root:
        if root.left == None and root.right == None:
            if root.val == sum:
                root_to_leaf.paths.append(path)
            return

        root_to_leaf(root.left, sum - root.val, path)
        root_to_leaf(root.right, sum - root.val, path)
        path.pop()
    root_to_leaf.paths = []


def flatten(root):
    if root:
        lelf_head, left_end = flatten(root.left)
        right_head, right_end = flatten(root.right)
        root.right = lelf_head if root.right else None
        left_end.right = right_head if left_end.right else None
        return (root, right_end if right_end else left_end)

    return None, None


# root = TreeNode(1)
# root.left = TreeNode(2)
# root.left.left = TreeNode(4)
# root.left.right = TreeNode(5)
#
# root.right = TreeNode(3)
# root.right.left = TreeNode(6)
# root.right.right = TreeNode(7)
#
# print level_order(root)

def sum_to_leaf(root, cur_sum):
    if root:
        if root.left == None and root.right == None:
            return cur_sum * 10 + root.val

        return sum_to_leaf(root.left, cur_sum * 10 + root.val) + sum_to_leaf(root.right, cur_sum * 10 + root.val)
    return 0


def trimBST(root, L, R):
    if root:
        if root.val < L:
            return trimBST(root.right, L, R)
        if root.val > R:
            return trimBST(root.left, L, R)
        root.left = trimBST(root.left, L, R)
        root.right = trimBST(root.right, L, R)
        return root
    return None


def root_to_leaf_paths(root, path=[]):
    if root:
        path.append(root.val)
        if root.left == None and root.right == None:
            print path
        root_to_leaf_paths(root.left, path)
        root_to_leaf_paths(root.right, path)
        path.pop()


def width(root):
    level = defaultdict(lambda: [sys.maxint, -sys.maxint])

    def width_util(root, h=0, l=0):
        if root:
            level[l][0] = min(level[l][0], h)
            level[l][1] = max(level[l][1], h)
            width_util(root.left, h - 1, l + 1)
            width_util(root.right, h + 1, l + 1)

    width_util(root)
    return max(level[k][1] - level[k][0] for k in level)


def diameter(root):
    def diameter_util(root, l=0):
        if root:
            ld, lh = diameter_util(root.left, l + 1)
            rd, rh = diameter_util(root.right, l + 1)
            return max(ld, rd, lh + rh + 1), max(lh, rh) + 1
        return 0, 0

    return diameter_util(root)


def get_max_sum():
    def do(root, i, n):
        if i < n and root[i] != '#':
            excl = do(root, i + 1, n) + do(root, i + 2, n)
            print root[i], excl
            incl = int(root[i])
            if i + 1 < n and root[i + 1] != '#':
                incl += do(root, i + 2, n) + do(root, i + 3, n)
            if i + 2 < n and root[i + 2] != '#':
                incl += do(root, i + 3, n) + do(root, i + 4, n)
            gb[0] = max(gb[0], incl, excl)
            return incl
        return 0

    gb = [0]
    root = ['1', '2', '3', '1', '#', '4', '5']
    return do(root, 0, 6)


print get_max_sum()

# root = TreeNode(1)
# root.left = TreeNode(2)
# root.right = TreeNode(3)
# root.right.left = TreeNode(4)
# root.right.right = TreeNode(5)
# root.left.left = TreeNode(1)
# print get_max_sum(root)
#
# root.right.right = TreeNode(8)
# root.left.left = TreeNode(4)
# root.left.right = TreeNode(5)
# print width(root)

# root_to_leaf_paths(root)
# print diameter(root)
