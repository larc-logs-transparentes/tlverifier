# tlverifier

### documentation
https://tlverifier.readthedocs.io/en/latest/

#### installation: 
pip install --extra-index-url https://test.pypi.org/simple/ tlverifier

#### installation of specific version:
pip install --extra-index-url https://test.pypi.org/simple/ tlverifier==x.y.z

#
#

## Environment:
#### dev: python==3.9
#### required: python>=3.7
#### libs required: pymerkle-logsTransparentes~=0.0.3 [https://pypi.org/project/pymerkle-logsTransparentes/]

#
#

### Functions:
- verify_inclusion_proof
- verify_consistency_proof
- verify_data_entry
- verify_local_tree_history_consistency
- verify_global_tree_history_consistency

#

### Functions details:

###### verify_inclusion_proof(proof, root, data, expected_index=None)
- proof: dictionary
- root: string
- data: bytes
- return: dictionary
  - {"success": True}
  - {"success": False, "exception": InvalidProof}
  - {"success": False, "exception": InvalidChallenge} 
  - {"success": False, "exception": Other}

###### verify_consistency_proof(first_root, second_root, proof)
- first_root: bytes
- second_root: bytes
- proof: MerkleProof (pymerkle_logsTransparentes.proof.MerkleProof)
- return: dictionary
  - {"success": True}
  - {"success": False, "exception": InvalidProof}
  - {"success": False, "exception": InvalidChallenge} 
  - {"success": False, "exception": Other}

###### verify_data_entry(proof, global_root, data)
- proof: dictionary
- global_root: string
- data: bytes
- return: dictionary
  - {"success": True}
  - {"success": False, "exception": inclusion_proof_local}
  - {"success": False, "exception": inclusion_proof_global}

###### verify_local_tree_history_consistency(global_tree_data, consistency_proofs, trusted_global_root, tree_name)
- global_tree_data: dictionary
- consistency_proofs: dictionary
- trusted_global_root: string
- tree_name: string
- return: dictionary
  - {"success": True}
  - {"success": False, "exception": "Global roots don't match"}
  - {"success": False, "exception": "Global tree data and Consistency proofs do not match"}
  - {"success": False, "exception": "Consistency proof is false"}

###### verify_global_tree_history_consistency(consistency_proofs, stored_global_roots=None)
- consistency_proofs: dictionary
- trusted_global_root: dictionary
- return: dictionary
  - {"success": True}
  - {"success": False, "exception": "Consistency proof is false"}

#
#

### Testing with testers.py and data_access.py
#### - testers.py 
##### has 5 functions, each one gets data from "data_access.py" and calls only one function of tl_functions
#### - data_access.py
##### gets mocked data, you can change data here to create to test for failure, or to add your own mocked data
