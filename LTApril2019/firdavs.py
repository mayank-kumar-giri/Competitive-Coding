class Graph():
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]

    def minDistance(self, dist, sptSet):
        mini = 999999999
        for v in range(self.V):
            if dist[v] < mini and sptSet[v] == False:
                mini = dist[v]
                min_index = v
        return min_index

    def answer(self, qv, dist):
        return dist[qv]

    def dijkstra(self, src, dist):
        dist[src] = 0
        sptSet = [False] * self.V

        for cout in range(self.V):
            u = self.minDistance(dist, sptSet)

            sptSet[u] = True

            for v in range(self.V):
                if self.graph[u][v] > 0 and sptSet[v] == False and dist[v] > dist[u] + self.graph[u][v]:
                    dist[v] = dist[u] + self.graph[u][v]
        return dist


t = int(input())
for i in range(t):
    n,q = map(int, input().split())
    v = list(map(int, input().split()))
    gra = [[0 for pp in range(n)] for qq in range(n)]
    for j in range(n):
        for k in range(n):
            gra[j][k] = abs(v[j]-v[k]) + (k-j)

    g = Graph(n)
    g.graph = gra
    for j in range(q):
        x,y = map(int, input().split())
        dist = [999999999] * n
        dist = g.dijkstra(x-1, dist)
        print(g.answer(y-1, dist))