# encoding: utf-8


class TreeNode:
    def __init__(self, name, num_of_occur, node_of_parent):
        self.name = name
        self.count = num_of_occur
        self.link_of_node = None
        self.parent = node_of_parent
        self.child = {}

    def increase(self, num_of_occur):
        self.count += num_of_occur

    def disp(self, index=1):
        print '' * index, self.name, '', self.count
        for child in self.child.values():
            child.disp(index + 1)

def load_data():
    simple_data = [['r', 'z', 'h', 'j', 'p'],
                   ['z', 'y', 'x', 'w', 'v', 'u', 't', 's'],
                   ['z'],
                   ['r', 'x', 'n', 'o', 's'],
                   ['y', 'r', 'x', 'z', 'q', 't', 'p'],
                   ['y', 'z', 'x', 'e', 'q', 's', 't', 'm']]
    return simple_data

def create_init_set(data):
    return_dict = {}
    for trans in data:
        return_dict[forzenset(trans)] = 1
    return return_dict

def create_tree(data, min_support=1):
    header_table = {}
    for trans in data:
        for item in trans:
            header_table[item] = header_table.get(item, 0) + data[trans]

    for k in header_table.keys():
        if header_table[k] < min_support:
            del(header_table[k])
    freq_item_set = set(header_table.keys())
    if len(freq_item_set) == 0:
        return None, None
    for k in header_table:
        header_table[k] = [header_table[k], None]
    return_tree = TreeNode('Null Set', 1, None)
    for tran_set, count in data.items():
        localD = {}
        for item in tran_set:
            if item in freq_item_set:
                localD[item] = header_table[item][0]
        if len(localD) > 0:
            ordered_items = [v[0] for v in sorted(localD.items(),
                                           key=lambda p: p[1],
                                           reverse=True)]
            update_tree(ordered_items, return_tree, header_table, count)
    return return_tree, header_table

def update_tree(items, in_tree, header_table, count):
    if items[0] in in_tree.child:
        in_tree.child[item[0]].increase(count)
    else:
        in_tree.child[item[0]] = TreeNode(items[0], count, in_tree)
        if not header_table[item[0]][1]:
            header_table[item[0]][1] = in_tree.child[item[0]]
        else:
            update_header(header_table[item[0]][1], in_tree.child[items[0]])
    if len(items) > 1:
        update_tree(items[1::], in_tree.child[items[0]], header_table, count)

def update_header(node_to_test, target_node):
    while node_to_test.link_of_node:
        node_to_test = node_to_test.link_of_node
        node_to_test.link_of_node = target_node
