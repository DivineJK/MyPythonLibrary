import sys
sys.setrecursionlimit(500010)
class SCC:
    def __init__(self, n):
        self.n = n
        self.d = [[] for _ in range(n)]
        self.inv_d = [[] for _ in range(n)]
        self.t = [-1]*n
        self.cmp = []
        self.flg = [True]*n
        self.fflg = [True]*n
        self.group = [-1]*n
        self.visited = []
        self.group_count = 0
        self.tf = set()
        self.td = []
        self.ts_count = []
    def connect_edge(self, u, v, directed=True):
        self.d[u].append(v)
        self.inv_d[v].append(u)
        if not directed:
            self.d[v].append(u)
            self.inv_d[u].append(v)
    def dfs(self, v):
        self.flg[v] = False
        for i in self.d[v]:
            if self.flg[i]:
                self.dfs(i)
        if self.t[v] < 0:
            if self.visited == []:
                self.t[v] = 0
            else:
                self.t[v] = self.t[self.visited[-1]] + 1
        self.visited.append(v)
    def rdfs(self, v, k):
        self.fflg[v] = False
        self.group[v] = k
        for i in self.inv_d[v]:
            if self.fflg[i]:
                self.rdfs(i, k)
    def reset():
        self.t = [-1]*n
        self.flg = [True]*n
        self.fflg = [True]*n
        self.group = [-1]*n
        self.visited = []
        self.group_count = 0
        self.tf = set()
        self.td = []
        self.ts_count = []
    def SCC(self):
        cnt = 0
        pnt = 0
        while cnt < self.n - 1:
            while not self.flg[pnt]:
                pnt += 1
            self.dfs(pnt)
            cnt = self.t[pnt]
        for i in range(self.n, 0, -1):
            if not self.fflg[self.visited[i-1]]:
                continue
            self.td.append([])
            self.ts_count.append(0)
            self.cmp.append([])
            self.rdfs(self.visited[i-1], self.group_count)
            self.group_count += 1
        for i in range(self.n):
            self.cmp[self.group[i]].append(i)
    def topological_sort(self):
        for i in range(self.n):
            for j in self.d[i]:
                if self.group[i] != self.group[j] and self.group[i]*self.group_count+self.group[j] not in self.tf:
                    self.td[self.group[i]].append(self.group[j])
                    self.ts_count[self.group[j]] += 1
                    self.tf.add(self.group[i]*self.group_count+self.group[j])
        t = []
        ffflg = [True]*self.group_count
        pnt = 0
        cnt = 0
        for i in range(self.group_count):
            if self.ts_count[i] == 0:
                t.append(i)
                cnt += 1
                ffflg[i] = False
        while pnt < cnt:
            m = cnt
            for i in range(pnt, cnt):
                for j in self.td[t[i]]:
                    if self.ts_count[j]:
                        self.ts_count[j] -= 1
                        if self.ts_count[j] == 0:
                            ffflg[j] = False
                            t.append(j)
                            cnt += 1
            pnt = m
        return t
