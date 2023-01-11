import queue
from typing import Any
import matplotlib.pyplot as plt
import networkx as nx

class BinaryNode:
    value: Any
    left_child: 'BinaryNode'
    right_child: 'BinaryNode'

    def __init__(self,value):

        self.value = value
        self.left_child = None
        self.right_child = None

    def min(self):
        if self.left_child is None:
            return self
        else:
            return self.left_child.min()

class BinarySearchTree:
    root: BinaryNode

    def __init__(self, value: Any):
        self.root = value

    def insert(self,value):
        self._insert(self.root, value)
        return self

    def insert_list(self,list: Any):
        for element in list:
            self.insert(element)

    def _insert(self,node, value):
        if node is None:
            node = value
        elif value.value < node.value:
            node.left_child = self._insert(node.left_child,value)
        else:
            node.right_child = self._insert(node.right_child,value)
        return node

    def contains(self, value:Any):
        curr_node = self.root

        while curr_node.value != value and curr_node is not None:
            if curr_node.value < value:
                curr_node = curr_node.right_child
            elif curr_node.value > value:
                curr_node = curr_node.left_child

        if curr_node.value == value:
            return True
        else:
            return False

    def remove(self,value:Any):
        self._remove(self.root,value)
        return self

    def _remove(self,node: BinaryNode, value:Any):

        if node is not None:
            if value == node.value:
                if node.left_child is None and node.right_child is None:
                    node = None
                    return node
                elif node.left_child is None and node.right_child is not None:
                    node = node.right_child
                    return node
                elif node.right_child is None and node.left_child is not None:
                    node = node.left_child
                    return node

                node.value = node.right_child.min().value
                node.right_child = self._remove(node.right_child,value)

            elif value < node.value:
                node.left_child = self._remove(node.left_child, value)
            else:
                node.right_child = self._remove(node.right_child, value)

        return node

    def show(self):
        G = nx.Graph()
        q = queue.Queue()

        q.put(self.root)
        while not q.empty():
            node = q.get()
            if node.left_child is not None:
                q.put(node.left_child)
                G.add_edge(node.value, node.left_child.value)
            if node.right_child is not None:
                q.put(node.right_child)
                G.add_edge(node.value, node.right_child.value)

        nx.draw(G, with_labels=True)
        plt.show()



node = BinaryNode(8)
node_3 = BinaryNode(3)
node_10 = BinaryNode(10)
node_1 = BinaryNode(1)
node_6 = BinaryNode(6)
node_14 = BinaryNode(14)
node_4 = BinaryNode(4)
node_7 = BinaryNode(7)
node_13 = BinaryNode(13)



root = BinarySearchTree(node)



# print(root.insert(node_3))
# print(root.insert(node_10))
# print(root.insert(node_1))
# print(root.insert(node_6))
# print(root.insert(node_14))
# print(root.insert(node_4))
# print(root.insert(node_7))
# print(root.insert(node_13))

lista = [node_3,node_10,node_1,node_6,node_14,node_4,node_7,node_13]
root.insert_list(lista)

print(root.root.value)
print(root.contains(10))
root.remove(4)
print(root.root.left_child.right_child.value)

