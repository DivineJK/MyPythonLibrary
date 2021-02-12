class value_first_01knapsack:
    def __init__(self, weight_limit, value_sum):
        self.wl = weight_limit
        self.vs = value_sum
        self.minimum_weight = [weight_limit+1]*(value_sum+1)
        self.minimum_weight[0] = 0
        self.total_value = 0
    def add_item(self, w, v):
        for i in range(self.total_value, -1, -1):
            if self.minimum_weight[i+v] > self.minimum_weight[i] + w:
                self.minimum_weight[i+v] = self.minimum_weight[i] + w
        self.total_value += v
    def solver(self):
        p = self.vs
        while self.minimum_weight[p] > self.wl:
            p -= 1
        return p
