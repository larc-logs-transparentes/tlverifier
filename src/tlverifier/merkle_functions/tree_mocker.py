from pymerkle import MerkleTree


def make_tree(list_of_data):
    m_tree = MerkleTree()
    for data in list_of_data:
        m_tree.append_entry(data)
    return m_tree


def make_all_trees():
    tree_1 = make_tree([b'foo', b'bar', b'baz', b'qux', b'tev'])
    tree_2 = make_tree([b'123', b'234', b'345', b'456', b'567'])
    tree_3 = make_tree([b'seg', b'ter', b'qua', b'qui', b'sex'])
    tree_g = make_tree([tree_1.root, tree_2.root, tree_3.root])

    return tree_1, tree_2, tree_3, tree_g


if __name__ == '__main__':
    t1, t2, t3, tg = make_all_trees()
    proof = tg.prove_inclusion(t2.root)
    print(proof.serialize())
