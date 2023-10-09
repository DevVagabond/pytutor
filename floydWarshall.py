class FWGraph:
    def __init__(self,  v):
        self.V = int(v)+1
        self.A = [[[float("inf")] * self.V for _ in range(self.V)] for _ in range(self.V)]

    def setWeightMatrix(self,   m):
        for i in range(1, self.V):
            for j in range(1, self.V):
                self.A[0][i][j] = m[i - 1][j - 1]

    def calculateAllPairShortestPath(self):
        for k in range(1, len(self.A)):
            for i in range(1, len(self.A[k])):
                for j in range(1, len(self.A[k][i])):
                    if self.A[k-1][i][k] + self.A[k-1][k][j] < self.A[k-1][i][j]:
                        self.A[k][i][j] = self.A[k-1][i][k] + self.A[k-1][k][j]
                    else:
                        self.A[k][i][j] = self.A[k-1][i][j]

    def printCstGraph(self):
        for i in range(1, len(self.A[-1])):
            print(self.A[-1][i][1:])


g = FWGraph(4)

g.setWeightMatrix([
    [0, 3,  float("inf"), 7],
    [8, 0,  2,  float("inf")],
    [5, 8,  0,  1],
    [2, float("inf"), float("inf"), 0]
])

g.calculateAllPairShortestPath()
g.printCstGraph()
