from heapq import heappush, heappop
class dijkstra:
    def __init__(self, n, identity=0, INF=int(1e18)):
        self.INF = INF
        self.n = n
        self.identity = identity
        self.cost = [INF]*n
        self.neighbor = [[] for _ in range(n)]
        self.neighbor_cost = {}
        self.prev = [-1]*n
    def reset(self):
        self.cost = [INF]*self.n
        self.prev = [-1]*self.n
        self.neighbor = [[] for _ in range(self.n)]
        self.neighbor_cost = {}
    def connect_edge(self, a, b, c=1, directed=True):
        if a*self.n+b not in self.neighbor_cost:
            self.neighbor[a].append(b)
            self.neighbor_cost[a*self.n+b] = c
        else:
            if self.neighbor_cost[a*self.n+b] > c:
                self.neighbor_cost[a*self.n+b] = c
        if not directed:
            if b*self.n+a not in self.neighbor_cost:
                self.neighbor[b].append(a)
                self.neighbor_cost[b*self.n+a] = c
            else:
                if self.neighbor_cost[b*self.n+a] > c:
                    self.neighbor_cost[b*self.n+a] = c
    def simply_dijkstra(self, st):
        pq = []
        pq_cnt = 0
        self.cost[st] = self.identity
        for i in range(self.n):
            pq_cnt += 1
            heappush(pq, (self.cost[i], i))
        while pq_cnt:
            b = heappop(pq)
            r = b[1]
            pq_cnt -= 1
            if self.cost[r] < b[0]:
                continue
            for i in self.neighbor[r]:
                if self.cost[i] > self.cost[r]+self.neighbor_cost[r*self.n+i]:
                    self.cost[i] = self.cost[r]+self.neighbor_cost[r*self.n+i]
                    self.prev[i] = r
                    heappush(pq, (self.cost[i], i))
                    pq_cnt += 1
    def path_restore(self, s, g):
        path = [g]
        if s == g:
            return path
        while self.prev[g] != s:
            if self.prev[g] == -1:
                return []
            g = self.prev[g]
            path.append(g)
        path.append(s)
        path.reverse()
        return path
