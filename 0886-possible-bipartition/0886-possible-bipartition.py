class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        def bfs(i):     
            q = deque([i])
            color[i] = -1
            while q:
                node = q.popleft()
                for neighbor in adjList[node]:
                    if color[node] == color[neighbor]:
                        return False

                    if color[neighbor] == 0:
                        q.append(neighbor)

                    if color[node] == -1:
                        color[neighbor] = 1

                    else:
                        color[neighbor] = -1

            return True

        adjList = [[] for _ in range(n + 1)]
        for n1, n2 in dislikes:
            adjList[n1].append(n2)
            adjList[n2].append(n1)

        color = [0] * (n + 1)
        for i in range(1, n + 1):
            if color[i] == 0:
                if not bfs(i):
                    return False

        return True