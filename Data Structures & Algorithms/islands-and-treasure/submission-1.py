class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        treasure_chests = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    treasure_chests.append(tuple((i, j)))
        if not treasure_chests:
            return
        queue = deque()
        queue.append(treasure_chests)
        self.bfs(queue, grid)

    def bfs(self, queue, grid):
        distance = 0
        visited = set()

        while queue:
            level = queue.popleft()
            next_level = []
            
            for pos in level:
                row, col = pos
                if distance > grid[row][col] or pos in visited:
                    continue

                visited.add(pos)
                grid[row][col] = distance

                if row + 1 < len(grid) and grid[row + 1][col] != -1 and grid[row + 1][col] > distance + 1:
                    next_level.append(tuple((row + 1, col)))
                if row - 1 >= 0 and grid[row - 1][col] != -1 and grid[row - 1][col] > distance + 1:
                    next_level.append(tuple((row - 1, col)))
                if col + 1 < len(grid[0]) and grid[row][col + 1] != -1 and grid[row][col + 1] > distance + 1:
                    next_level.append(tuple((row, col + 1)))
                if col - 1 >= 0 and grid[row][col - 1] != -1 and grid[row][col - 1] > distance + 1:
                    next_level.append(tuple((row, col - 1)))
            if next_level:
                queue.append(next_level)
            distance += 1


                





        
        