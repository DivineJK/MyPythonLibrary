compf = lambda a, b: a < b
class warshall_floyd:
    def __init__(self, n, compare, identity=0, INF=int(1e18)):
        self.n = n
        self.Map = [INF]*(n*n)
        self.compare = compare
        self.identity = identity
        self.INF = INF
        for i in range(n):
            self.Map[i*(n+1)] = identity
    def reset(self):
        self.Map = [self.INF]*(self.n*self.n)
        for i in range(self.n):
            self.Map[i*(self.n+1)] = self.identity
    def connect_edge(self, a, b, c=1, directed=True):
        if self.compare(c, self.Map[a*self.n+b]):
            self.Map[a*self.n+b] = c
        if not directed:
            if self.compare(c, self.Map[b*self.n+a]):
                self.Map[b*self.n+a] = c
    def simply_wf(self):
        for k in range(self.n):
            for i in range(self.n):
                for j in range(self.n):
                    if self.compare(self.Map[i*self.n+k]+self.Map[k*self.n+j], self.Map[i*self.n+j]):
                        self.Map[i*self.n+j] = self.Map[i*self.n+k]+self.Map[k*self.n+j]
