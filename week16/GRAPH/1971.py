class Solution(object):
    def validPath(self, n, edges, source, destination):
        """
        :type n: int
        :type edges: List[List[int]]
        :type source: int
        :type destination: int
        :rtype: bool
        """
        from collections import deque
        visited = [0] * n
        connected_nodes = [[] for i in range(n)]

        for edge in edges:
            connected_nodes[edge[0]].append(edge[1])
            connected_nodes[edge[1]].append(edge[0])

        queue = deque([source])
        visited[source] = 1

        while queue:
            source = queue[0]
            for i in connected_nodes[source]:
                while visited[i] == 0:
                    queue.append(i)
                    visited[i] = 1
            queue.popleft()

        if visited[destination]:
            return True
        else:
            return False















#Union find  알고리즘을 이용하면 더 시간복잡도가 낮음
#디큐 짱임
#스택은 list pop append만 사용해도 ㄱㅊ
#그래프를 구현할 때 dictionary로 구현하고 n by ㅜ 형태의 그래프를 구현하지 않는다 왜?
#linkedlist
#nXn table