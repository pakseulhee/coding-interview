"""
     4
    / \
   1   5
  / \   \
 2   3   9

"""

vertice = [4,1,5,2,3,9]
adj_list = {}
adj_list[4] = [1,5]
adj_list[1] = [2,3]
adj_list[5] = [9]
adj_list[2] = []
adj_list[3] = []
adj_list[9] = []

stack = []
visited = []


def dfs(start):
    stack.append(start)

    while len(stack) > 0:
        cur = stack.pop()
        for neighbor in adj_list[cur]:
            if not neighbor in visited:
                stack.append(neighbor)
        visited.append(cur)

dfs(4)

print(visited)