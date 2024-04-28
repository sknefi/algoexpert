# difficulty: 4/4

# input: linkedList: {
#     head: "0",
#     nodes: [
#       {"id": "0", "next": "1", "value": 0},
#       {"id": "1", "next": "2", "value": 1},
#       {"id": "2", "next": "3", "value": 2},
#       {"id": "3", "next": "4", "value": 3},
#       {"id": "4", "next": "5", "value": 4},
#       {"id": "5", "next": null, "value": 5}
#     ]
#   }

# output: {
#    head: "1",
#    nodes: [
#     {"id": "1", "next": "0", "value": 1},
#     {"id": "0", "next": "3", "value": 0},
#     {"id": "3", "next": "2", "value": 3},
#     {"id": "2", "next": "5", "value": 2},
#     {"id": "5", "next": "4", "value": 5},
#     {"id": "4", "next": null, "value": 4}
#   ]
# }

class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def nodeSwap(head):
    # lets hope head will be not NULL
    node1 = head
    node2 = head.next  # <obj> | NULL

    if node2:
        # there are atleast two nodes, so we will set node2 as a new head
        newHead = node2
    else:
        # there is only one node, make no change
        newHead = head

    # for better visualization try to draw nodes and connection between them
    while node1 and node2:
        # set node3 to track our position in LinkedList
        node3 = node2.next
        node2.next = node1

        if node3:
            node1.next = node3.next
        else:
            node1.next = node3
            break

        if node1.next:
            node2 = node1.next
            node1 = node3
        else:
            node1.next = node3
            break

    return newHead

