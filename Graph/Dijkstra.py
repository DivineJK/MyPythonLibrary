from heapq import heappush, heappop
class Dijkstra:
    def __init__(self, n):
        self.n = n
        self.graph = [[] for _ in range(self.n)]
        self.inf = int(1e18)+18
        self.threshold = int(1e18)
        self.cost = [self.inf]*self.n
        self.isDirty = False
    def resetAll(self):
        self.graph = [[] for _ in range(self.n)]
        self.cost = [self.inf]*self.n
        self.isDirty = False
    def resetOnlyCost(self):
        self.cost = [self.inf]*self.n
        self.isDirty = False
    def connectEdge(self, a, b, c, undirected=True):
        self.graph[a].append((b, c))
        if undirected:
            self.graph[b].append((a, c))
    def getMinimumCost(self, start):
        if self.isDirty:
            for i in range(self.n):
                self.cost[i] = self.inf
        self.cost[start] = 0
        pq = [(0, start)]
        pq_cnt = 1
        while pq_cnt:
            b = heappop(pq)
            r = b[1]
            pq_cnt -= 1
            if self.cost[r] < b[0]:
                continue
            for k in self.graph[r]:
                i, v = k[0], k[1]
                if self.cost[i] > self.cost[r] + v:
                    self.cost[i] = self.cost[r] + v
                    pq_cnt += 1
                    heappush(pq, (self.cost[i], i))
        self.isDirty = True
