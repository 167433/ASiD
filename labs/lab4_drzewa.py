from typing import Any, List
import queue
import matplotlib.pyplot as plt
import networkx as nx


class TreeNode:
    value: Any
    children: List['TreeNode']

    def __init__(self,value):
        self.children = []
        self.value = value

    def is_leaf(self):
        if len(self.children) == 0:
            return True
        else:
            return False

    def add(self,child: 'TreeNode'):
        self.children.append(child)

    def for_each_deep_first(self,visit):
        visit(self.value)
        if self.children != []:
            for child in self.children:
                child.for_each_deep_first(visit)

    def for_each_lvl_order(self,visit):
        visit(self.value)
        q = queue.Queue()
        q.put(self.children)

        while not q.empty():
            for child in q.get():
                visit(child.value)
                q.put(child.children)

    def search(self, value:Any):

        if self.value == value.value:
            return True

        q = queue.Queue()
        q.put(self.children)

        while not q.empty():
            for child in q.get():
                if child.value == value.value:
                    return True
                q.put(child.children)
        return False


    def __str__(self):
        return str(self.value)


class Tree:
    root: TreeNode

    def __init__(self, root: Any):
        self.root = root

    def add(self,value: Any, parent_name: Any):

        if self.root.search(parent_name):
            if isinstance(value, TreeNode):
                nowe_dziecko = value
            else:
                nowe_dziecko = TreeNode(value)

            if self.root == parent_name:
                self.root.add(nowe_dziecko)

            q = queue.Queue()
            q.put(self.root.children)

            while not q.empty():
                for child in q.get():
                    if child == parent_name:
                        child.add(value)
                        break
                    q.put(child.children)
        else:
            print("Nie udało sie")

    def for_each_level_order(self, visit: Any) -> None:
        return self.root.for_each_lvl_order(visit)

    def for_each_deep(self,visit: Any) -> None:
        return self.root.for_each_deep_first(visit)

    def show(self):

        G = nx.Graph()
        q = queue.Queue()
        q.put(self.root.children)

        if self.root.children != []:
            for child in self.root.children:
                G.add_edge(self.root,child)

        while not q.empty():
            for child in q.get():
                for kid in child.children:
                    G.add_edge(child,kid)
                q.put(child.children)

        # Rysuj graf
        nx.draw(G, with_labels=True)
        plt.show()

root = TreeNode('F')
B = TreeNode('B')
G = TreeNode('G')
A = TreeNode('A')
I = TreeNode('I')
D = TreeNode('D')
C = TreeNode('C')
E = TreeNode('E')
H = TreeNode('H')

# root.add(B)
# root.add(G)
#
# B.add(A)
# B.add(D)
#
# G.add(I)
#
# D.add(C)
# D.add(E)
#
# I.add(H)

#root.for_each_lvl_order(print)

#root = TreeNode('F')

korzen = Tree(root)
korzen.add(B,root)
korzen.add(G,root)

korzen.add(A,B)
korzen.add(D,B)

korzen.add(I,G)

korzen.add(C,D)
korzen.add(E,D)

korzen.add(H,I)

korzen.for_each_level_order(print)
print("----")
korzen.for_each_deep(print)
korzen.show()



