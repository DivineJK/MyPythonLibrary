import sys
sys.setrecursionlimit(50000)
class Bellman_Ford:
    def __init__(self, n, INF=int(1e18)):
        self.n = n
        self.INF = INF
        self.graph = [[] for _ in range(n)]
        self.distance = [INF]*n
        self.prev = [-1]*n
        self.edges = {}
        self.arrived = [False]*n
        self.reachable = [False]*n
        self.negative_weight_cycle = False
    def connect_edge(self, a, b, c, directed=True):
        if a*self.n+b in self.edges:
            if self.edges[a*self.n+b] > c:
                self.edges[a*self.n+b] = c
        else:
            self.edges[a*self.n+b] = c
            self.graph[a].append(b)
        if not directed:
            if b*self.n+a in self.edges:
                if self.edges[b*self.n+a] > c:
                    self.edges[b*self.n+a] = c
            else:
                self.edges[b*self.n+a] = c
                self.graph[b].append(a)
    def dfs(self, st, gl):
        if st == gl:
            self.reachable[st] = True
            return True
        if self.arrived[st]:
            return self.reachable[st]
        reachability = False
        self.arrived[st] = True
        for i in self.graph[st]:
            if self.dfs(i, gl):
                reachability = True
                break
        self.reachable[st] = reachability
        return reachability
    def simply_Bellman_Ford(self, v, d=-1):
        if d == -1: d = self.n - 1
        self.distance = [self.INF]*self.n
        self.prev = [-1]*self.n
        self.distance[v] = 0
        for i in range(1, self.n):
            for ab in self.edges:
                a = ab//self.n
                b = ab%self.n
                if self.distance[b] > self.distance[a] + self.edges[ab]:
                    self.distance[b] = self.distance[a] + self.edges[ab]
                    self.prev[b] = a
        for ab in self.edges:
            a = ab//self.n
            b = ab % self.n
            if self.distance[a] + self.edges[ab] < self.distance[b]:
                if self.reachable[b]:
                    self.negative_weight_cycle = True
