def make_path(links, source, end, lens):
    paths = source.copy()
    for path in paths.copy():
        p = []
        for i in links[int(path[-1])]:
            if i not in path.copy() and i != end:
                temp = path.copy()
                temp.append(i)
                if len(temp) == lens - 1:
                    if i in links[end]:
                        p.append(temp)
                        continue
                    else:
                        continue
                if len(temp) < lens:
                    p.append(temp)
        if len(p) == 0:
            if len(path) != lens - 1:
                del paths[0]
            continue
        del paths[0]
        paths.extend(p)
    if paths == source:
        return paths
    return make_path(links, paths, end, lens)


def get_position(x, y):
    temp = list()
    for z in range(1, y + 1):
        temp.append(list(range(z * x - x, z * x)))
    return temp


def get_neighbour(positions):
    node_links = dict()
    for i in range(len(positions)):
        for x in range(len(positions[0])):
            node_links[positions[i][x]] = list()
            if i - 1 >= 0:
                node_links[positions[i][x]].append(positions[i - 1][x])
                if x - 1 >= 0:
                    node_links[positions[i][x]].append(positions[i - 1][x - 1])
                if x + 1 <= len(positions[0]) - 1:
                    node_links[positions[i][x]].append(positions[i - 1][x + 1])
            if x - 1 >= 0:
                node_links[positions[i][x]].append(positions[i][x - 1])
            if x + 1 <= len(positions[0]) - 1:
                node_links[positions[i][x]].append(positions[i][x + 1])
            if i + 1 <= len(positions) - 1:
                node_links[positions[i][x]].append(positions[i + 1][x])
                if x - 1 >= 0:
                    node_links[positions[i][x]].append(positions[i + 1][x - 1])
                if x + 1 <= len(positions[0]) - 1:
                    node_links[positions[i][x]].append(positions[i + 1][x + 1])
    return node_links


def convert_to_costs(grid, paths):
    temp = list()
    for z in paths:
        p = list()
        for x in z:
            p.append(grid[int(x // len(grid[0]))][int(x % len(grid[0]))])
        temp.append(p)
    return temp


def g_key(grid, path):
    if path == len(grid) * len(grid[0]):
        return sum(list(map(lambda i: sum(i), grid)))
    if len(grid) == len(grid[0]) and path == len(grid):
        return sum([grid[x][x] for x in range(len(grid))])
    position_matrix = get_position(len(grid[0]), len(grid))
    links = get_neighbour(position_matrix)
    paths = []
    for x in links[position_matrix[0][0]]:
        paths += make_path(links, [[position_matrix[0][0], x]], position_matrix[-1][-1], path)
    paths = list(filter(lambda i: i[-1] in links[position_matrix[-1][-1]] and len(i) == path - 1, paths))
    paths = convert_to_costs(grid, paths)
    paths_sums = list(map(lambda i: sum(i) + grid[-1][-1], paths))
    return max(paths_sums)


if __name__ == '__main__':
    print("Example:")
    # print(g_key([[2, 5, 4, 1],
    #           [0, 4, 9, 5],
    #           [7, 2, 5, 1],
    #           [1, 3, 2, 2]],14))
    print(g_key([[1, 6, 7, 2, 4],
                 [0, 4, 9, 5, 3],
                 [7, 2, 5, 1, 4],
                 [3, 3, 2, 2, 9],
                 [2, 6, 1, 4, 0]], 9))
    print(g_key([[1, 6],
                 [5, 1]], 2))
    # These "asserts" using only for self-checking and not necessary for auto-testing
    # assert g_key([[1, 6, 7, 2, 4],
    #               [0, 4, 9, 5, 3],
    #               [7, 2, 5, 1, 4],
    #               [3, 3, 2, 2, 9],
    #               [2, 6, 1, 4, 0]], 9) == 46

    # assert g_key([[2, 5, 4, 1, 8],
    #               [0, 4, 9, 5, 3],
    #               [7, 2, 5, 1, 4],
    #               [3, 3, 2, 2, 9],
    #               [2, 6, 1, 4, 1]], 6) == 27

    assert g_key([[1, 2, 3, 4, 5],
                  [2, 3, 4, 5, 1],
                  [3, 4, 5, 1, 2],
                  [4, 5, 1, 2, 3],
                  [5, 1, 2, 3, 4]], 24) == 75

    assert g_key([[1, 6],
                  [5, 1]], 2) == 2
    #
    # print("Coding complete? Click 'Check' to earn cool rewards!")

