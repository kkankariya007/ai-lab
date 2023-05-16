def isBipartite(src,graph):
    colorArr = [-1] * len(graph)
 
        
    colorArr[src] = 1

    queue = []
    queue.append(src)
 
    while queue:
        u = queue.pop()
 
        if graph[u][u] == 1:
            return False;
 
        for v in range(len(graph)):
 
            if graph[u][v] == 1 and colorArr[v] == -1:
 
                colorArr[v] = 1 - colorArr[u]
                queue.append(v)
 
            elif graph[u][v] == 1 and colorArr[v] == colorArr[u]:
                return False

    return True


graph=[[0, 1, 0, 1],[1, 0, 1, 0],[0, 1, 0, 1],[1, 0, 1, 0]]
if isBipartite(0,graph):
    print("Yes")
else:
    print("No")
