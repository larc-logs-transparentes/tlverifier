import json


def get_proof():
    file = open("../mock/mock_dev/t1_proof_bar.json", "r")
    json_file = json.loads(file.read())
    file.close()
    proof = json_file
    return proof


def get_proof_global_tree():
    file = open("../mock/mock_dev/tg_proof_root1.json", "r")
    json_file = json.loads(file.read())
    file.close()
    proof = json_file['proof']
    return proof


def get_trusted_global_root():
    file = open("../mock/mock_dev/tg_root.json", "r")
    json_file = json.loads(file.read())
    file.close()
    root_global = json_file['value']
    return root_global


def get_local_root():
    file = open("../mock/mock_dev/t1_root.json", "r")
    json_file = json.loads(file.read())
    file.close()
    root_global = json_file['value']
    return root_global


def get_data():
    return b'bar'
