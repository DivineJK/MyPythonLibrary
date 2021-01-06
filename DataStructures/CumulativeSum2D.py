class cumulative_sum_2d:
    def __init__(self, h, w, a, get_sum=True):
        self.h = h
        self.w = w
        self.cs = [0]*((w+1)*(h+1))
        for i in range(h):
            for j in range(w):
                self.cs[(i+1)*(w+1)+j+1] = a[i][j]
        if get_sum:
            for i in range(h+1):
                for j in range(w):
                    self.cs[i*(w+1)+j+1] += self.cs[i*(w+1)+j]
            for j in range(w+1):
                for i in range(h):
                    self.cs[(i+1)*(w+1)+j] += self.cs[i*(w+1)+j]
    def c_sum(self, x1, y1, x2, y2):
        return self.cs[x2*(self.w+1)+y2] - self.cs[x1*(self.w+1)+y2] - self.cs[x2*(self.w+1)+y1] + self.cs[x1*(self.w+1)+y1]
