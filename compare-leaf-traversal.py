# difficulty: 4/4

# input: {
#   "tree1": {
#     "nodes": [
#       {"id": "1", "left": "2", "right": "3", "value": 1},
#       {"id": "2", "left": "4", "right": "5", "value": 2},
#       {"id": "3", "left": null, "right": "6", "value": 3},
#       {"id": "4", "left": null, "right": null, "value": 4},
#       {"id": "5", "left": "7", "right": "8", "value": 5},
#       {"id": "6", "left": null, "right": null, "value": 6},
#       {"id": "7", "left": null, "right": null, "value": 7},
#       {"id": "8", "left": null, "right": null, "value": 8}
#     ],
#     "root": "1"
#   },
#   "tree2": {
#     "nodes": [
#       {"id": "1", "left": "2", "right": "3", "value": 1},
#       {"id": "2", "left": "4", "right": "7", "value": 2},
#       {"id": "3", "left": null, "right": "5", "value": 3},
#       {"id": "4", "left": null, "right": null, "value": 4},
#       {"id": "5", "left": "8", "right": "6", "value": 5},
#       {"id": "6", "left": null, "right": null, "value": 6},
#       {"id": "7", "left": null, "right": null, "value": 7},
#       {"id": "8", "left": null, "right": null, "value": 8}
#     ],
#     "root": "1"
#   }
# }

# output: true
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class Stack:
    # create data structure stack for easier approach
    def __init__(self):
        self.arr = []

    def push(self, node: BinaryTree):
        self.arr.append(node)

    def pop(self):
        self.arr.pop()

    def isEmpty(self):
        return self.arr == []

    def getTop(self):
        return self.arr[-1]

    def setEmpty(self):
        self.arr = []


def areEqual(x: int, y: int):
    return x == y


def compareLeafTraversal(tree1, tree2):
    stack = Stack()

    # all leaves values from tree1
    result = []

    stack.push(tree1)

    # while stack is not empty
    while stack.arr:
        head1 = stack.getTop()
        stack.pop()

        # iterrate through tree1

        # check if node is leaf
        if head1.left == None and head1.right == None:
            result.append(head1.value)

        else:
            # it is not a leaf

            # add on stack right child
            if head1.right:
                stack.push(head1.right)

            # add on stack left child
            if head1.left:
                stack.push(head1.left)

    # result = [4, 7, 8, 6]

    # stack has to be empty, because first while loop ended (there was condition:
    # while stakc is not empty)
    stack.push(tree2)

    # pointer points in result (list), we compare value on index 'ptr' from tree1 and
    # value from tree2
    ptr = 0

    # number of leaves from tree1
    numberOfLeaves = len(result)

    # while stack is not empty
    while stack.arr:
        head2 = stack.getTop()
        stack.pop()

        # iterrate through tree2
        # check if node is leaf
        if head2.left == None and head2.right == None:
            if not areEqual(head2.value, result[ptr]):
                # if leaf from tree1 is not on the same traversal position as leaf from tree2
                return False

            if ptr < numberOfLeaves:
                # in second tree can't be more leaves than in first tree
                ptr += 1
            else:
                # in second tree are more leaves than in first tree
                return False

        else:
            # it is not a leaf

            # add on stack right child
            if head2.right:
                stack.push(head2.right)

            # add on stack left child
            if head2.left:
                stack.push(head2.left)

    return True


