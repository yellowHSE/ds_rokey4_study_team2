from collections import deque

def solution(maps):
    
    rows, cols = len(maps), len(maps[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = deque([(0, 0, 1)])
    visited = {(0, 0)}

    while queue:
        posX, posY, dist = queue.popleft()
        if (posX, posY) == (rows - 1, cols - 1):
            return dist
        for dx, dy in directions:
            nx, ny = posX + dx, posY + dy
            if 0 <= nx < rows and 0 <= ny < cols and maps[nx][ny] == 1 and (nx, ny) not in visited:
                queue.append((nx, ny, dist + 1))
                visited.add((nx, ny))
    return -1