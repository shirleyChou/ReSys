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
