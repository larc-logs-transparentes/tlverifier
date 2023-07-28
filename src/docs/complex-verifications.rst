=========================
Complex Verifications
=========================


Verifying local tree history consistency
=========================

Function verifies if a LOCAL tree is consistent.

.. This verification includes 1) the data is correctly registered in a local tree; 2) the root from the local tree is correctly
.. registered in a global tree; 3) the calculated global root is equal to a trusted global root.

.. code-block:: 
    
    # 1. Rebuild global tree
    # 2. Compare calculated and trusted global roots
    # 3. Compare local roots with to roots in consistency proof
    # 4. Verify consistency proof
    #
    # proof = dict
    # global_root = string
    # data = bytes
    #
    # INSERIR EXEMPLO DE USO DA FUNCAO


Verifying global tree history consistency
=========================

Function verifies if a GLOBAL tree is consistent.

.. code-block::

    # 1. Rebuild global tree
    # 2. Verify if partial roots are consistent with proofs
    # 3. Verify consistency proofs
    #
    # consistency_proofs = dict
    # (optional) stored_global_roots = dict

This function casts proof to MerkleTreeProof object from dict, and verify if proof is valid and correct.
