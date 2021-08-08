class RootedTree:
    def _RootedTree_calculateChildCount(self):
        p = [self.root]
        pnt = 0
        cnt = 1
        d = 0
        while pnt < cnt:
            d += 1
            m = cnt
            for i in range(pnt, cnt):
                c = p[i]
                for j in self.child[c]:
                    self.depth[j] = d
                    p.append(j)
                    cnt += 1
            pnt = m
        for j in range(self.n, 1, -1):
            self.childCount[self.parent[p[j-1]]] += self.childCount[p[j-1]]
    def _RootedTree_setEulerTour(self):
        p = [0]*self.n
        nowV = self.root
        u = 0
        while nowV != -1:
            tmp = nowV
            if self.inTime[nowV] == -1:
                self.inTime[nowV] = u
            self.verticeEulerTour.append(nowV)
            if p[nowV] == self.childNum[nowV]:
                self.outTime[nowV] = u + 1
                nowV = self.parent[nowV]
            else:
                t = p[nowV]
                p[nowV] += 1
                nowV = self.child[nowV][t]
            if nowV != -1:
                self.edgeEulerTour.append((tmp, nowV))
            u += 1
    def __init__(self, parent):
        self.n = len(parent)
        self.root = -1
        self.parent = [-1]*self.n
        self.child = [[] for _ in range(self.n)]
        self.childNum = [0]*self.n
        self.depth = [0]*self.n
        self.childCount = [1]*self.n
        self.inTime = [-1]*self.n
        self.outTime = [-1]*self.n
        self.verticeEulerTour = []
        self.edgeEulerTour = []
        for i in range(self.n):
            if parent[i] == -1:
                self.root = i
                continue
            self.parent[i] = parent[i]
            self.child[parent[i]].append(i)
            self.childCount[parent[i]] += 1
            self.childNum[parent[i]] += 1
        self._RootedTree_calculateChildCount()
        self._RootedTree_setEulerTour()
