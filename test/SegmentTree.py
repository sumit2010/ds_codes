from collections import Counter


class SegmentTree:
    def __init__(self, arr):
        self.Tree = [None] * (2 * len(arr) + 1)
        self.arr = arr
        self.construct()

    def construct(self):
        self.construct_util(self.arr, 0, len(self.arr) - 1, 0)

    def construct_util(self, arr, ss, se, si):
        if ss == se:
            print ss
            self.Tree[si] = arr[ss]
            return arr[ss]
        mid = (ss + se) / 2
        self.Tree[si] = self.construct_util(arr, ss, mid, 2 * si + 1) + self.construct_util(arr, mid + 1, se,
                                                                                            2 * si + 2)
        return self.Tree[si]

    def getSum_util(self, qs, qe, ss, se, si):
        if qs <= ss and se <= qe:
            return self.Tree[si]
        if qs > se or ss > qe:
            return 0
        mid = (ss + se) / 2
        return self.getSum_util(qs, qe, ss, mid, 2 * si + 1) + self.getSum_util(qs, qe, mid + 1, se, 2 * si + 2)

    def getSum(self, qs, qe):
        return self.getSum_util(qs, qe, 0, len(self.arr) - 1, 0)


# st = SegmentTree([1, 3, 5, 7, 9, 11])
# print st.getSum(1, 3)

A = [1, 3, 1, 2, 2, 1]
counter_list = [Counter()] * (len(A) + 1)
for i in range(len(A)):
    counter_list[i] = counter_list[i - 1] + Counter({A[i]: 1})
print counter_list
print counter_list[4][1] - counter_list[-1][1]
Counter().copy()