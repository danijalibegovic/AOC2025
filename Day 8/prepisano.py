from collections import defaultdict, Counter
import math
import sys
import timeit
import unittest

pr = print

class Edge:
    def __init__(self, to):
        self.to = to
    def __repr__(self):
        return f"Edge({self.to})"

class Graph:
    def __init__(self, nodes, edges):
        self.nodes = list(nodes)
        self.edges = {k: list(v) for k, v in dict(edges).items()}

    def connected_components(self):
        comp = {}
        cid = 0
        for node in self.nodes:
            if node in comp:
                continue
            stack = [node]
            comp[node] = cid
            while stack:
                u = stack.pop()
                for e in self.edges.get(u, []):
                    v = e.to
                    if v not in comp:
                        comp[v] = cid
                        stack.append(v)
            cid += 1
        return comp


class Tests(unittest.TestCase):
    def setUp(self):
        self.testinput = """162,817,812
                            57,618,57
                            906,360,560
                            592,479,940
                            352,342,300
                            466,668,158
                            542,29,236
                            431,825,988
                            739,650,466
                            52,470,668
                            216,146,977
                            819,987,18
                            117,168,530
                            805,96,715
                            346,949,466
                            970,615,88
                            941,993,340
                            862,61,35
                            984,92,344
                            425,690,689"""
        
        self.test = parse_input(self.testinput.split("\n"))

        self.testinput2 = self.testinput
        self.test2 = parse_input(self.testinput2.split("\n"), p2mode=True)

    def test_part1(self):
        self.assertEqual(part1(self.test), 0)

    def test_part2(self):
        self.assertEqual(part2(self.test2), 0)


def parse_input(inp, p2mode=False):
    o = []
    for idx, line in enumerate(inp):
        line = line.strip()
        if not line:
            continue
        o.append(tuple(int(n) for n in line.split(",")))
    return o


def part1(inp):
    dists = {}
    for j1 in inp:
        for j2 in inp:
            if j1 == j2:
                continue
            dist = math.sqrt(((j1[0] - j2[0]) ** 2) + ((j1[1] - j2[1]) ** 2) + ((j1[2] - j2[2]) ** 2))
            # keep first pair for a distance; collisions unlikely but deterministic
            if dist not in dists:
                dists[dist] = (j1, j2)
    sorted_keys = sorted(dists.keys())
    edges = defaultdict(list)
    take = min(1000, len(sorted_keys))
    for i in range(take):
        pair = dists[sorted_keys[i]]
        j1, j2 = pair
        edges[j1].append(Edge(j2))
        edges[j2].append(Edge(j1))
    g = Graph(inp, edges)
    c = Counter(g.connected_components().values())
    o = 1
    for k, v in c.most_common(3):
        o *= v
    return o


def part2(inp):
    dists = {}
    for j1 in inp:
        for j2 in inp:
            if j1 == j2:
                continue
            dist = math.sqrt(((j1[0] - j2[0]) ** 2) + ((j1[1] - j2[1]) ** 2) + ((j1[2] - j2[2]) ** 2))
            if dist not in dists:
                dists[dist] = (j1, j2)
    sorted_keys = sorted(dists.keys())
    edges = defaultdict(list)
    i = 0
    while i < len(sorted_keys):
        pair = dists[sorted_keys[i]]
        j1, j2 = pair
        edges[j1].append(Edge(j2))
        edges[j2].append(Edge(j1))
        g = Graph(inp, edges)
        v = len(Counter(g.connected_components().values()))
        if v == 1:
            return j1[0] * j2[0]
        i += 1
    return None


def main():
    t0 = timeit.default_timer()
    with open(sys.argv[1], "r") as f:
        i = parse_input(f.readlines())
    print(part1(i))
    t1 = timeit.default_timer()
    with open(sys.argv[1], "r") as f:
        i = parse_input(f.readlines(), True)
    print(part2(i))
    t2 = timeit.default_timer()
    if len(sys.argv) > 2:
        print(f"Part 1: {t1 - t0} seconds")
        print(f"Part 2: {t2 - t1} seconds")


if __name__ == '__main__':
    if len(sys.argv) < 2:
        unittest.main()
    else:
        main()