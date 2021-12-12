from collections import defaultdict

def def_value():
    return False

def part1():
    import sys
    print(sys.setrecursionlimit(2000))
    with open("input.txt") as input:
        vertices = {}
        for path in input:
            in_path = path.rstrip().split("-")
            if in_path[0] not in vertices:
                vertices[in_path[0]] = []

            if in_path[1] not in vertices:
                vertices[in_path[1]] = []

            vertices[in_path[0]].append(in_path[1])
            vertices[in_path[1]].append(in_path[0])

        visited = {}
        for i in vertices.keys():
            visited[i] = False

        paths = []
        twice_cave = False #True for recursive pt2, which doesnt work
        recursive_dfs("start", "end", visited, vertices, paths, twice_cave)
        return counter


counter = 0


def recursive_dfs(node,end ,visited, vertices, paths, twice_cave):
    visited[node] = True
    paths.append(node)

    if node == end:
        global counter
        counter = counter + 1
    else:
        for neighbour in vertices[node]:
            can_enter_twice = visited[neighbour] and neighbour.islower() and twice_cave and (neighbour != "start" and neighbour != "end")

            if not visited[neighbour] or (visited[neighbour] and neighbour.isupper()) or (can_enter_twice):
                if can_enter_twice:
                    twice_cave = False
                recursive_dfs(neighbour, end, visited, vertices, paths, twice_cave)

    paths.pop()
    visited[node] = False


def part2():
    with open("input.txt") as input:
        vertices = {}
        for path in input:
            in_path = path.rstrip().split("-")
            if in_path[0] not in vertices:
                vertices[in_path[0]] = []

            if in_path[1] not in vertices:
                vertices[in_path[1]] = []

            vertices[in_path[0]].append(in_path[1])
            vertices[in_path[1]].append(in_path[0])

        all_paths = 0
        stack = [(["start"], True)]
        while stack:
            path, twice_cave = stack.pop(0)
            for neigbour in vertices[path[-1]]:
                if neigbour == "end":
                    all_paths += 1
                elif neigbour not in path or neigbour.isupper():
                    stack.append((path + [neigbour], twice_cave))
                elif twice_cave and neigbour != "start":
                    stack.append((path + [neigbour], False))
        return all_paths


print("Part 1:", part1())
print("Part 2:", part2())