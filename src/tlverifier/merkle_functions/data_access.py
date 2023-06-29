import json
import random

from pymerkle_logsTransparentes import MerkleProof


def get_proof():
    file = open("../mock/mock_dev/v3/t1_proof_leaf11.json", "r")
    json_file = json.loads(file.read())
    file.close()
    proof = json_file
    return proof


def get_proof_global_tree():
    file = open("../mock/mock_dev/v3/tg_proof_root1.json", "r")
    json_file = json.loads(file.read())
    file.close()
    proof = json_file['proof']
    return proof


def get_trusted_global_root():
    file = open("../mock/mock_dev/v3/tg_root.json", "r")
    json_file = json.loads(file.read())
    file.close()
    root_global = json_file['value']
    return root_global


def get_partial_global_roots():
    file = open("../mock/mock_dev/v3/partial_global_roots.json", "r")
    json_file = json.loads(file.read())
    file.close()
    return json_file


def get_middle_last_roots_from_partial_global():
    # get partial roots with tree_sizes
    partial_global_roots = get_partial_global_roots()
    roots = partial_global_roots["roots"]

    # select a middle root randomly
    random_middle_index = random.randint(1, len(roots) - 2)
    random_middle_root = roots[random_middle_index]
    middle_root_value = random_middle_root["value"]

    # select last root
    random_last_index = random_middle_index + 1
    last_root = roots[random_last_index]
    last_root_value = last_root["value"]

    # get consistency proof of middle root
    proofs = get_all_consistency_proof_global()["proofs"]   # get proofs from all_consistency_proof_global
    middle_merkle_proof = None
    for proof in proofs:
        if proof["root"]["value"] == last_root_value:
            middle_proof = proof["consistency_proof"]
            middle_merkle_proof = MerkleProof.deserialize(middle_proof)
            break

    # transform roots to bytes
    middle_root_bytes = bytes(middle_root_value, "utf_8")
    last_root_bytes = bytes(last_root_value, "utf_8")

    return middle_root_bytes, middle_merkle_proof, last_root_bytes


def get_local_root():
    file = open("../mock/mock_dev/v3/t1_root.json", "r")
    json_file = json.loads(file.read())
    file.close()
    root_global = json_file['value']
    return root_global


def get_all_leaf_global_tree():
    file = open("../mock/mock_dev/v3/all_leaf_global_tree.json", "r")
    json_file = json.loads(file.read())
    file.close()
    return json_file


def get_all_consistency_proof():
    file = open("../mock/mock_dev/v3/all_consistency_proof_tree1.json", "r")
    json_file = json.loads(file.read())
    file.close()
    return json_file


def get_all_consistency_proof_global():
    file = open("../mock/mock_dev/v3/all_consistency_proof_global.json", "r")
    json_file = json.loads(file.read())
    file.close()
    return json_file


def get_tree_name():
    return "tree1"


def get_data():
    return b"leaf11"


if __name__ == '__main__':
    get_middle_last_roots_from_partial_global()
