from collections import deque

wordMap = {
    'A': 0,
    'B': 1,
    'C': 2,
    'D': 3,
    'E': 4,
}

def bfs(adjList, starting_node, visited):
    # make a queue
    q = deque()
    
    # visit the starting node
    q.append(starting_node)
    visited[wordMap[starting_node]] = True
    
    # while the queue is not empty
    while q:
        # pop the node currently in queue and print it
        current_node = q.popleft()
        print(current_node, end=' ')
        
        # visit its neighbours
        for node in adjList[wordMap[current_node]]:
            if not visited[wordMap[node]]:
                visited[wordMap[node]] = True
                q.append(node)


# Function to add an edge to the graph
def addEdge(adjList, u, v):
    adjList[wordMap[u]].append(v)


if __name__ == "__main__":
    # Number of vertices in the graph
    vertices = 5

    # Adjacency list representation of the graph
    adjList = [[] for _ in range(vertices)]

    # Add edges to the graph
    addEdge(adjList, 'A', 'B')
    addEdge(adjList, 'A', 'C')
    addEdge(adjList, 'B', 'D')
    addEdge(adjList, 'B', 'E')
    addEdge(adjList, 'C', 'E')
    addEdge(adjList, 'D', 'E')

    # Mark all the vertices as not visited
    visited = [False] * vertices

    # Perform BFS traversal starting from vertex 0
    print("Breadth First Traversal starting from vertex A:", end=" ")
    bfs(adjList, 'A', visited)
    
    # for arr in adjList:
    #     for node in arr:
    #         print(visited[wordMap[node]])