def find_left_height(root):
    height = 0
    while root.left:
        root = root.left
        height += 1
    return height

def find_right_height(root):
    height = 0
    while root.right:
        root = root.right
        height += 1
    return height

def count_nodes(root):
    if not root:
        return 0
    left = find_left_height(root)
    right = find_right_height(root)

    if left == right:
        return (2 << left) - 1
    else:
        return count_nodes(root.left) + count_nodes(root.right) + 1


class Node:
	
	def __init__(self, data = 0, left = None, right = None):
		self.left = left
		self.right = right
		self.data = data
	
	def printtree(self):
		print(self.data)
		
objleft2 = Node(2)
objleft = Node(4, objleft2)
objright = Node(8)
root = Node(6, objleft, objright)

print(count_nodes(root))
