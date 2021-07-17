class tree_diameter:
    def __init__(self, n):
        self.n = n
        self.graph = [[] for _ in range(n)]
        self.dist_d = {}
        self.prev = [-2]*self.n
        self.diameter = [0]*self.n
        self.dest_node = -1
    def connect_edge(self, a, b, c=1, directed=False):
        self.graph[a].append(b)
        self.dist_d[a*self.n+b] = c
        if not directed:
            self.graph[b].append(a)
            self.dist_d[b*self.n+a] = c
    def calc_diameter(self, x):
        st = [x]
        pnt = 0
        cnt = 1
        flg = [True]*self.n
        flg[x] = False
        dist = [0]*self.n
        md = 0
        nd = x
        while pnt < cnt:
            n = cnt
            for i in range(pnt, cnt):
                c = st[i]
                for j in self.graph[c]:
                    if flg[j]:
                        flg[j] = False
                        dist[j] = dist[c] + self.dist_d[c*self.n+j]
                        if md < dist[c] + self.dist_d[c*self.n+j]:
                            md = dist[c] + self.dist_d[c*self.n+j]
                            nd = j
                        st.append(j)
                        cnt += 1
            pnt = n
        st = [nd]
        pnt = 0
        cnt = 1
        self.diameter[nd] = 0
        self.prev[nd] = -1
        res = 0
        self.dest_node = nd
        while pnt < cnt:
            n = cnt
            for i in range(pnt, cnt):
                c = st[i]
                for j in self.graph[c]:
                    if self.prev[j] == -2:
                        self.prev[j] = c
                        self.diameter[j] = self.diameter[c] + self.dist_d[c*self.n+j]
                        if res < self.diameter[j]:
                            res = self.diameter[j]
                            self.dest_node = j
                        st.append(j)
                        cnt += 1
            pnt = n
        return res
    def restore_path(self):
        res = [self.dest_node]
        c = self.prev[self.dest_node]
        while c >= 0:
            res.append(c)
            c = self.prev[c]
        res.reverse()
        return res
