class Solution:
    def matrixMul(self, a, b):
        ans = [[0] * 3 for _ in range(3)]
        for i in range(3):
            for j in range(3):
                for k in range(3):
                    ans[i][j] += a[i][k] * b[k][j]
                ans[i][j] %= 1000000007
        return ans

    def quickMul(self, matrix, x):
        ans = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
        while x:
            if x & 1:
                ans = self.matrixMul(ans, matrix)
            x >>= 1
            matrix = self.matrixMul(matrix, matrix)
        return ans

    def waysToStep(self, n: int) -> int:
        if n < 3:
            return n
        ans = self.quickMul([[0, 0, 1], [1, 0, 1], [0, 1, 1]], n - 2)
        return (ans[0][2] + ans[1][2] + ans[2][2] * 2) % 1000000007


class Solution_two:
    def waysToStep(self, n: int) -> int:
        if n <= 2:
            return n
        if n == 3:
            return 4
        f1, f2, f3 = 1, 2, 4
        mod = 10 ** 9 + 7
        for _ in range(n - 3):
            f1, f2, f3 = f2, f3, (f1 + f2 + f3) % mod

        return f3