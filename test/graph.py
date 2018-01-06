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

