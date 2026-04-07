"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        length = len(grid)
        topLeft = None
        topRight = None
        bottomLeft = None
        bottomRight = None
        
        if length == 1:
            return Node(grid[0][0], True, None, None, None, None)

        
        mid = length // 2
        quadrant = [[0 for i in range(mid)] for j in range(mid)] 
        print(grid)
        print(quadrant)
        isLeaf = True
        sameValues = set()
        
        # top left
        cur = grid[0][0]
        split = False
        for i in range(mid):
            for j in range(mid):
                quadrant[i%mid][j%mid] = grid[i][j]
                if grid[i][j] != cur:
                    split = True
                    isLeaf = False
        
        if not split:
            topLeft = Node(cur, True, None, None, None, None)
            sameValues.add(cur)
        else:
            topLeft = self.construct(quadrant[:])

        # top right
        cur = grid[0][mid]
        split = False
        for i in range(mid):
            for j in range(mid, length):
                quadrant[i%mid][j%mid] = grid[i][j]
                if grid[i][j] != cur:
                    split = True
                    isLeaf = False
        
        if not split:
            topRight = Node(cur, True, None, None, None, None)
            sameValues.add(cur)
        else:
            topRight = self.construct(quadrant[:])

        # bottom left
        cur = grid[mid][0]
        split = False
        for i in range(mid, length):
            for j in range(mid):
                quadrant[i%mid][j%mid] = grid[i][j]
                if grid[i][j] != cur:
                    split = True
                    isLeaf = False
        
        if not split:
            bottomLeft = Node(cur, True, None, None, None, None)
            sameValues.add(cur)
        else:
            bottomLeft = self.construct(quadrant[:])

        # bottom right
        cur = grid[mid][mid]
        split = False
        for i in range(mid, length):
            for j in range(mid, length):
                quadrant[i%mid][j%mid] = grid[i][j]
                if grid[i][j] != cur:
                    split = True
                    isLeaf = False
        
        if not split:
            bottomRight = Node(cur, True, None, None, None, None)
            sameValues.add(cur)
        else:
            bottomRight = self.construct(quadrant[:])

        if len(sameValues) > 1:
            isLeaf = False
        
        if isLeaf:
            topLeft, topRight, bottomLeft, bottomRight = None, None, None, None
            
        
        return Node(grid[0][0], isLeaf, topLeft, topRight, bottomLeft, bottomRight)