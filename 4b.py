from collections import defaultdict

def tsp_bfs(graph, start):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for neighbor in graph[vertex] - set(path):
            if len(path) == len(graph) - 1:
                yield path + [neighbor]
            else:
                queue.append((neighbor, path + [neighbor]))

def tsp_dfs(graph, start, path=[]):
    path = path + [start]
    if len(path) == len(graph):
        yield path
    for neighbor in graph[start] - set(path):
        yield from tsp_dfs(graph, neighbor, path)

def tsp(graph, start, method="bfs"):
    if method == "bfs":
        return tsp_bfs(graph, start)
    elif method == "dfs":
        return tsp_dfs(graph, start)

if __name__ == "__main__":
    graph = defaultdict(set)
    # edges = [("A", "B"), ("A", "C"), ("B", "C"), ("C", "D")]
    edges = [("A", "B"), ("A", "C"), ("B", "C"),("B","E"),("C", "D"),("D","E")]
    # edges=[]

    for edge in edges:
        graph[edge[0]].add(edge[1])
        graph[edge[1]].add(edge[0])

    for path in tsp(graph, "A", method="bfs"):
        print(" -> ".join(path))
    print("---")
    for path in tsp(graph, "A", method="dfs"):
        print(" -> ".join(path))