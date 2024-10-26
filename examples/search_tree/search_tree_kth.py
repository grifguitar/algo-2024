from random import randint


class Vertex:
    def __init__(self, key=None, priority=None, left=None, right=None):
        self.key: int = key
        self.priority: int = priority
        self.left: Vertex = left
        self.right: Vertex = right
        self.sz: int = 1  # update

    def __str__(self):
        lines = {}
        Vertex.print_tree(v=self, skip=0, d=0, lines=lines)
        ans = []
        for i in range(len(lines)):
            if i in lines:
                ans.append(lines[i])
        return '\n'.join(ans)

    @staticmethod
    def print_tree(v, skip, d, lines) -> int:
        if d not in lines:
            lines[d] = ''
        if v is None:
            cur = '(,)'
            lines[d] += ' ' * (skip - len(lines[d]))
            lines[d] += cur
            return len(cur)
        cur = '(' + str(v.key) + ',' + str(v.priority) + ')'
        l = Vertex.print_tree(v=v.left, skip=skip, d=(d + 1), lines=lines)
        lines[d] += ' ' * (skip + l - len(lines[d]))
        lines[d] += cur
        r = Vertex.print_tree(v=v.right, skip=(skip + l + len(cur)), d=(d + 1), lines=lines)
        return l + r + len(cur)

    # update
    @staticmethod
    def size_of(v):
        return v.sz if v is not None else 0

    # update
    @staticmethod
    def recalc(v):
        if v is not None:
            v.sz = Vertex.size_of(v.left) + Vertex.size_of(v.right) + 1
        return v


def merge(root1: Vertex, root2: Vertex) -> Vertex:
    if root1 is None:
        return root2
    if root2 is None:
        return root1
    if root1.priority < root2.priority:
        root1.right = merge(root1.right, root2)
        return Vertex.recalc(root1)  # update
    else:
        root2.left = merge(root1, root2.left)
        return Vertex.recalc(root2)  # update


def split(root: Vertex, key0: int) -> (Vertex, Vertex):
    if root is None:
        return None, None
    if root.key < key0:
        (a, b) = split(root.right, key0)
        root.right = a
        return Vertex.recalc(root), b  # update
    else:
        (a, b) = split(root.left, key0)
        root.left = b
        return a, Vertex.recalc(root)  # update


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


# update
def kth(root: Vertex, k: int) -> int:
    l = Vertex.size_of(root.left)
    if k == l:
        return root.key
    elif k < l:
        return kth(root.left, k)
    else:
        return kth(root.right, k - l - 1)


def main():
    tree: Vertex = None
    tree = insert(tree, 10)
    tree = insert(tree, 2)
    tree = insert(tree, 55)
    tree = insert(tree, 3)
    print(tree)

    # update
    print('kth:')
    print(kth(tree, 0))
    print(kth(tree, 1))
    print(kth(tree, 2))
    print(kth(tree, 3))


if __name__ == '__main__':
    main()
