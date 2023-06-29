from pymerkle_logsTransparentes import MerkleTree, MerkleProof, verify_inclusion, verify_consistency
from pymerkle_logsTransparentes.tree import InvalidChallenge
from pymerkle_logsTransparentes.proof import InvalidProof


def verify_inclusion_proof(proof, root, data, expected_index=None):
    """"
    # expected index:
    # index of data must be in the expected index
    # to get actual index use the int values of path
    """
    try:
        proof_des = MerkleProof.deserialize(proof)
        verify_inclusion(data, root, proof_des)
        return {"success": True}
    except InvalidProof as invalid_e:
        return {"success": False, "exception": invalid_e}
    except InvalidChallenge as invalid_e:
        return {"success": False, "exception": invalid_e}
    except Exception as invalid_e:
        return {"success": False, "exception": invalid_e}


def verify_consistency_proof(first_root, second_root, proof):
    try:
        verify_consistency(first_root, second_root, proof)
        return {"success": True}
    except InvalidProof as invalid_e:
        return {"success": False, "exception": invalid_e}
    except InvalidChallenge as invalid_e:
        return {"success": False, "exception": invalid_e}
    except Exception as invalid_e:
        return {"success": False, "exception": invalid_e}


def verify_single_data(proof, global_root, data):
    # get local root value as string
    local_root_value = proof["local_tree"]["local_root"]["value"]

    # transform local root value in root to bytes, then everything to one big string
    local_root = proof["local_tree"]["local_root"]
    local_root['value'] = bytes(local_root['value'], "utf_8")
    local_root = str(local_root)

    # get global root and proof of local root in global tree
    global_root_in_proof = proof["global_root"]["value"]
    local_proof = proof["local_tree"]["inclusion_proof"]
    global_proof = proof["data"]["inclusion_proof"]

    # compare global_root from "proof" and from "trusted source", if different, return false
    if global_root_in_proof != global_root:
        return {"success": False, "exception": "Global Root in proof different from Global Root from trusted source"}

    # verify inclusion of data in local tree, get exception if error
    local_tree_inclusion_verification = verify_inclusion_proof(local_proof, local_root_value, data)
    inclusion_proof_local = local_tree_inclusion_verification["success"]
    exception_local = local_tree_inclusion_verification["exception"] if not inclusion_proof_local else None

    # verify inclusion of local tree root in global tree, get exception if error
    local_root = bytes(local_root, "utf_8")
    global_tree_inclusion_verification = verify_inclusion_proof(global_proof, global_root, local_root)
    inclusion_proof_global = global_tree_inclusion_verification["success"]
    exception_global = global_tree_inclusion_verification["exception"] if not inclusion_proof_global else None

    # return exceptions, if any, or success
    if not inclusion_proof_local:
        return {"success": False, "exception": exception_local}
    elif not inclusion_proof_global:
        return {"success": False, "exception": exception_global}
    else:
        return {"success": True}


