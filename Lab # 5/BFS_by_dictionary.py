from collections import deque


def bfs(graph, starting_node):
    # setup the queue and the visited set
    visited = set()
    queue = deque([starting_node])
    
    # visit the starting node
    visited.add(starting_node)
    
    # print the starting_node
    while queue:
        # pop the queue and print the element
        current_node = queue.popleft()
        print(current_node, end=' ')
        
        # enqueue the adjacent elements of current_node into the visited set
        for node in graph[current_node]:
            if node not in visited:
                queue.append(node)
                visited.add(node)
        


if __name__ == '__main__':
    graph = {
        0: [1, 2],
        1: [3, 4],
        2: [4],
        3: [],
        4: [],
    }

    # graph = {
    #     'a': ['b', 'c'],
    #     'b': ['d', 'e'],
    #     'c': ['e'],
    #     'd': [],
    #     'e': [],
    # }
        
    print("BFS Traversal from 0: ", end=' ')
    bfs(graph, 0)