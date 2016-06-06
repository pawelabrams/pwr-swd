import json

with open('paths.json') as f:
    paths = json.load(f)

print paths

def avg(ls):
    return sum(ls, 0.0) / len(ls)

def find_adjecent(pos):
    adj = []
    for path in paths:
        if path.split("-")[0] == pos:
            adj.append(path.split("-")[1])
    return adj

def dijkstra(paths, vertex="51.11,17.02"):
    queue = set()
    dist = dict()
    prev = dict()

    def min_dist():
        min = next(iter(queue))
        for u in queue:
            if dist[u] < dist[min]:
                min = u
        return min

    for path in paths:
        derp = path.split("-")
        dist[derp[0]] = float('inf')
        prev[derp[0]] = None
        queue.add(derp[0])
        dist[derp[1]] = float('inf')
        prev[derp[1]] = None
        queue.add(derp[1])

    dist[vertex] = 0

    while queue:
        u = min_dist()
        queue.remove(u)
        adjs = find_adjecent(u)

        for v in adjs:
            alt = dist[u] + max(paths[u+"-"+v])
            if not dist[v] or alt < dist[v]:
                dist[v] = alt
                prev[v] = u

    dest = dest_orig = "42.25,11.75"
    path = []
    while prev.has_key(dest):
        path.append(dest)
        dest = prev[dest]
    path.reverse()

    return path, dist[dest_orig]

print dijkstra(paths)