class Heap_max:
    def __init__(self, B=[]):
        self.A = B

    def __str__(self):
        return str(self.A)

    def find_max(self):
        return self.A[0]

    def heapify_down(self, k, n):
        while 2 * k + 1 < n:
            L = 2 * k + 1
            R = 2 * k + 2
            if L < n and self.A[k] < self.A[L]:
                m = L
            else:
                m = k
            if R < n and self.A[m] < self.A[R]:
                m = R
            if k != m:
                self.A[k], self.A[m] = self.A[m], self.A[k]
                k = m
            else:
                break

    def heapify_up(self, k):
        while k > 0 and self.A[(k - 1) // 2] < self.A[k]:
            self.A[k], self.A[(k - 1) // 2] = self.A[(k - 1) // 2], self.A[k]
            k = (k - 1) // 2

    def insert(self, key):
        self.A.append(key)
        self.heapify_up(len(self.A) - 1)

    def make_Heap(self):
        n = len(self.A)
        for k in range(n - 1, -1, -1):
            self.heapify_down(k, n)

    def delete_max(self):
        if len(self.A) == 0: return None
        key = self.A[0]
        self.A[0], self.A[len(self.A) - 1] = self.A[len(self.A) - 1], self.A[0]
        self.A.pop()
        self.heapify_down(0, len(self.A))
        return key

    def __len__(self):
        return len(self.A)


class Heap_min:
    def __init__(self, B=[]):
        self.A = B

    def __str__(self):
        return str(self.A)

    def find_min(self):
        return self.A[0]

    def heapify_down(self, k, n):
        while 2 * k + 1 < n:
            L = 2 * k + 1
            R = 2 * k + 2
            if L < n and self.A[k] > self.A[L]:
                ni = L
            else:
                ni = k
            if R < n and self.A[ni] > self.A[R]:
                ni = R
            if k != ni:
                self.A[k], self.A[ni] = self.A[ni], self.A[k]
                k = ni
            else:
                break

    def heapify_up(self, k):
        while k > 0 and self.A[(k - 1) // 2] > self.A[k]:
            self.A[k], self.A[(k - 1) // 2] = self.A[(k - 1) // 2], self.A[k]
            k = (k - 1) // 2

    def insert(self, key):
        self.A.append(key)
        self.heapify_up(len(self.A) - 1)

    def make_Heap(self):
        n = len(self.A)
        for k in range(n - 1, -1, -1):
            self.heapify_down(k, n)

    def delete_min(self):
        if len(self.A) == 0: return None
        key = self.A[0]
        self.A[0], self.A[len(self.A) - 1] = self.A[len(self.A) - 1], self.A[0]
        self.A.pop()
        self.heapify_down(0, len(self.A))
        return key

    def __len__(self):
        return len(self.A)