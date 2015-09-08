# encoding: utf-8
from fp_tree import FPTree

def test_data():
    """Create test data
    """
    simple_data = [['r', 'z', 'h', 'j', 'p'],
                   ['z', 'y', 'x', 'w', 'v', 'u', 't', 's'],
                   ['z'],
                   ['r', 'x', 'n', 'o', 's'],
                   ['y', 'r', 'x', 'z', 'q', 't', 'p'],
                   ['y', 'z', 'x', 'e', 'q', 's', 't', 'm']]
    return simple_data

def initialize_data(data):
    """format data for function create_tree
    """
    init_set = {}
    for trans in data:
        # forzenset: sets that cannot change and can be used for keys in dict.
        init_set[frozenset(trans)] = 1
    return init_set

# sort items according to its frequency
def create_header_table(init_set, min_support=1):
    header_table = {}
    for items in init_set:
        for item in items:
            header_table[item] = header_table.get(item, 0) + init_set[items]
    for key in header_table.keys():
        if header_table[key] < min_support:
            header_table.pop(key)
    return header_table

def create_tree(init_set, header_table):
    freq_item_set = set(header_table.keys())
    if not len(freq_item_set):
        return None, None
    for key in header_table:
        header_table[key] = [header_table[key], None]
    fp_tree = FPTree('Null Set', 1, None)

    # Order each tran_set by their frequency and add it to fp_tree.
    for tran_set, count in init_set.items():
        frequency = {}
        for item in tran_set:
            if item in freq_item_set:
                frequency[item] = header_table[item][0]
        if len(frequency):
            ordered_items = [v[0] for v in sorted(frequency.items(),
                                           key=lambda p: p[1],
                                           reverse=True)]
            update_tree(ordered_items, fp_tree, header_table, count)
    return fp_tree, header_table

def update_tree(items, fp_tree, header_table, count):
    if items[0] in fp_tree.child:
        fp_tree.child[items[0]].increase(count)
    else:
        fp_tree.child[items[0]] = FPTree(items[0], count, fp_tree)
        if not header_table[items[0]][1]:
            header_table[items[0]][1] = fp_tree.child[items[0]]
        else:
            update_header(header_table[items[0]][1], fp_tree.child[items[0]])
    if len(items) > 1:
        update_tree(items[1::], fp_tree.child[items[0]], header_table, count)

def update_header(node_to_test, target_node):
    while node_to_test.link_of_node:
        node_to_test = node_to_test.link_of_node
        node_to_test.link_of_node = target_node
