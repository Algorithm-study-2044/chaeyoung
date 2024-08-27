class Solution:
    def pacificAtlantic(self, heights):
        rows, cols = len(heights), len(heights[0])

        def dfs(i, j, visited, ocean):
            if i < 0 or i >= rows or j < 0 or j >= cols or visited[i][j] or heights[i][j] < ocean:
                return False
            visited[i][j] = True
            if dfs(i - 1, j, visited, heights[i][j]) or dfs(i, j - 1, visited, heights[i][j]) or dfs(i + 1, j, visited,
                                                                                                     heights[i][
                                                                                                         j]) or dfs(i,
                                                                                                                    j + 1,
                                                                                                                    visited,
                                                                                                                    heights[
                                                                                                                        i][
                                                                                                                        j]):
                return True
            return False

        pacific = [[False for _ in range(cols)] for _ in range(rows)]
        atlantic = [[False for _ in range(cols)] for _ in range(rows)]

        for i in range(rows):
            dfs(i, 0, pacific, 0)
            dfs(i, cols - 1, atlantic, 0)

        for j in range(cols):
            dfs(0, j, pacific, 0)
            dfs(rows - 1, j, atlantic, 0)

        res = []
        for i in range(rows):
            for j in range(cols):
                if pacific[i][j] and atlantic[i][j]:
                    res.append([i, j])
        return res