import queue
from typing import Any, Callable
import matplotlib.pyplot as plt
import networkx as nx

class BinaryNode:
    value: Any
    left_child: 'BinaryNode'
    right_child: 'BinaryNode'

    def __init__(self,value: int):
        self.value = value
        self.right_child = None
        self.left_child = None

    def is_leaf(self):
        if self.left_child is None and self.right_child is None:
            return True
        return False

    def add_left_child(self, value: Any):
        if isinstance(value,BinaryNode):
            if not self.left_child is None:
                return None
            else:
                self.left_child = value
        else:
            self.left_child = BinaryNode(value)


    def add_right_child(self, value: Any):
        if isinstance(value,BinaryNode):
            if not self.right_child is None:
                return None
            else:
                self.right_child = value
        else:
            self.right_child = BinaryNode(value)


    def traverse_in_order(self,visit):

        if self.left_child is not None:
            self.left_child.traverse_in_order(visit)

        visit(self.value)

        if self.right_child is not None:
            self.right_child.traverse_in_order(visit)

    def traverse_post_order(self,visit):

        if self.left_child != None:
            self.left_child.traverse_post_order(visit)

        if self.right_child != None:
            self.right_child.traverse_post_order(visit)

        visit(self.value)

    def traverse_pre_order(self, visit):
        visit(self.value)

        if self.left_child != None:
            self.left_child.traverse_post_order(visit)

        if self.right_child != None:
            self.right_child.traverse_post_order(visit)

    def __str__(self):
        return str(self.value)

class BinaryTree:
    root: BinaryNode

    def __init__(self,value:Any):
        if isinstance(value,BinaryNode):
            self.root = value
        else:
            self.root = BinaryNode(value)

    def traverse_in_order(self,visit):
        self.root.traverse_in_order(visit)

    def traverse_post_order(self,vist):
        self.root.traverse_post_order(vist)

    def traverse_pre_order(self,visit):
        self.root.traverse_pre_order(visit)

    def show(self):
        G = nx.Graph()
        q = queue.Queue()

        q.put(self.root)
        while not q.empty():
            node = q.get()
            if node.left_child is not None:
                q.put(node.left_child)
                G.add_edge(node,node.left_child)
            if node.right_child is not None:
                q.put(node.right_child)
                G.add_edge(node, node.right_child)

        nx.draw(G,with_labels=True)
        plt.show()

root_node = BinaryNode(10)

node_2 = BinaryNode(2)
node_9 = BinaryNode(9)

root_node.add_right_child(node_2)
root_node.add_left_child(node_9)

node_3 = BinaryNode(3)
node_1 = BinaryNode(1)

node_9.add_right_child(node_3)
node_9.add_left_child(node_1)

node_4 = BinaryNode(4)
node_6 = BinaryNode(6)

node_2.add_right_child(node_6)
node_2.add_left_child(node_4)

#root_node.traverse_pre_order(print)

tree = BinaryTree(root_node)

tree.traverse_in_order(print)

tree.traverse_post_order(print)

tree.traverse_post_order(print)

tree.show()