from random import randint


class Vertex:
    def __init__(self, priority=None, left=None, right=None, sz=1, flag=0, data=0):
        # self.key: int = key
        self.priority: int = priority
        self.left: Vertex = left
        self.right: Vertex = right
        self.sz: int = sz
        self.flag: int = flag
        self.sum: int = data
        self.data: int = data

    def __str__(self):
        lines: dict = {}
        ans: list = []
        print_tree(v=self, skip=0, d=0, lines=lines)
        for i in range(len(lines)):
            if i in lines:
                ans.append(lines[i])
        return '\n'.join(ans)


def print_tree(v: Vertex, skip: int, d: int, lines: dict) -> int:
    if d not in lines:
        lines[d] = ''
    if v is None:
        cur: str = '(,)'
        lines[d] += ' ' * (skip - len(lines[d])) + cur
        return len(cur)
    cur: str = '(' + str(v.data) + ',' + str(v.flag) + ',' + str(v.sum) + ')'
    l: int = print_tree(v=v.left, skip=skip, d=(d + 1), lines=lines)
    lines[d] += ' ' * (skip + l - len(lines[d])) + cur
    r: int = print_tree(v=v.right, skip=(skip + l + len(cur)), d=(d + 1), lines=lines)
    return l + r + len(cur)


def update(v: Vertex, flag: int):
    if v is not None:
        v.flag += flag


def push(v: Vertex):
    if v is not None and v.flag != 0:
        v.data += v.flag
        v.sum += v.flag * v.sz
        update(v.left, v.flag)
        update(v.right, v.flag)
        v.flag = 0


def size_of(v: Vertex) -> int:
    push(v)
    return v.sz if v is not None else 0


def sum_of(v: Vertex) -> int:
    push(v)
    return v.sum if v is not None else 0


def data_of(v: Vertex) -> int:
    push(v)
    return v.data if v is not None else 0


def recalc(v: Vertex) -> Vertex:
    push(v)
    if v is not None:
        v.sz = size_of(v.left) + size_of(v.right) + 1
        v.sum = sum_of(v.left) + sum_of(v.right) + data_of(v)
    return v


def merge(root1: Vertex, root2: Vertex) -> Vertex:
    push(root1)
    push(root2)
    if root1 is None:
        return root2
    if root2 is None:
        return root1
    if root1.priority < root2.priority:
        root1.right = merge(root1.right, root2)
        return recalc(root1)
    else:
        root2.left = merge(root1, root2.left)
        return recalc(root2)


def split(root: Vertex, key0: int, skip_left: int) -> (Vertex, Vertex):
    push(root)
    if root is None:
        return None, None
    if (skip_left + size_of(root.left)) < key0:
        (root.right, other) = split(root.right, key0, skip_left + size_of(root.left) + 1)
        return recalc(root), other
    else:
        (other, root.left) = split(root.left, key0, skip_left)
        return other, recalc(root)


def insert(root: Vertex, key0: int, data: int, shifting: bool = True) -> Vertex:
    (a, b) = split(root, key0, 0)
    if not shifting:
        (c, b) = split(b, 1, 0)
    c = Vertex(priority=randint(1000, 9999), data=data)
    return merge(a, merge(c, b))


def remove(root: Vertex, key0: int) -> Vertex:
    (a, b) = split(root, key0, 0)
    (c, b) = split(b, 1, 0)
    return merge(a, b)


def get(root: Vertex, key0: int) -> (int, Vertex):
    (a, b) = split(root, key0, 0)
    (c, d) = split(b, 1, 0)
    return data_of(c), merge(a, merge(c, d))


def add(root: Vertex, left: int, right: int, value: int) -> Vertex:
    (a, b) = split(root, left, 0)
    (c, d) = split(b, right - left, 0)
    update(v=c, flag=value)
    return merge(a, merge(c, d))


def main():
    tree: Vertex = None
    tree = insert(tree, 0, 1)
    tree = insert(tree, 0, 2)
    tree = insert(tree, 0, 3)
    tree = insert(tree, 0, 4)
    tree = insert(tree, 0, 5)
    print(tree)
    print()
    add(tree, left=0, right=5, value=10)
    print(tree)


if __name__ == '__main__':
    main()
