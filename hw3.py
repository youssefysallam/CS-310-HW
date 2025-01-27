def findCircleNum(M):
    def dfs(node):
        for neighbor, is_friend in enumerate(M[node]):
            if is_friend and neighbor not in visited:
                visited.add(neighbor)
                dfs(neighbor)

    visited = set()
    circles = 0

    for i in range(len(M)):
        if i not in visited:
            dfs(i)
            circles += 1

    return circles

#TEST [EXAMPLE]
M1 = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
M2 = [[1, 1, 0], [1, 1, 1], [0,1,1]]
print(findCircleNum(M1))
print(findCircleNum(M2))