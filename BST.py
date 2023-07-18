class Node:
    def __init__(self,key):
        self.key=key
        self.left=None
        self.right=None


def insert(node,key):
    if node is None:
        return Node(key)

    if key< node.key:
            node.left=insert(node.left,key)

    else:
        node.right=insert(node.right,key)

    return node


def Binary_search_tree(node,target):
    if node is Node or target== node.key:
        return node

    if target<node.key:
        return Binary_search_tree(node.left,target)
    else:
        return Binary_search_tree(node.right,target)




node=None

target=6

values=[8, 3, 10, 1, 6, 14, 4, 7, 13]

for key in values:
    node=insert(node,key)


print(bool(Binary_search_tree(node,target)))    