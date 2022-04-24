class Linked_Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
    
    def add_next(self, next):
        self.next = next

    @classmethod
    def print_linked(cls, head):
        initial = head
        def rec_print(head):
            print(head.value)
            if head.next and head.next != initial:
                rec_print(head.next)
        rec_print(head)

# last_node = Linked_Node(3)
# head = Linked_Node(1, Linked_Node(2, last_node))



# node_1 = Linked_Node(1)
# node_2 = Linked_Node(2)
# node_1.add_next(node_2)
# print(node_1.next.value, node_1)
# other_node = Linked_Node(4, head)
# last_node.add_next(other_node)


# Linked_Node.print_linked(head)

class Double_Linked_Node(Linked_Node):
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev
    
    def add_prev(self, prev):
        self.prev = prev

# head = Double_Linked_Node(1)
# node_1 = Double_Linked_Node(2)
# node_2 = Double_Linked_Node(3)

# head.add_next(node_1)
# node_1.add_next(node_2)
# node_1.add_prev(head)
# node_2.add_prev(node_1)

# Double_Linked_Node.print_linked(head)

class Tree_Node:

    def __init__(self, value, links = []):
        self.value, self.links = value, links

    def add(self, node):
        self.links.append(node)

    @classmethod
    def print_depth(cls, node):
        print(node.value)
        for child in node.links:
            cls.print_depth(child)

nodes = [Tree_Node(i) for i in range(9)]


for link in [nodes[1], nodes[2]]:
    nodes[0].add(link)

for link in [nodes[3], nodes[4]]:
    nodes[1].add(link)

for link in [nodes[5], nodes[6]]:
    nodes[2].add(link)

for link in [nodes[7], nodes[8]]:
    nodes[3].add(link)

Tree_Node.print_depth(nodes[0])