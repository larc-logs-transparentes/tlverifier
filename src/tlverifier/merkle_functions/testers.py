from data_access import get_data, get_proof, get_local_root, get_trusted_global_root, get_proof_global_tree
from src.tlverifier.merkle_functions.tl_functions import verify_single_data, verify_inclusion_proof, verify_consistency_proof
from tree_mocker import make_tree


def test_inclusion_proof():
    proof = get_proof()
    root = get_local_root()
    data = get_data()
    print(verify_inclusion_proof(proof, root, data))


def test_single_data():
    proof = get_proof()     # insert global root in this proof
    # local_root = get_local_root()
    # proof_global = get_proof_global_tree()
    trustable_global_root = get_trusted_global_root()
    data = get_data()
    result = verify_single_data(proof, trustable_global_root, data)
    print(result)


def test_consistency_proof():
    tree = make_tree([b'foo', b'bar', b'baz', b'qux', b'tev'])
    sub_root = tree.root
    sub_length = tree.length
    tree.append_entry(b'kjh')
    local_root_new = tree.root
    proof = tree.prove_consistency(sub_length, sub_root)
    print(verify_consistency_proof(sub_root, local_root_new, proof))


if __name__ == '__main__':
    test_single_data()
