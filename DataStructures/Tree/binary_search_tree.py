from DataStructures.Tree import bst_node as bn
from DataStructures.List import array_list as al
from DataStructures.List import single_linked_list as sl
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
    
    my_bst['root'] = insert_node(root, key, value)
    my_bst['size'] = size(my_bst)
    
def compare_keys(key, key_node):
    if key > key_node:
        return 1
    elif key < key_node:
        return -1
    else:
        return 0
 
def insert_node(node, key, value):
    if (node == None):
        return bn.new_node(key, value)
   
    cmp = compare_keys(key, node['key'])
    if (cmp < 0):
        node['left'] = insert_node(node['left'], key, value)
    elif (cmp > 0):
        node['right'] = insert_node(node['right'], key, value)
    else:
        node['value'] = value
    node['size'] = size_tree(node['left']) + size_tree(node['right']) + 1
    return node

#Funciones para calcular tamaño del nodo

def size(my_bst):
    return size_tree(my_bst['root'])
 
def size_tree(node):
    if node is None:
        return 0
    else:
        return node['size']
    
#Función para obtener el valor asociado a una llave en el arbol
def get(my_bst, key):
    return get_node(my_bst['root'], key)
 
def get_node(node, key):
    if (node == None):
        return None
    cmp = compare_keys(key, node['key'])
    if (cmp < 0):
        return get_node(node['left'], key)
    elif (cmp > 0):
        return get_node(node['right'], key)
    else:
        return node['value']
    
#Función que elimina pareja llave-valor que coincidad con key

def remove(my_bst, key):
    if my_bst['root'] is None:
        return my_bst
    my_bst['root'] = remove_node(my_bst['root'], key)
    return my_bst
    
def remove_node(node, key):
    if node is None:
        return None

    cmp = compare_keys(key, node['key'])
    
    if cmp < 0:
        node['left'] = remove_node(node['left'], key)
        
    elif cmp > 0:
        node['right'] = remove_node(node['right'], key)
        
    else:
        if node['left'] is None and node['right'] is None:
            return None
        
        elif node['left'] is None:
            return node['right']
        
        elif node['right'] is None:
            return node['left']
        
        else:
            lower_node = min_tree(node['right'])  
            
            node['key'] = lower_node['key']
            
            node['right'] = remove_node(node['right'], lower_node['key'])
    
    node['size'] = 1 + (node['left']['size'] if node['left'] else 0) + (node['right']['size'] if node['right'] else 0)
    
    return node

#Función informa si la llave key se encuentra en el arbol

def contains(my_bst, key):
    if get(my_bst, key) == None:
        return False
    else:
        return True
    
#Función para retornar la mínima llave en el arbol
    
def min_key(my_bst):
    if my_bst is None:
        return None
    
    min_key_v = min_tree(my_bst['root'])
    
    if min_key_v != None:
        return min_key_v['key']
    return min_key_v
 
def min_tree(node):
    if node == None:
        return None
    if (node['left'] == None):
        return node
    return min_tree(node['left'])

#Función para retornar la máxima llave en el arbol

def max_key(my_bst):
    max_key_v = max_tree(my_bst['root'])
    if max_key_v != None:
        return max_key_v['key']
    return max_key_v
 
def max_tree(node):
    if node == None:
        return None
    if (node['right'] == None):
        return node
    return max_tree(node['right'])
    
# Función para ver si el arbol esta vacio

def is_empty(my_bst):
    return my_bst['root'] == None

# Funcion que retorna una lista con todas las llaves de la tabla.

def key_set(my_bst):
    lst = al.new_list()
    pila = []
    root = my_bst['root']
    if my_bst['root'] == None:
        return lst
    key_set_tree(root, pila, min_key(my_bst), max_key(my_bst))
    lst['elements'] = pila
    lst['size'] = len(pila)
    return lst


