# difficulty: 3/4

# input:   linkedList: {
#     head: "0",
#     nodes: [
#       {"id": "0", "next": "1", "value": 0},
#       {"id": "1", "next": "2", "value": 1},
#       {"id": "2", "next": "3", "value": 2},
#       {"id": "3", "next": "4", "value": 3},
#       {"id": "4", "next": "5", "value": 4},
#       {"id": "5", "next": null, "value": 5}
#     ]
#   },
#   k: 2

# output: {
#   "head": "4",
#   "nodes": [
#     {"id": "4", "next": "5", "value": 4},
#     {"id": "5", "next": "0", "value": 5},
#     {"id": "0", "next": "1", "value": 0},
#     {"id": "1", "next": "2", "value": 1},
#     {"id": "2", "next": "3", "value": 2},
#     {"id": "3", "next": null, "value": 3}
#   ]
# }

# This is the class of the input linked list.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def shiftLinkedList(head, k):
    currentNode = head
    numberOfNodes = 0

    while currentNode:
        if currentNode.next == None:
            tail = currentNode

        numberOfNodes += 1
        currentNode = currentNode.next

    offset = k % numberOfNodes
    if offset == 0:
        return head

    tail.next = head

    newTail = head
    for _ in range(numberOfNodes - offset - 1):
        newTail = newTail.next

    newHead = newTail.next
    newTail.next = None

    return newHead
