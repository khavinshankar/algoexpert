# time = O(n) and space = O(1) => n = number of nodes
def iterativeInOrderTraversal(tree, callback):
    prev_node = None
    curr_node = tree

    while curr_node is not None:
        next_node = None
        if prev_node == None or prev_node == curr_node.parent:
            if curr_node.left:
                next_node = curr_node.left
            else:
                callback(curr_node)
                next_node = curr_node.right if curr_node.right else curr_node.parent
        elif prev_node == curr_node.left:
            callback(curr_node)
            next_node = curr_node.right if curr_node.right else curr_node.parent
        else:
            next_node = curr_node.parent
        
        prev_node = curr_node
        curr_node = next_node