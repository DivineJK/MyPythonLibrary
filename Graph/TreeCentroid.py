import sys
input = sys.stdin.readline
class tree_centroid:
    def __init__(self, n, tree=[]):
        self.n = n
        self.tree = tree
        if tree == []:
            self.tree = [[] for _ in range(n)]
        self.subtree_size = [0]*n
        self.centroids = []
        self.rank = [-1]*n
    def sub_tree_centroid(self, v, par=-1):
        self.subtree_size[v] = 1
        is_centroid = True
        for child in self.tree[v]:
            if child == par:
                continue
            self.sub_tree_centroid(child, v)
            if self.subtree_size[child] > self.n // 2:
                is_centroid = False
            self.subtree_size[v] += self.subtree_size[child]
        if self.n - self.subtree_size[v] > self.n // 2:
            is_centroid = False
        if is_centroid:
            self.centroids.append(v)
    def get_tree_centroid(self):
        self.centroids = []
        self.sub_tree_centroid(0, N)
    def bfs(self, v):
        self.rank = [-1]*self.n
        self.rank[v] = 0
        st = [v]
        cnt = 1
        pnt = 0
        while pnt < cnt:
            m = cnt
            for i in range(pnt, cnt):
                c = st[i]
                for j in self.tree[c]:
                    if self.rank[j] < 0:
                        self.rank[j] = self.rank[c] + 1
                        cnt += 1
                        st.append(j)
            pnt = m
