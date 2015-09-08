# encoding utf-8


class FPTree:
    def __init__(self, name, num_of_occur, node_of_parent):
        self.node_name = name
        self.count = num_of_occur
        self.link_of_node = None
        self.parent = node_of_parent
        self.child = {}

    def increase(self, num_of_occur):
        self.count += num_of_occur

    def disp(self, index=1):
        print ' ' * ind, self.node_name, ' ', self.count
        for child in self.child.values():
            child.disp(index + 1)
