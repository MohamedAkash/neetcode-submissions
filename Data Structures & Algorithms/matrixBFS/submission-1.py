class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        queue = deque()
        queue.append((0,0))
        visit.add((0,0))

        length = 0
        while queue:
            for i in range(len(queue)):
                r,c = queue.popleft()
                if r == ROWS - 1 and c == COLS - 1:
                    return length

                neighbors = [[0,1],[0,-1],[1,0],[-1,0]]
                for dr, dc in neighbors:
                    if (min(dr+r, dc+c) < 0 or 
                        dr+r == ROWS or dc+c == COLS or 
                        (dr+r,dc+c) in visit or
                        grid[r+dr][c+dc] == 1 
                        ):
                        continue
                    queue.append((dr+r, dc+c))
                    visit.add((dr+r, dc+c))
            length += 1
        return -1
