class StronglyConnectedComponents:
    def __init__(self, n, graph):
        self.n = n
        self.rightPath = [[] for _ in range(self.n)]
        self.oppositePath = [[] for _ in range(self.n)]
        self.rightCount = [0]*self.n
        self.oppositeCount = [0]*self.n
        self.verticeId = [-1]*self.n
        self.idVertice = [-1]*self.n
        self.groupId = [-1]*self.n
        for i in graph:
            self.rightPath[i[0]].append(i[1])
            self.oppositePath[i[1]].append(i[0])
            self.rightCount[i[0]] += 1
            self.oppositeCount[i[1]] += 1
    def decompose(self):
        p = 0
        isVisited = [False]*self.n
        pos = [0]*self.n
        counter = 0
        previous = [-1]*self.n
        # dfs
        while p < self.n:
            if isVisited[p]:
                p += 1
                continue
            isVisited[p] = True
            t = p
            while pos[p] < self.rightCount[p]:
                x = pos[t]
                if x == self.rightCount[t]:
                    self.verticeId[t] = counter
                    self.idVertice[counter] = t
                    counter += 1
                    t = previous[t]
                    pos[t] += 1
                    continue
                v = self.rightPath[t][x]
                if isVisited[v]:
                    pos[t] += 1
                    continue
                previous[v] = t
                isVisited[v] = True
                t = v
            self.verticeId[p] = counter
            self.idVertice[counter] = p
            counter += 1
        # rdfs
        p = self.n - 1
        isVisited = [False]*self.n
        pos = [0]*self.n
        gc = 0
        while p >= 0:
            u = self.idVertice[p]
            if isVisited[u]:
                p -= 1
                continue
            isVisited[u] = True
            t = u
            self.groupId[u] = gc
            while pos[u] < self.oppositeCount[u]:
                x = pos[t]
                if x == self.oppositeCount[t]:
                    t = previous[t]
                    pos[t] += 1
                    continue
                v = self.oppositePath[t][x]
                if isVisited[v]:
                    pos[t] += 1
                    continue
                previous[v] = t
                isVisited[v] = True
                self.groupId[v] = gc
                t = v
            self.groupId[u] = gc
            gc += 1
    def getTopologicalSort(self):
        m = max(self.groupId) + 1
        res = [[] for _ in range(m)]
        for i in range(self.n):
            res[self.groupId[i]].append(i)
        return res
