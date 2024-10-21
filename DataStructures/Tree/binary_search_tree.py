from DataStructures.Tree import bst_node as bn

def new_map():
    
    binary_search_tree = {
        'root' : None,
        'size' : 0,
        'type' : 'BST'
    }
    
    return binary_search_tree

def put(my_bst, key, value):
    
    if my_bst['root'] is None:
        my_bst['root'] = bn.new_node(key,value)
        my_bst['size'] += 1
        return my_bst
    
    root = my_bst['root']
        
    if root['key'] == key:
        root['value'] = value
        return my_bst
            
    if key < root['key']:
        if root['left'] is None:
            root['left'] = bn.new_node(key, value)
            my_bst['size'] += 1
        else:
            put(root['left'], key, value)
    else:
        if root['right'] is None:
            root['right'] = bn.new_node(key, value)
            my_bst['size'] += 1
        else:
            put(root['right'], key, value)
            
    return my_bst