def check(root, min_, max_):
    return (root is None or 
            (root.data < max_ and root.data > min_ and 
             check(root.left, min_, root.data) and 
             check(root.right, root.data, max_)))

def check_binary_search_tree_(root):
    return check(root, -float('inf'), float('inf'))