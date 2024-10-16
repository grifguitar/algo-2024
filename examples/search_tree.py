from random import randint


class Vertex:
    def __init__(self, key=None, priority=None, left=None, right=None):
        self.key: int = key
        self.priority: int = priority
        self.left: Vertex = left
        self.right: Vertex = right

    def __str__(self, tab=0):
        return ((self.right.__str__(tab=(tab + 1)) if self.right is not None else ' ' * 4 * (tab + 1) + '(,)') + '\n' +
                ' ' * 4 * tab + '(' + str(self.key) + ',' + str(self.priority) + ')' + '\n' +
                (self.left.__str__(tab=(tab + 1)) if self.left is not None else ' ' * 4 * (tab + 1) + '(,)'))


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
        (a, b) = split(root.right, key0)
        root.right = a
        return root, b
    else:
        (a, b) = split(root.left, key0)
        root.left = b
        return a, root


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
