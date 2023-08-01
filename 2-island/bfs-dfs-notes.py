from collections import defaultdict, deque


g = {
    'a': ['c', 'b'],
    'b': ['d'],
    'c': ['e'],
    'd': ['f'],
    'e': [],
    'f': []
}

def dfs(graph, source):
  stack = [source]
  while stack:
    current = stack.pop()
    print(current)
    for neighbor in graph[current]:
       stack.append(neighbor)

# dfs(g, 'a')


def dfs_recursive(graph, source):
  print(source)

  for neighbor in graph[source]:
    dfs_recursive(graph, neighbor)

# dfs_recursive(g, 'a')


def bfs(graph, source):
  q = deque(source)
  while q:
    current = q.pop()
    print(current)
    for neighbor in graph[current]:
      q.appendleft(neighbor)
# bfs(g, 'a')

def graph_has_path(graph, src, dst):
  if src == dst:
    return True
  for neighbor in graph[src]:
    return graph_has_path(graph, neighbor, dst)
  return False

# print(graph_has_path(g, 'c', 'f'))

def graph_has_path_bfs(graph, src, dst):
  q = deque(src)
  while q:
    current = q.pop()
    if current == dst:
      return True
    for neighbor in graph[current]:
      q.appendleft(neighbor)
  return False
# print(graph_has_path_bfs(g, 'a', 'e'))

edges = [['i', 'j'], ['k', 'i'], ['m', 'k'], ['k', 'l'], ['o', 'n']]
adjacency_list = defaultdict(list)

for src, dst in edges:
  adjacency_list[src].append(dst)
  adjacency_list[dst].append(src)

print(adjacency_list)
def graph_has_path_undirected(graph, src, dst, seen = set()):
  if src in seen:
    return False
  if src == dst:
    return True
  seen.add(src)

  for neighbor in graph[src]:
      return graph_has_path_undirected(graph, neighbor, dst, seen)
  return False

print(graph_has_path_undirected(adjacency_list, 'i', 'l'))