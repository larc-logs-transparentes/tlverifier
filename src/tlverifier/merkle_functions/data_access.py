import json


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
