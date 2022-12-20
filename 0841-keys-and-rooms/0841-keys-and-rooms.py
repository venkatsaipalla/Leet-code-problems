class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        keys=rooms[0]
        visited=[False]*len(rooms)
        visited[0]=True
        while keys!=[]:
            x=keys.pop()
            if not visited[x]:
                visited[x]=True
                keys+=rooms[x]
        return all(visited)