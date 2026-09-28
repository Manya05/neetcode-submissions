class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights)
        n = len(heights[0])

        pacific = [[False] *n for _ in range(m)]
        atlantic = [[False]* n for _ in range(m)]

        def dfs(r, c, ocean):
            ocean[r][c] = True
            directions= [(1,0),(-1, 0), (0,1), (0,-1)]

            for dr,dc in directions:
                nr = r+dr
                nc = c+dc
                if nr< 0 or nr>= m or nc<0 or nc>= n:
                    continue
                if ocean[nr][nc] ==True:
                    continue 
                if heights[nr][nc] < heights[r][c]:
                    continue
                dfs(nr,nc,ocean)
        for c in range(n):
            dfs(0,c, pacific)
        for r in range(m):
            dfs(r, 0 , pacific)
        for c in range(n):
            dfs( m-1, c, atlantic)
        for r in range(m):
            dfs(r,n-1,atlantic)
            
        result =[]
        for r in range(m):
            for c in range(n):
                if pacific[r][c] and atlantic[r][c]:
                    result.append([r,c])
        return result