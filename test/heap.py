import heapq


def sum_nmax(A, B):
    A.sort(reverse=True)
    B.sort(reverse=True)
    min_heap = []
    for a in A:
        for b in B:



    min_heap = []
    for a in A:
        for b in B:
            if len(min_heap) < len(A):
                heapq.heappush(min_heap, a + b)
            elif a + b > min_heap[0]:
                heapq.heappop(min_heap)
                heapq.heappush(min_heap, a + b)
            res = []
    while min_heap:
        res.append(heapq.heappop(min_heap))

    return res[::-1]


print sum_nmax([3, 2, 4, 2], [4, 3, 1, 2])
