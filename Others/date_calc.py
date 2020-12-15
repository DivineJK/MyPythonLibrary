class date_calc:
    def __init__(self):
        self.days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        self.days_sum = [0]*13
        for i in range(12):
            self.days_sum[i+1] = self.days_sum[i] + self.days[i]
        self.leap_days = [365+(((i%100!=0)and(i%4==0))or(i%400==0)) for i in range(400)]
        self.leap_sum = [0]*401
        for i in range(400):
            self.leap_sum[i+1] = self.leap_sum[i] + self.leap_days[i]
    def IsLeap(self, n):
        if n % 400 == 0:
            return True
        if n % 100 == 0:
            return False
        if n % 4 == 0:
            return True
    def trim_date(self, year, month, day, realistic=False):
        y, m, d = year, month, day
        d -= 1
        y += (m - 1) // 12
        m = (m - 1) % 12
        if self.IsLeap(y):
            if m >= 2:
                d += 1
        d += self.days_sum[m]
        d += self.leap_sum[y%400]
        m = 0
        y = (y // 400) * 400
        y += d // self.leap_sum[-1]
        d %= self.leap_sum[-1]
        left, right = 0, 401
        mid = (left + right) // 2
        while right - left > 1:
            if self.leap_sum[mid] <= d:
                left = mid
            else:
                right = mid
            mid = (left + right) // 2
        y += mid
        d -= self.leap_sum[mid]
        for i in range(12):
            tmp = self.days[i]
            if i == 1 and self.IsLeap(y):
                tmp += 1
            if d >= tmp:
                d -= tmp
                m += 1
            else:
                break
        if realistic:
            res_y = y
            if res_y <= 0:
                res_y -= 1
            return (res_y, m+1, d+1)
        return (y, m, d)
    def date_serial(self, year, month, day):
        # year = 1, month = 0 -> year = 0, month = 12
        # year = -1 -> year = 0
        # (year, month, day) = (0, 1, 1) -> serial = 0
        td = self.trim_date(year, month, day)
        y, m, d = td[0], td[1], td[2]
        d += self.days_sum[m]
        if self.IsLeap(y) and m >= 2:
            d += 1
        d += (y // 400) * self.leap_sum[-1]
        y %= 400
        d += self.leap_sum[y]
        return d
