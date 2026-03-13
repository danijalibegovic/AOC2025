import sys
sys.setrecursionlimit(10**7)

END = "out"

from functools import lru_cache

def count_paths(graph, start):
    @lru_cache(None)
    def dp(node, dac, fft):
        # update flags
        if node == "dac":
            dac = True
        if node == "fft":
            fft = True

        # if this node leads directly to out
        if graph[node] == [END]:
            return 1 if (dac and fft) else 0

        total = 0
        for nxt in graph[node]:
            total += dp(nxt, dac, fft)
        return total

    return dp(start, False, False)

graph = {}

with open("reactor.txt", "r", encoding="utf-8") as f:
    for line in f:
        key = line[:3]
        values = line[4:].split()
        graph[key] = values

print(count_paths(graph, "svr"))
