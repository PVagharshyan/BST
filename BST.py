from node import Node

class BST:
    def __init__(self):
        self.__root = None

    def __hash__(self):
        result = 0
        arr = self.inorder()
        for i in arr:
            result += hash(i)
        return result

    def __eq__(self, other):
        return (
            self.inorder() == other.inorder() and
            self.postorder() == other.postorder() and
            self.preorder() == other.preorder()
        )

    def __bool__(self):
        return bool(self.inorder())

    def __len__(self):
        return len(self.inorder())

    def insert(self, value, root = 1):
        new_node = Node(value)

        if root == 1:
            root = self.__root

        if root == None:
            self.__root = new_node
            return
        elif root.value > value:
            if root.left == None:
                root.left = new_node
                return
            else:
                self.insert(value, root.left)
        elif root.value < value:
            if root.right == None:
                root.right = new_node
                return
            else:
                self.insert(value, root.right)

    def search(self, value, root = 1):
        if root == 1:
            root = self.__root

        if root == None:
            return False
        elif root.value == value:
            return True
        elif root.value > value:
            return self.search(value, root.left)
        elif root.value < value:
            return self.search(value, root.right)

    def postorder(self, root = 1):
        if root == 1:
            root = self.__root

        if root == None:
            return list()

        arr_left = self.postorder(root.left)
        arr_right = self.postorder(root.right)
        arr_right.append(root.value)

        return arr_left + arr_right

    def inorder(self, root = 1):
        if root == 1:
            root = self.__root

        if root == None:
            return list()

        arr_left = self.inorder(root.left)
        arr_left.append(root.value)
        arr_right = self.inorder(root.right)

        return arr_left + arr_right

    def preorder(self, root = 1):
        if root == 1:
            root = self.__root

        if root == None:
            return list()

        arr_left = [root.value]
        arr_left = arr_left + self.preorder(root.left)
        arr_right = self.preorder(root.right)

        return arr_left + arr_right


def main():
    print("!BST!")
    b = BST()
    b.insert(10)
    b.insert(11)
    b.insert(45)
    b.insert(6)
    b.insert(22)
    b.insert(22)
    b.insert(18)
    b.insert(12)
    print("hash:", hash(b))
    print("postorder:", b.postorder())
    print("inorder:", b.inorder())
    print("preorder:", b.preorder())
    print(b._BST__root)
    print(b._BST__root.left)
    print(b._BST__root.left.left)
    print(b._BST__root.left.right)
    print(b._BST__root.right)
    print(b._BST__root.right.left)
    print(b._BST__root.right.right)
    b1 = BST()
    b1.insert(10)
    b1.insert(11)
    b1.insert(45)
    b1.insert(6)
    b1.insert(22)
    b1.insert(22)
    b1.insert(18)
    b1.insert(12)
    print("b == b1:", b == b1)
    b3 = BST()
    print("inorder:", b3.inorder())
    print("b")
    print("len:", len(b))
    print("bool", bool(b))
    print("b1")
    print("len:", len(b1))
    print("bool:", bool(b1))
    print("b2")
    print("len:", len(b3))
    print("bool:", bool(b3))

if __name__ == "__main__":
    main()
