class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
    
    # time = O(n) and space = O(1)
    def insert(self, value):
        curr = prev = self
        while curr:
            prev = curr
            if value < curr.value: curr = curr.left
            else: curr = curr.right
        
        node = BST(value)
        if value < prev.value: prev.left = node
        else: prev.right = node

        return self

    # time = O(n) and space = O(1)
    def remove(self, value):
        parent = None
        curr = self
        while curr:
            if curr.value == value: break
            parent = curr
            if value < curr.value: curr = curr.left
            else: curr = curr.right
        
        if curr is None: return

        if curr.left is None and curr.right is None:
            if parent:
                if parent.left == curr: parent.left = None
                else: parent.right = None
        elif curr.left is None:
            if parent:
                if parent.left == curr: parent.left = curr.right
                else: parent.right = curr.right
            else:
                self = curr.right
        elif curr.right is None:
            if parent:
                if parent.left == curr: parent.left = curr.left
                else: parent.right = curr.left
            else:
                self = curr.left
        else:
            right_smallest, right_smallest_parent = self.smallest(curr.right)
            right_smallest_parent.left = right_smallest.right
            node = BST(right_smallest.value, curr.left, curr.right)
            if parent:
                if parent.left == curr: parent.left = node
                else: parent.right = node
            else:
                self = node
            
            del right_smallest

        del curr
        return self

    # time = O(n) and space = O(1)
    def contains(self, value):
        curr = self
        while curr:
            if curr.value == value: return True
            elif value < curr.value: curr = curr.left
            else: curr = curr.right
        
        return False

    def smallest(self, root):
        parent = None
        curr = root
        while curr.left:
            parent = curr 
            curr = curr.left
        return curr, parent

