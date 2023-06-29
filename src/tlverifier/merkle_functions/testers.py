from data_access import get_data, get_proof, get_local_root, get_trusted_global_root, get_all_leaf_global_tree, get_all_consistency_proof, get_partial_global_roots, get_all_consistency_proof_global, get_middle_last_roots_from_partial_global
from src.tlverifier.merkle_functions.tl_functions import verify_single_data, verify_inclusion_proof, verify_consistency_proof, verify_local_tree_history_consistency, verify_global_tree_history_consistency


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
    middle_root_value, middle_proof, last_root_value = get_middle_last_roots_from_partial_global()
    print(verify_consistency_proof(middle_root_value, last_root_value, middle_proof))


def test_verify_local_tree_history_consistency():
    all_leaf_global = get_all_leaf_global_tree()
    all_consistency = get_all_consistency_proof()
    global_root = get_trusted_global_root()
    tree_name = "tree1"
    print(verify_local_tree_history_consistency(all_leaf_global, all_consistency, global_root, tree_name))


def test_verify_global_tree_history_consistency():
    consistency_proofs = get_all_consistency_proof_global()
    consistency_proofs_stored = get_partial_global_roots()
    print(verify_global_tree_history_consistency(consistency_proofs, consistency_proofs_stored))


if __name__ == '__main__':
    # test_inclusion_proof()
    # test_single_data()
    test_consistency_proof()
    # test_verify_local_tree_history_consistency()
    # test_verify_global_tree_history_consistency()
