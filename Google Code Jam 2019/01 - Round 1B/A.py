# April, 28, 2019
# Round 1B
# "Manhattan Crepe Cart"


class Person:
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction


def possible(x, y, p):
    return (p.direction == 'E' and x > p.x or
            p.direction == 'W' and x < p.x or
            p.direction == 'N' and y > p.y or
            p.direction == 'S' and y < p.y)

def manhattan_crepe_cart(people, size):
    xs = set([0])
    ys = set([0])
    for p in people:
        xs.add(p.x)
        xs.add(p.x + 1)
        ys.add(p.y)
        ys.add(p.y + 1)

    x_max = 0
    y_max = 0
    v_max = 0

    count = 0
    print (len(xs))
    print(len(ys))
    for x in xs:
        if count % 10 == 0: print(count)
        count += 1
        for y in ys:
            # print(count, end=' ')
            # count += 1
            v = sum(1 for p in people if possible(x, y, p))
            if v > v_max:
                x_max = x
                y_max = y
                v_max = v
    return x_max, y_max



    xs = []
    ys = []
    for p in people:
        L, R, T, B = rectangle(p, size)
        xs.append((L, R))
        ys.append((T, B))
    xs.sort(key=lambda a: a[0])
    ys.sort(key=lambda a: a[0])
    x_max = 0
    y_max = 0



    grid = Grid(people)
    for p in people:
        print()
        grid.set_dir(p.x, p.y, p.direction)
    grid.print()

    return grid.max_coord()

       
N = int(input())

for case in range(1, N + 1):
    P, Q = map(int, input().split())
    people = []
    for _ in range(P):
        line = input().split()
        people.append(Person(x = int(line[0]), y = int(line[1]), direction = line[2]))
    x, y = manhattan_crepe_cart(people, Q + 1)
    print("Case #%d: %s %s" % (case, x, y))
