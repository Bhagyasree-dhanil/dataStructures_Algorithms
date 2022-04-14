"""
Binary search Tree

General tree with some constraints

1. child nodes are limited to a maximum of 2.
2. it should have some order - left subtree < parent node < right subtree
3. elements are always unique

Two types of approaches

1. Breadth first search
2. Depth first search

   *  Inorder traversal  - left tree , root node, Right node
   *  Preorder traversal - root node, left tree,  Right node
   *  Postorder traversal - left tree, Right node, root node

NODE Deletion

1. delete with no child - just delete no need to swap data
2. delete with one child - add child node  to the place of deleted node
3. delete with two child - tricky one . we need to follow the properties of BT
   *  Find minimum value from right subtree and copy that
   *  Find maximum from left subtree


"""


class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self ,data):
        if data == self.data:
            return
        n1 = self.data
        n2 = self.left
        n3 = self.right
        if data < self.data:
            # add in left subtree
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            # add in right subtree
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)

    def in_order_traversal(self):
        elements = []

        # visit left
        if self.left:
            elements += self.left.in_order_traversal()

        # visit base node
        elements.append(self.data)

        # visit right
        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    def pre_order_traversal(self):

        # visit base node
        elements = [self.data]

        # visit left
        if self.left:
            elements += self.left.in_order_traversal()

        # visit right
        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    def post_order_traversal(self):

        elements = []

        # visit left
        if self.left:
            elements += self.left.in_order_traversal()

        # visit right
        if self.right:
            elements += self.right.in_order_traversal()

        # visit base node
            elements.append(self.data)

        return elements

    def search(self, val):
        if self.data == val:
            return True

        if val < self.data:
            if self.left:
                self.left.search(val)
            else:
                return False
        if val > self.data:
            if self.right:
                self.right.search(val)
            else:
                return False

    def find_min(self):
        # find the left most leaf node

        if self.left is None:
            return self.data
        return self.left.find_min()

    def find_max(self):
        # find the left most leaf node

        if self.right is None:
            return self.data

        return self.right.find_max()

    def find_sum(self):
        # find the left most leaf node

        left_sum = self.left.find_sum() if self.left else 0
        right_sum = self.right.find_sum() if self.right else 0
        total_sum = self.data + left_sum + right_sum
        return total_sum

    def delete(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        else:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.right

            min_val = self.right.find_min()
            self.data = min_val
            self.right = self.right.delete(min_val)

            '''
            max_val = self.right.find_max()
            self.data = max_val
            self.left = self.left.delete(max_val)
            
            '''

        return self


def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])

    for i in range(1, len(elements)):
        root.add_child(elements[i])

    return root


if __name__ ==  "__main__":
    numbers=[17, 4, 1, 20, 9, 23, 18, 34]
    numbers_tree = build_tree(numbers)
    print(numbers_tree.in_order_traversal())
    print(numbers_tree.pre_order_traversal())
    print(numbers_tree.post_order_traversal())
    print(numbers_tree.search(20))
    print(numbers_tree.find_max())
    print(numbers_tree.find_min())
    print(numbers_tree.find_sum())
    numbers_tree.delete(9)
    print("after deleting", numbers_tree.in_order_traversal())

"""
# ==========================================Exercise================================================================#

1. find min
2. find max
3. calculate sum
4. preorder traversal
5. postorder traversal

"""