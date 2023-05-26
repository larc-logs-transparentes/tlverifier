from pymerkle_logsTransparentes import MerkleProof, verify_inclusion, verify_consistency
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
    # derive all data from whole proof
    local_root = proof["local_tree"]["local_root"]["value"]
    global_root_in_proof = proof["global_root"]["value"]
    local_proof = proof["local_tree"]["inclusion_proof"]
    global_proof = proof["data"]["inclusion_proof"]

    # compare global_root from "proof" and from "trusted source", if different, return false
    if global_root_in_proof != global_root:
        return {"success": False, "exception": "Global Root in proof different from Global Root from trusted source"}

    # verify inclusion of data in local tree, get exception if error
    local_tree_inclusion_verification = verify_inclusion_proof(local_proof, local_root, data)
    inclusion_proof_local = local_tree_inclusion_verification["success"]
    exception_local = local_tree_inclusion_verification["exception"] if not inclusion_proof_local else None

    # verify inlusion of local tree root in global tree, get exception if error
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
