import time
from matplotlib import pyplot as plt


class Node:
    def __init__(self, val):
        self.l = None
        self.r = None
        self.v = val

class Tree:
    def __init__(self):
        self.root = None

    def getRoot(self):
        return self.root

    def add(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            self._add(val, self.root)

    def _add(self, val, node):
        if val < node.v:
            if node.l is not None:
                self._add(val, node.l)
            else:
                node.l = Node(val)
        else:
            if node.r is not None:
                self._add(val, node.r)
            else:
                node.r = Node(val)

    def find(self, val):
        if self.root is not None:
            return self._find(val, self.root)
        else:
            return None

    def _find(self, val, node):
        if val == node.v:
            return node
        elif (val < node.v and node.l is not None):
            self._find(val, node.l)
        elif (val > node.v and node.r is not None):
            self._find(val, node.r)

    def deleteTree(self):
        # garbage collector will do this for us.
        self.root = None

    def printTree(self):
        if self.root is not None:
            self._printTree(self.root)

    def _printTree(self, node):
        if node is not None:
            self._printTree(node.l)
            print(str(node.v) + ' ')
            self._printTree(node.r)

dict_binarytree = Tree()
dict_hashtable = {}

dict_bt_time = []
dict_ht_time = []
dict_num_insertions = []

num_insertions = 1
more_than_three = False

while (True):
    dict_num_insertions.append(num_insertions)
    dict_hashtable = {}
    dict_binarytree = Tree()

    ht_t_1 = time.time()
    for i in range(num_insertions):
        dict_hashtable[i] = str(i)
    ht_t_2 = time.time()
    dict_ht_time.append(ht_t_2 - ht_t_1)
    if (dict_ht_time[-1] > 3):
        more_than_three = True

    bt_t_1 = time.time()
    for i in range(num_insertions):
        dict_binarytree.add(str(i))
    bt_t_2 = time.time()
    dict_bt_time.append(bt_t_2 - bt_t_1)
    if (more_than_three or dict_bt_time[-1] > 3):
        break

    num_insertions = num_insertions * 10

plt.plot(dict_num_insertions, dict_ht_time, label="Hashtable",c = 'r')
plt.plot(dict_num_insertions, dict_bt_time, label="Binarytree",c = 'b')
plt.axhline(y=3 ,ls=":",c="g")
plt.legend()
plt.xlabel("Number of Insertions (N)")
plt.xscale("log")
plt.ylabel("Insertion Time of Algorithm (seconds)")
plt.show()

# Referemces:
# Hash table: https://mail.python.org/pipermail/python-list/2000-March/048085.html
# Binary tree: http://codeforces.com/blog/entry/58480