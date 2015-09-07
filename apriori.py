#encoding: utf-8

# Apriori algorithm helper functions
def load_data_set():
    """ create a sample data set for testing create_c1() and scan_d"""
    return [[1, 3, 4], [2, 3, 5], [1, 2, 3, 5], [2, 5]]

def create_c1(dataset):
    """create a frozenset of each item in c1"""
    # c1 is a list containing just one item for each element.
    c1 = []
    for transaction in dataset:
        for item in transaction:
            if not [item] in c1:
                c1.append([item])
    c1.sort()
    return map(frozenset, c1)

def scan_d(d, ck, min_support):
    """calculate support for every itemset"""
    ss_cnt = {}
    # d == map(set, load_data_set())
    for tid in d:
        # ck = creatr_c1()
        for can in ck:
            if can.issubset(tid):
                if not ss_cnt.has_key(can):
                    ss_cnt[can] = 1
                else:
                    ss_cnt[can] += 1
    num_items = float(len(d))
    ret_list = []
    support_data = {}
    for key in ss_cnt:
        support = ss_cnt[key] / num_items
        # min_support is minimum support
        if support >= min_support:
            ret_list.insert(0, key)
        support_data[key] = support
    return ret_list, support_data

def apriori_gen(lk, k):
    """create candidate itemsets: ck"""
    ret_list = []
    # lk is the list of frequent itemsets
    len_of_lk = len(lk)
    for i in range(len_of_lk):
        for j in range(i+1, len_of_lk):
            l1 = list(lk[i])[:k-2]
            l2 = list(lk[j])[:k-2]
            l1.sort()
            l2.sort()
            if l1 == l2:
                ret_list.append(lk[i] | lk[j])
    return ret_list

def apriori(dataset, min_support=0.5):
    c1 = create_c1(dataset)
    d = map(set, dataset)
    l1, support_data = scan_d(d, c1, min_support)
    l = [l1]
    k = 2
    while (len(l[k-2]) > 0):
        ck = apriori_gen(l[k-2], k)
        lk, sup_k = scan_d(d, ck, min_support)
        support_data.update(sup_k)
        l.append(lk)
        k += 1
    return l, support_data
