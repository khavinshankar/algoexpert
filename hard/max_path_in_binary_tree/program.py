# time = O(n) and space = O(log(n)) => n = num_nodes(tree)
def maxPathSum(tree):
    return maxPathSumHelper(tree)[1]

def maxPathSumHelper(tree):
    if not tree: return 0, 0

    left_branch_sum, left_sum = maxPathSumHelper(tree.left)
    right_branch_sum, right_sum = maxPathSumHelper(tree.right)
    
    max_child_branch_sum = max(left_branch_sum, right_branch_sum)
    curr_branch_sum = max(max_child_branch_sum + tree.value, tree.value)

    curr_node_sum = max(curr_branch_sum, left_branch_sum + tree.value + right_branch_sum)
    max_curr_node_sum = max(left_sum, curr_node_sum, right_sum)

    return curr_branch_sum, max_curr_node_sum