def get_layer(net, crush):
    """ Ету функцию можно заменить на
    source_paths = lambda n, c: ["".join(x).replace(c, "") for x in n if c in x] в disconnected_users"""
    return ["".join(x).replace(crush, "") for x in net if crush in x]


def make_path(links, source, crushes):
    paths = list(source)
    for path in paths.copy():
        p = [path + i for i in links[path[-1]] if (i not in path) and (i not in crushes)]
        if len(p) == 0:
            continue
        paths.remove(path)
        paths.extend(p)
    if paths == source:
        return paths
    return make_path(links, paths, crushes)


def disconnected_users(net, users, source, crushes):
    if source in crushes:
        return sum(users.values())
    link_nodes = {x: get_layer(net, x) for x in users.keys()}
    source_paths = make_path(link_nodes, source, crushes)
    print(source_paths)
    set_con_point = set()
    for x in source_paths:
        set_con_point |= set(x)
    broken_points = set(users.keys()) - set_con_point
    count = 0
    for x in list(broken_points):
        count += users[x]
    return count


if __name__ == '__main__':
    disconnected_users([
        ['A', 'B'],
        ['B', 'C'],
        ['C', 'D']
    ], {
        'A': 10,
        'B': 20,
        'C': 30,
        'D': 40
    },
        'A', ['C'])

    disconnected_users([["A", "B"], ["B", "C"], ["C", "D"], ["C", "G"], ["G", "K"], ["K", "C"], ["A", "D"]],
                       {"A": 10, "C": 10, "B": 10, "G": 10, "D": 10, "K": 10}, "D", ["B", "G"])
    # These "asserts" using only for self-checking and not necessary for auto-testing
    disconnected_users([["A", "B"], ["B", "C"], ["G", "D"], ["C", "G"], ["G", "K"], ["K", "C"]],
                       {"A": 10, "C": 10, "B": 10, "G": 10, "D": 10, "K": 10}, "D", ["B", "G"])
