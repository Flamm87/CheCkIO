def get_layer(net, crush):
    temp = []
    for x in net.copy():
        if crush in x:
            temp.append("".join(x).replace(crush, ""))
    return temp


def make_path(net, crush, path, old_path=0):
    if path != 0 and old_path == path:  # Проверка на кольцо
        return path
    if len(path) == 0:  # Добавляем вершину
        path.append(crush)
    for node in path.copy():
        layer = get_layer(net, node[-1])  # Для каждой нижней точки вибираем список следующих звеньев
        old_path = path.copy()  # сохраняем старый список путей
        for x in layer:  # Формируем новый
            if x == path[0][0]:
                continue
            if len(node) > 1:
                if node[-2] == x:
                    continue
            if node in path:
                path.remove(node)
            path.append(node + x)
    return make_path(net.copy(), None, path, old_path)


def count_pigeons(users, source, paths, crushes):
    points = set(crushes)
    for path in paths:
        if source not in path:
            points |= set(path)
    count = 0
    for x in list(points):
        count += users[x]
    return count


def disconnected_users(net, users, source, crushes):
    paths = []
    if source in crushes:
        return sum(users.values())
    for crush in crushes:
        paths.extend(make_path(net.copy(), crush, [], 0))
    return count_pigeons(users, source, paths, crushes)


if __name__ == '__main__':
    disconnected_users([["A", "B"], ["A", "C"], ["A", "D"], ["A", "E"], ["A", "F"]],
                       {"A": 10, "C": 10, "B": 10, "E": 10, "D": 10, "F": 10}, "A", ["B", "C"])
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert disconnected_users([
        ['A', 'B'],
        ['B', 'C'],
        ['C', 'D']
    ], {
        'A': 10,
        'B': 20,
        'C': 30,
        'D': 40
    },
        'A', ['A']) == 100, "First"

    assert disconnected_users([
        ['A', 'B'],
        ['B', 'D'],
        ['A', 'C'],
        ['C', 'D']
    ], {
        'A': 10,
        'B': 0,
        'C': 0,
        'D': 40
    },
        'A', ['B']) == 0, "Second"

    assert disconnected_users([
        ['A', 'B'],
        ['A', 'C'],
        ['A', 'D'],
        ['A', 'E'],
        ['A', 'F']
    ], {
        'A': 10,
        'B': 10,
        'C': 10,
        'D': 10,
        'E': 10,
        'F': 10
    },
        'C', ['A']) == 50, "Third"

    print('Done. Try to check now. There are a lot of other tests')
