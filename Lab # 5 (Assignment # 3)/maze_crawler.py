from collections import deque
maze = [
[0, 1, 0, 0, 0, 1],
[0, 1, 0, 1, 0, 1],
[0, 0, 0, 1, 0, 0],
[0, 1, 0, 1, 1, 0],
[0, 1, 0, 0, 0, 0],
[1, 1, 1, 1, 1, 0]
]
start = (0, 0)
end = (5, 5)
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def is_valid_move(x, y, maze, visited):
    return 0 <= x < len(maze) and 0 <= y < len(maze[0]) and maze[x][y] == 0 and not visited[x][y]


def bfs(maze, start, end):
    queue = deque([start])
    visited = [[False for _ in range(len(maze[0]))] for _ in range(len(maze))]
    visited[start[0]][start[1]] = True
    parent = {start: None}
    while queue:
        current = queue.popleft()
        if current == end:
            path = []
            while current:
                path.append(current)
                current = parent[current]
            return path[::-1]
        
        for direction in directions:
            next_x, next_y = current[0] + direction[0], current[1] + direction[1]
            
            if is_valid_move(next_x, next_y, maze, visited):
                queue.append((next_x, next_y))
                visited[next_x][next_y] = True
                parent[(next_x, next_y)] = current
                
    return None


path = bfs(maze, start, end)
if path:
    print("Path to exit the maze:")
for step in path:
    print(step)
else:
    print("No path found from start to end.")