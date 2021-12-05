class Stack:
    def __init__(self, l=[]):
        self.array = []
        self.back = len(l)-1
        self.size = len(l)
        for i, k in enumerate(l):
            self.array.append(k)
    def clear(self):
        self.array = []
        self.back = -1
        self.size = 0
    def getSize(self):
        return self.back + 1
    def pop(self):
        res = self.array[self.back]
        self.back -= 1
        return res
    def top(self):
        return self.array[self.back]
    def push(self, val):
        if self.back + 1 >= self.size:
            self.array.append(val)
            self.back += 1
            self.size += 1
        else:
            self.back += 1
            self.array[self.back] = val
