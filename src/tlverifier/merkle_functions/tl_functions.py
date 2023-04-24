from pymerkle import MerkleProof, verify_inclusion, verify_consistency
from pymerkle.tree import InvalidChallenge
from pymerkle.proof import InvalidProof


def verify_inclusion_proof(proof, root, data, expected_index=None):
    # expected index:
    # index of data must be in the expected index
    # to get actual index use the int values of path
    try:
        proof_des = MerkleProof.deserialize(proof)
        verify_inclusion(data, root, proof_des)
        return True, None
    except InvalidProof as invalid_e:
        return False, invalid_e
    except InvalidChallenge as invalid_e:
        return False, invalid_e
    except Exception as invalid_e:
        return False, invalid_e


def verify_consistency_proof(first_root, second_root, proof):
    try:
        verify_consistency(first_root, second_root, proof)
        return True, None
    except InvalidProof as invalid_e:
        return False, invalid_e
    except InvalidChallenge as invalid_e:
        return False, invalid_e
    except Exception as invalid_e:
        return False, invalid_e


def verify_single_data(proof, proof_global, local_root, global_root, data):
    # if proof['global_root']['value'] != global_root:
    #     return False

    inclusion_proof_local, exception_local = verify_inclusion_proof(proof, local_root, data)
    inclusion_proof_global, exception_global = verify_inclusion_proof(proof_global, global_root, local_root)

    if not inclusion_proof_local:
        return False, exception_local
    elif not inclusion_proof_global:
        return False, exception_global
    else:
        return True, None
