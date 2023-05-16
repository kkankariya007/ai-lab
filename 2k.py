#Graph Colouring-hi

def can_color(graph, node, color, coloring):
    for adjacent in graph[node]:
        if coloring[adjacent] == color:
            return False
    return True

def graph_coloring(graph, colors, coloring, node=0):
    if node == len(graph):
        return coloring
    
    for color in colors:
        if can_color(graph, node, color, coloring):
            coloring[node] = color
            result = graph_coloring(graph, colors, coloring, node+1)
            if result is not None:
                return result
    
    return None

graph = {
    0: [1,2],
    1: [0,2,4],
    2: [0,1,4],
    3: [4],
    4: [1,2,3]
}
colors = ['red', 'gh']
coloring = [None] * len(graph)

result = graph_coloring(graph, colors, coloring)
print(result)