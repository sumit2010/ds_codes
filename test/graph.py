from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u] = v
        self.graph[v] = u

    def dfs(self):
        def do(u):
            visited.add(u)
            print u
            for v in self.graph[u]:
                if v not in visited:
                    do(v)

        visited = set()

    def has_cycle(self):
        def do(u):
            flag_recur.add(u)
            for v in self.graph[u]:
                if v not in flag_recur and do(v):
                    return True
                elif v in flag_recur:
                    return True

            return False

        flag_recur = set()

    def topological_util(self, u, stack, visited):
        visited.add(u)
        for v in self.graph[u]:
            if v not in visited:
                self.topological(v)

        stack.append(u)

    def topological(self):
        visited = set()
        stack = []
        for u in self.graph:
            if u not in visited:
                self.topological_util(u, stack, visited)

        return stack


# graph = defaultdict(list)
# print not graph['1']
# print all([range(7)])




def test():
    # Enter your code here. Read input from STDIN. Print output to STDOUT
    from collections import defaultdict

    # Enter your code here. Read input from STDIN. Print output to STDOUT
    def dependent_passed(graph, tests, u):
        if not tests[u - 1]:
            return False
        if not graph[u]:
            return True
        return all(dependent_passed(v) for v in graph[u])

    n = int(raw_input().split(' ')[1])
    graph = defaultdict(list)
    tests = map(int, raw_input().split())
    for i in range(n):
        x, y = raw_input().split(' ')
        graph[x].append(y)

    print graph

    for test, has_passed in enumerate(tests):
        if has_passed == 0:
            print "NO"
        else:
            print "YES" if dependent_passed(graph, tests, test + 1) else "NO"


def zombieCluster(zombies):
    def dfs(i):
        visited.add(i)
        for j in range(len(zombies[i])):
            if zombies[i][j] == 1 and j not in visited:
                dfs(j)

    visited = set()
    clusters = 0
    for i in range(len(zombies)):
        if i not in visited:
            dfs(i)
            clusters += 1
    return clusters


#
#
# zombies = [[1, 1, 0, 0],
#            [1, 1, 1, 0],
#            [0, 1, 1, 0],
#            [0, 0, 0, 1]]
# print zombieCluster(zombies)


# Complete the function below.

def connectedCities(n, g, originCities, destinationCities):
    def gcd(x, y):
        while y != 0:
            (x, y) = (y, x % y)
        return x

    res = []

    gcd_table = [[None] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            gcd_table[i][j] = gcd_table[j][i] = gcd(i, j)

    def bfs(s, d):
        visited = [False] * (n + 1)

        # Create a queue for BFS
        queue = []

        # Mark the source node as visited and enqueue it
        queue.append(s)
        visited[s] = True

        while queue:

            # Dequeue a vertex from queue and print it
            s = queue.pop(0)
            if s == d:
                return True

            # Get all adjacent vertices of the dequeued
            # vertex s. If a adjacent has not been visited,
            # then mark it visited and enqueue it
            for i in range(1, n + 1):

                if gcd_table[s][i] > g and visited[i] == False:
                    queue.append(i)
                    visited[i] = True

    for s, d in zip(originCities, destinationCities):
        res.append(1 if bfs(s, d) else 0)

    return res


print connectedCities(6, 1, [1, 4, 3, 6], [3, 6, 2, 5])
