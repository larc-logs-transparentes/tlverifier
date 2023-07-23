=========================
Simple Verifications
=========================


Verifying single data
=========================

The most common use case is to verify that a given data is correctly registered on the transparent log.

.. This verification includes 1) the data is correctly registered in a local tree; 2) the root from the local tree is correctly
.. registered in a global tree; 3) the calculated global root is equal to a trusted global root.

.. code-block:: 
    
    # setup the tlmanager, building the tree

    # get the proof object (specify that usually you get the proof from a public endpoint)
    # get the global root from a trusted source (alternatively, you send the root to a trusted auditor)
    # get the data to be verified
    # verify the proof

This function verifies the path, both on the local tree and on the global tree, and compares the obtained root 
with the trusted global root.


Verifying inclusion proof
=========================

Function checks if inclusion proof is valid and correct.

.. code-block::

    # 1. Deserialize proof
    # 2. Verify inclusion checking data, root and proof
    #
    # proof = dict
    # root = string
    # data = bytes

This function casts proof to MerkleTreeProof object from dict, and verify if proof is valid and correct.


Verifying consistency proof
=========================

Function checks if inclusion proof is consistent with the roots.

.. code-block::

    # Verify consistency on Tree
    #
    # first_root = bytes
    # second_root = bytes
    # proof = MerkleProof

Direct verification in tree.