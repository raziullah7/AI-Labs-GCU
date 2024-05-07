def DFS(graph, start, visited=None):
    # for the time when DFS is called from main function
    if visited is None:
        visited = set()
    
    # add the node to visited set and print it
    visited.add(start)
    print(start, end=" ")
    
    # getting the set accociated with the passed node
    for n in graph.get(start, set()):
        if n not in visited:
            # recursively going through the depth
            DFS(graph, n, visited)


if __name__ == "__main__":
    # making the graph (which is a dictionary)
    graph = {
        'A': set(['B', 'E', 'C']),
        'B': set(['A', 'E', 'D']),
        'C': set(['F', 'G']),
        'D': set(['B', 'E']),
        'E': set(['A', 'B', 'D']),
        'F': set(['C']),
        'G': set(['C']),
    }
    
    # calling the DFS function
    DFS(graph, 'A')