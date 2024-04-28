# difficulty: 2/4

# matrix: [
#     [1, 0, 0, 1, 0],
#     [1, 0, 1, 0, 0],
#     [0, 0, 1, 0, 1],
#     [1, 0, 1, 0, 1],
#     [1, 0, 1, 1, 0] ]

# output: [2, 1, 5, 2, 2]

class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next_node = None


class Linked_list:
    def __init__(self) -> None:
        self.head: Node = None

    def is_empty(self):
        if self.head == None: return True

        return False

    def add_on_end(self, x: int):
        if not self.is_empty():
            current_node = self.head

            while current_node.next_node:
                current_node = current_node.next_node

            current_node.next_node = Node(x)

        else:
            self.head = Node(x)

    def pop_from_start(self):
        # indexing: 1. 2. 3. 4. ... nth
        if not self.is_empty():
            self.head = self.head.next_node
        else:
            # print('cant pop, linkedlist is empty')
            pass

    def print_linked_list(self):
        itr = 0

        if not self.is_empty():
            current_node = self.head
            while current_node:
                print(f'{current_node.data} -> ', end='')
                current_node = current_node.next_node
                itr += 1
        print('NULL', end='')
        print()
        # print(itr)

    def remove_duplicity(self):
        previous_node = None
        current_node = self.head
        coordinates_dict = {}

        while current_node:
            if current_node.data not in coordinates_dict:
                coordinates_dict[current_node.data] = True
                previous_node = current_node
                current_node = current_node.next_node

            else:
                previous_node.next_node = current_node.next_node
                current_node = previous_node.next_node


linked_l = Linked_list()


def check_for_other_rivers(indX: int, indY: int, ch_river: int, array_2d: list):
    global linked_l
    if array_2d[indX][indY] != ch_river:
        return []
    else:
        # only river, nofriends :[
        # print('only river')
        pass

    rows = len(array_2d)
    columns = len(array_2d[0])
    # code becease of this two lines above, works only with square or rectangle matrices

    new_q = []
    for x in range(-1, 2, 2):
        # x = -1 | 1
        if 0 <= (indX + x) and (indX + x) < rows and array_2d[indX + x][indY] == ch_river:
            # new_q.append((indX + x, indY))
            linked_l.add_on_end((indX + x, indY))

    for y in range(-1, 2, 2):
        # y = -1 | 1
        if 0 <= (indY + y) and (indY + y) < columns and array_2d[indX][indY + y] == ch_river:
            # new_q.append((indX, indY + y))
            linked_l.add_on_end((indX, indY + y))

    # new_q = [(4, 3), (5, 4)]
    # linked_list: (4, 3)->(5, 4)

    # return new_q


def is_river(x: int, y: int, matrix: list) -> bool:
    if matrix[x][y] == 1: return True

    return False


def riverSizes(matrix):
    global linked_l
    # q=[ (2, 2)]

    rivers = []

    for rowI in range(len(matrix)):
        for columnI in range(len(matrix[0])):
            if is_river(rowI, columnI, matrix):
                river_lenght = 0
                check_for_other_rivers(rowI, columnI, 1, matrix)
                matrix[rowI][columnI] = 0  # already explored, we can set this river as land so program wont confused
                river_lenght += 1
                # linked_l.print_linked_list()
                # print(linked_l.head.data)

                while linked_l.head:
                    # print(river_lenght)
                    check_for_other_rivers(linked_l.head.data[0], linked_l.head.data[1], 1, matrix)
                    linked_l.remove_duplicity()

                    matrix[linked_l.head.data[0]][linked_l.head.data[1]] = 0
                    linked_l.pop_from_start()
                    river_lenght += 1

                rivers.append(river_lenght)

    return rivers

