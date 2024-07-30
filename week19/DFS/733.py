class Solution(object):
    def fill_DFS(self, image, r, c, visited, orginal_color, to_color):
        if r > -1 and c > -1 and r < len(image) and c < len(image[0]):
            if visited[r][c] == 0 and image[r][c] == orginal_color:
                image[r][c] = to_color

    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """

        visited = [[0 for _ in range(len(row))] for row in image]

        def fill_DFS(r, c):
            if r > -1 and c > -1 and r < len(image) and c < len(image[0]):
                print(f"[{r},{c}] 인덱스 탐색")
                if visited[r][c] == 0 and image[r][c] == orginal_color:
                    image[r][c] = color
                    visited[r][c] = 1
                    print(f"image changed : {image}")
                    for i, j in fourwaylist:
                        fill_DFS(r + i, c + j)
            return

        orginal_color = image[sr][sc]

        visited[sr][sc] = 1
        image[sr][sc] = color

        fourwaylist = [[-1, 0], [0, -1], [0, 1], [1, 0]]

        for i, j in fourwaylist:
            fill_DFS(sr + i, sc + j)
            
        return image