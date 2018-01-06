# Enter your code here. Read input from STDIN. Print output to STDOUT

def merge(intervals):
    intervals.sort(key=lambda x: x[0])
    merged = []
    for interval in intervals:
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            merged[-1][1] = max(merged[-1][1], interval[1])

    return merged


n = int(raw_input())
pairs = []
for i in range(n):
    a, b = raw_input().strip().split(' ')
    pairs.append([int(a), int(b)])
    # pairs.append([int(raw_input().split(' ')[0]),int(raw_input().split(' ')[1])])
merged = merge(pairs)
print sum((m[1] - m[0] + 1) for m in merged)


# Enter your code here. Read input from STDIN. Print output to STDOUT
def calculate_time(t, cabs):
    return sum(t / cab for cab in cabs)


def binarySearch(cabs, K, l, h):
    while l < h:
        m = (l + h) / 2
        time = calculate_time(m, cabs)
        if time < K:
            l = m + 1
        else:
            h = m - 1
    return l


n, K = raw_input().strip().split(' ')
cabs = []
for i in range(int(K)):
    cabs.append(int(raw_input()))

l = binarySearch(cabs, int(n), 0, min(cabs) * int(K))
l -= 1
while calculate_time(l, cabs) < int(n):
    l += 1
print l
