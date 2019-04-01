def make_paths(links, crush, crushes):
    path = list(crush)
    for c in crush:
        p = [c + x for x in links[c[-1]] if (x not in c) and (x not in crushes)]
        if len(p) == 0:
            continue
        path.remove(c)
        path.extend(p)
    if path == crush:
        return path
    return make_paths(links, path, crushes)


def make_subet(paths):
    subnets = []
    while len(paths) > 0:
        temp = set()
        for i in paths.copy():
            if len(set(i[1:]) & temp) or len(temp) == 0:
                temp |= set(i[1:])
                paths.remove(i)
        if len(temp)>0: subnets.append(temp)
    return subnets

def subnetworks(net, crushes):
    links = dict()
    paths = []
    for x in net:
        links.setdefault(x[0], list()).append(x[1])
        links.setdefault(x[1], list()).append(x[0])
    for x in crushes:
        paths.extend(make_paths(links, x, crushes))
    return len(make_subet(paths))


if __name__ == '__main__':
    subnetworks([
        ['A', 'B'],
        ['B', 'C'],
        ['C', 'D']
    ], ['C', 'D'])
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert subnetworks([
            ['A', 'B'],
            ['B', 'C'],
            ['C', 'D']
        ], ['B']) == 2, "First"
    assert subnetworks([
            ['A', 'B'],
            ['A', 'C'],
            ['A', 'D'],
            ['D', 'F']
        ], ['A']) == 3, "Second"
    assert subnetworks([
            ['A', 'B'],
            ['B', 'C'],
            ['C', 'D']
        ], ['C', 'D']) == 1, "Third"
    print('Done! Check button is waiting for you!')
