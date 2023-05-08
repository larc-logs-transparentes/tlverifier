from data_access import get_data, get_proof, get_local_root, get_trusted_global_root, get_proof_global_tree
from src.tlverifier.merkle_functions.tl_functions import verify_single_data, verify_inclusion_proof, verify_consistency_proof
from tree_mocker import make_tree


def test_inclusion_proof():
    proof = get_proof()["local_tree"]["inclusion_proof"]    # incusion proof extracted from whole proof object
    root = get_local_root()
    data = get_data()   # raw data in bytes
    print(verify_inclusion_proof(proof, root, data))


def test_single_data():
    proof = get_proof()     # whole proof, verify_single_data(...) derives internal data from it
    trustable_global_root = get_trusted_global_root()
    data = get_data()       # raw data in bytes
    result = verify_single_data(proof, trustable_global_root, data)
    print(result)


def test_consistency_proof():
    tree = make_tree([b'foo', b'bar', b'baz', b'qux', b'tev'])  # create tree
    sub_root = tree.root    # get root (will be partial)
    sub_length = tree.length    # get length
    tree.append_entry(b'kjh')   # append new leaf
    local_root_new = tree.root  # get new root
    proof = tree.prove_consistency(sub_length, sub_root)    # get proof of tree consistency
    print(verify_consistency_proof(sub_root, local_root_new, proof))


if __name__ == '__main__':
    test_inclusion_proof()
    test_single_data()
    test_consistency_proof()