def key_set_tree(node, pila, key_low, key_high):
    if (node == None):
        return None
    cmp_low = compare_keys(key_low, node['key'])
    cmp_high = compare_keys(key_high, node['key'])
    if cmp_low < 0:
        key_set_tree(node['left'], pila, key_low, key_high)
    if cmp_low <= 0 and cmp_high >= 0:
        pila.append(node['key'])
    if cmp_high > 0:
        key_set_tree(node['right'], pila, key_low, key_high)
        
# Funcion que retorna una lista con todas las llaves de la tabla.
        
def value_set(my_bst):
    lst = al.new_list()
    pila = []
    root = my_bst['root']
    if my_bst['root'] == None:
        return lst
    value_set_tree(root, pila, min_key(my_bst), max_key(my_bst))
    lst['elements'] = pila
    lst['size'] = len(pila)
    return lst


def value_set_tree(node, pila, key_low, key_high):
    if (node == None):
        return None
    cmp_low = compare_keys(key_low, node['key'])
    cmp_high = compare_keys(key_high, node['key'])
    if cmp_low < 0:
        value_set_tree(node['left'], pila, key_low, key_high)
    if cmp_low <= 0 and cmp_high >= 0:
        pila.append(node['value'])
    if cmp_high > 0:
        value_set_tree(node['right'], pila, key_low, key_high)
        
#Eliminar el mínimo elemento del arbol
def delete_min(my_bst):
    if my_bst['root'] == None:
        return my_bst
    my_bst['root'] = delete_min_node(my_bst['root'])
 
def delete_min_node(node):
    if (node['left'] == None):
        return node['right']
    node['left'] = delete_min_node(node['left'])
    node['size'] = size_tree(node['left']) + size_tree(node['right']) + 1
    return node
 
#Eliminar el máximo elemento del arbol
def delete_max(my_bst):
    if my_bst['root'] == None:
        return my_bst
    my_bst['root'] = delete_max_node(my_bst['root'])
 
def delete_max_node(node):
    if (node['right'] == None):
        return node['left']
    node['right'] = delete_max_node(node['right'])
    node['size'] = size_tree(node['right']) + size_tree(node['left']) + 1
    return node

def floor(my_bst, key):
    return floor_key(my_bst['root'], key)

def floor_key(node, key):
    if node is None:
        return None
    
    cmp = compare_keys(key, node['key'])
    
    if cmp == 0:
        return node['key']
    elif cmp < 0:
        return floor_key(node['left'], key)
    else:
        right_floor = floor_key(node['right'], key)
        return right_floor if right_floor is not None else node['key']
    
def ceiling(my_bst, key):
    return ceiling_key(my_bst['root'], key)

def ceiling_key(node, key):
    if node is None:
        return None
    
    cmp = compare_keys(key, node['key'])
    
    if cmp == 0:
        return node['key']
    elif cmp > 0:
        return ceiling_key(node['right'], key)
    else:
        left_ceiling = ceiling_key(node['left'], key)
        return left_ceiling if left_ceiling is not None else node['key']

def select(my_bst, pos):
    if pos < 0 or pos >= my_bst['size']:
        return None
    return select_key(my_bst['root'], pos)

def select_key(node, pos):
    if node is None:
        return None
    
    left_size = size_tree(node['left'])
    
    if pos < left_size:
        return select_key(node['left'], pos)
    elif pos > left_size:
        return select_key(node['right'], pos - left_size - 1)
    else:
        return node['key']    

def rank(my_bst, key):
    return rank_keys(my_bst['root'], key)

def rank_keys(node, key):
    if node is None:
        return 0
    
    cmp = compare_keys(key, node['key'])
    
    if cmp < 0:
        return rank_keys(node['left'], key)
    elif cmp > 0:
        return 1 + size_tree(node['left']) + rank_keys(node['right'], key)
    else:
        return size_tree(node['left'])
    
def height(my_bst):
    return height_tree(my_bst['root'])

def height_tree(node):
    if node is None:
        return -1
    left_height = height_tree(node['left'])
    right_height = height_tree(node['right'])
    return max(left_height, right_height) + 1