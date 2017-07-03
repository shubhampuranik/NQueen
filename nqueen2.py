class NQueen(object):
    def __init__(self,n):
        self.n = n
        self.x = []
        for i in range(0, n):
            self.x.append(-1)
        self.output = []

    def place(self, k, i):
        for j in range(0, k):
            if self.x[j] == i or abs(self.x[j]-i) == abs(j-k):
                return False
        return True

    def n_queens(self, k, n):
        for i in range(0, n):
            if self.place(k, i):
                self.x[k] = i
                if k == n-1:
                    y = list(self.x)
                    self.output.append(y)
                    # print self.x
                    return
                else:
                    self.n_queens(k+1, n)

    def get_result(self):
        self.n_queens(0, self.n)
        return self.output

# n = input("enter value of n:")
# q = NQueen(n)
# for i in q.get_result():
#     print i