def verify_local_tree_history_consistency(global_tree_data, consistency_proofs, trusted_global_root, tree_name):
    # rebuild global_tree from global tree leaves
    leaves_in_tree = []
    for leaf in global_tree_data['leaves']:
        leaf_value = leaf['value']  # 3-tuple with root value, tree name and size
        leaf['value']['value'] = bytes(leaf['value']['value'], "utf-8")     # transform only root hash to bytes
        leaf_bytes = str(leaf_value)    # transform the whole tuple to a single string
        leaves_in_tree.append(leaf_bytes)           # append to array
    tree_rebuilt = _build_tree(leaves_in_tree)          # make tree from array

    # compare calculated and trusted global_root
    tree_rebuilt_root = tree_rebuilt.root.decode("utf_8")   # get root from rebuilt tree
    if tree_rebuilt_root != trusted_global_root:            # compare calculated and trusted
        return {"success": False, "exception": "Global roots don't match"}  # if different return false, else continues

    # Compare found local-roots with those presents on consistency_proofs (divided in 3 parts)
    # 1. search on global_tree all roots corresponding to tree_name as dicts
    tree_roots = []
    for leaf in global_tree_data['leaves']:
        if leaf['value']['tree_name'] == tree_name:
            leaf['value']['value'] = leaf['value']['value'].decode()
            tree_roots.append(leaf['value'])

    # 2. get from consistency_proofs all root objects as dicts
    consistency_proof_roots = []
    for proof in consistency_proofs['proofs']:
        consistency_proof_roots.append(proof['root'])

    # 3. compare tree_roots to consistency_proof_roots
    for tree_root in tree_roots:
        found = False
        for consistency_proof_root in consistency_proof_roots:
            if tree_root['value'] == consistency_proof_root['value'] and tree_root['tree_name'] == consistency_proof_root['tree_name'] and tree_root['tree_size'] == consistency_proof_root['tree_size']:
                found = True
        if found is False:
            return {"success": False, "exception": "Global tree data and Consistency proofs do not match"}  # if comparison fails return false, else continues

    # Verify consistency proof
    consistency_proofs_list = consistency_proofs['proofs']  # list of proofs from json object
    for proofs in zip(consistency_proofs_list, consistency_proofs_list[1:]):    # iterate in pairs
        first_root = bytes(proofs[0]['root']['value'], "utf_8")
        second_root = bytes(proofs[1]['root']['value'], "utf_8")
        consistency_proof = proofs[1]['consistency_proof']
        consistency_proof = MerkleProof.deserialize(consistency_proof)
        verification = verify_consistency_proof(first_root, second_root, consistency_proof)  # consistency verification
        if verification["success"] is False:
            return {"success": False, "exception": "Consistency proof is false"}  # if verifification fails return false, else continues

    # if every verification passes return true
    return {"success": True}


def verify_global_tree_history_consistency(consistency_proofs, stored_global_roots=None):
    # If roots not None, create tree with roots as leaves
    if stored_global_roots is not None:
        proofs = consistency_proofs["proofs"]
        partial_roots = stored_global_roots["roots"]

        # check if partial roots are consistent with proofs
        comparison = _compare_consistency_proofs_to_partial_roots(proofs, partial_roots)
        if not comparison:
            return {"success": False, "exception": "Consistency proof is false"}  # if verification fails return false, else continue

    # Verify consistency of proofs
    consistency_proofs_verification = _verify_consistency_proofs(consistency_proofs['proofs'])
    return consistency_proofs_verification


def _build_tree(list_of_data):
    m_tree = MerkleTree()
    for data in list_of_data:
        m_tree.append_entry(data)
    return m_tree


def _verify_consistency_proofs(consistency_proofs_list):
    for proofs in zip(consistency_proofs_list, consistency_proofs_list[1:]):  # iterate in pairs (n and n+1)
        first_root = bytes(proofs[0]['root']['value'], "utf_8")
        second_root = bytes(proofs[1]['root']['value'], "utf_8")
        consistency_proof = proofs[1]['consistency_proof']
        consistency_proof = MerkleProof.deserialize(consistency_proof)
        verification = verify_consistency_proof(first_root, second_root, consistency_proof)  # consistency verification
        if verification["success"] is False:
            return {"success": False,
                    "exception": "Consistency proof is false"}  # if verification fails return false, else continues

    # if every verification passes return true
    return {"success": True}


def _compare_consistency_proofs_to_partial_roots(proofs, roots):
    # For each root, iterate all proofs
    for root in roots[1:]:
        is_partial_root_in_proofs = False   # assume they don't match
        for proof in proofs:    # for each proof, check if they match
            if root["value"] == proof["root"]["value"] and \
                    root["tree_size"] == proof["root"]["tree_size"] and \
                    root["signature"] == proof["root"]["signature"] and \
                    root["timestamp"] == proof["root"]["timestamp"]:    # if all properties match
                is_partial_root_in_proofs = True    # set True
                break   # and skip to the next root
        if not is_partial_root_in_proofs:   # if any root does not match any proof
            return False    # return false

    # if no root is false, return true
    return True
