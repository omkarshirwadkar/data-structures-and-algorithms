def buildAdjacencyMatrix(n, m, edges):
    adjacencyMatrix = [[0] * (n + 1) for _ in range(n + 1)]
    for _ in range(m):
        a, b = edges[_]
        adjacencyMatrix[a][b] = 1
        # Remove the below line for Undirected Graphs
        adjacencyMatrix[b][a] = 1
    return adjacencyMatrix

def buildWeightedAdjacencyMatrix(n, m, edges, weights):
    adjacencyMatrix = [[0] * (n + 1) for _ in range(n + 1)]
    for _ in range(m):
        a, b = edges[_]
        adjacencyMatrix[a][b] = weights[_]
        # Remove the below line for Undirected Graphs
        adjacencyMatrix[b][a] = weights[_]
    return adjacencyMatrix

def printAdjacencyMatrix(n, m, edges):
    adjacencyMatrix = buildAdjacencyMatrix(n, m, edges)
    for i in range(n + 1):
        print(adjacencyMatrix[i])


def buildAdjacencyList(n, m, edges):
    adjacencyList = [[] for i in range(n + 1)]
    for _ in range(m):
        a, b = edges[_]
        adjacencyList[a].append(b)
        # Remove the below line for Undirected Graphs
        adjacencyList[b].append(a)
    return adjacencyList

def buildWeightedAdjacencyList(n, m, edges, weights):
    adjacencyList = [[] for i in range(n + 1)]
    for _ in range(m):
        a, b = edges[_]
        adjacencyList[a].append([b, weights[_]])
        # Remove the below line for Undirected Graphs
        adjacencyList[b].append([a, weights[_]])
    return adjacencyList

def printAdjacencyList(n, m, edges):
    adjacencyList = buildAdjacencyList(n, m, edges)
    for i in range(n + 1):
        print(adjacencyList[i])

n, m = [int(x) for x in input("Enter number of nodes and number of edges: ").split()]
edges = []
for _ in range(m):
    a, b = [int(x) for x in input().split()]
    edges.append([a, b])
print("Adjacency Matrix:")
printAdjacencyMatrix(n, m, edges)
print("Weighted Adjacency Matrix:")
print("Adjacency List:")
printAdjacencyList(n, m, edges)