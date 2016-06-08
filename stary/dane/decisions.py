# coding=utf-8
from __future__ import print_function, unicode_literals
import json

with open('paths.json') as f:
    paths = json.load(f)

for p in paths:
    print (p, " ", paths[p])

def avg(ls):
    return sum(ls, 0.0) / len(ls)

def find_adjecent(pos):
    adj = []
    for path in paths:
        if path.split("-")[0] == pos:
            adj.append(path.split("-")[1])
    return adj

def algo(paths, vertex="51.11,17.02"):
    queue = set()
    dist = dict()
    prev = dict()
    """
    def d(u, v):
        r = avg(paths[u+"-"+v])
        return r if r > 0 else .5
    """
    def d(u, v):
        r = max(paths[u+"-"+v])
        return r if r > 0 else 1
    #"""
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
            alt = dist[u] + d(u,v)
            if alt < dist[v]:
                dist[v] = alt
                prev[v] = u

    dest = dest_orig = "42.25,11.75"
    path = []
    while dest in prev:
        path.append(dest)
        dest = prev[dest]
    path.reverse()

    return path, dist[dest_orig]

path, dist = algo(paths)
for l in path:
    print (l)
print (dist)