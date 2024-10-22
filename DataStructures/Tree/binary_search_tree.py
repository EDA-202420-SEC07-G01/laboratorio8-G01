from DataStructures.Tree import bst_node as bn

def new_map():
    
    binary_search_tree = {
        'root' : None,
        'size' : 0,
        'type' : 'BST'
    }
    
    return binary_search_tree

def put(my_bst, key, value):
    
    if my_bst is None:
        my_bst = new_map()
        return my_bst
    
    if 'root' in my_bst:
        root = my_bst['root']
    else:
        root = my_bst
    
    if root is None:
        root = my_bst['root'] = bn.new_node(key, value)
        root['size'] = 1
        return my_bst
    else:
        if root['key'] == key:
            root['value'] = value
            return my_bst
        
        elif key < root['key']:
            if root['left'] is None:
                root['left'] = bn.new_node(key, value)
                root['size'] += 1
            else:
                put(root['left'], key, value)

        elif key > root['key']:
            if root['right'] is None:
                root['right'] = bn.new_node(key, value)
                root['size'] += 1
            else:
                put(root['right'], key, value)
                
    root['size'] = 1
    if root['left'] is not None:
        root['size'] += root['left']['size']
    if root['right'] is not None:
        root['size'] += root['right']['size']
                
    return my_bst
