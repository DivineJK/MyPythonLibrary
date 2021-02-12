class weight_first_01knapsack:
    def __init__(self, weight_limit):
        self.wl = weight_limit
        self.maximum_value = [0]*(weight_limit+1)
        self.res = 0
    def add_item(self, w, v):
        if w <= self.wl:
            for i in range(self.wl-w, -1, -1):
                if self.maximum_value[i+w] < self.maximum_value[i] + v:
                    self.maximum_value[i+w] = self.maximum_value[i] + v
                    if self.res < self.maximum_value[i+w]:
                        self.res = self.maximum_value[i+w]
    def solver(self):
        return self.res
