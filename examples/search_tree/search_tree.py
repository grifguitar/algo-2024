from random import randint


class Vertex:
    def __init__(self, key=None, priority=None, left=None, right=None):
        self.key: int = key
        self.priority: int = priority
        self.left: Vertex = left
        self.right: Vertex = right

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
    cur: str = '(' + str(v.key) + ',' + str(v.priority) + ')'
    l: int = print_tree(v=v.left, skip=skip, d=(d + 1), lines=lines)
    lines[d] += ' ' * (skip + l - len(lines[d])) + cur
    r: int = print_tree(v=v.right, skip=(skip + l + len(cur)), d=(d + 1), lines=lines)
    return l + r + len(cur)


def merge(root1: Vertex, root2: Vertex) -> Vertex:
    if root1 is None:
        return root2
    if root2 is None:
        return root1
    if root1.priority < root2.priority:
        root1.right = merge(root1.right, root2)
        return root1
    else:
        root2.left = merge(root1, root2.left)
        return root2


def split(root: Vertex, key0: int) -> (Vertex, Vertex):
    if root is None:
        return None, None
    if root.key < key0:
        (root.right, other) = split(root.right, key0)
        return root, other
    else:
        (other, root.left) = split(root.left, key0)
        return other, root


def insert(root: Vertex, key0: int) -> Vertex:
    (a, b) = split(root, key0)
    (c, d) = split(b, key0 + 1)
    c = Vertex(key0, randint(1000, 9999))
    return merge(a, merge(c, d))


def remove(root: Vertex, key0: int) -> Vertex:
    (a, b) = split(root, key0)
    (c, d) = split(b, key0 + 1)
    return merge(a, d)


def find(root: Vertex, key0: int) -> (bool, Vertex):
    (a, b) = split(root, key0)
    (c, d) = split(b, key0 + 1)
    flag: bool = (c is not None)
    return flag, merge(a, merge(c, d))


def main():
    tree: Vertex = None
    tree = insert(tree, 10)
    tree = insert(tree, 2)
    tree = insert(tree, 55)
    tree = insert(tree, 3)
    print(tree)


if __name__ == '__main__':
    main()
