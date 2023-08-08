=========================
Consistency checks
=========================
These functions check the consistency (i.e., append-only) of TL-Election. 
There are two functions: one related to local trees, and one related to global tree.



Verifying local tree history consistency
=========================================

Function verifies if a LOCAL tree is consistent. It makes the following

1. Verify if the received "global tree leafs" match with the trusted global root
2. Search in the "global tree leafs" all the local roots 
3. For each local root, verify its consistency with the previous root


How to use it:
-------------------------

First, get all global tree leafs. You can get it from TLmanager.

.. code-block::

    all_leaf_global = tlverifier.get_all_leaf_global_tree()



Then, get all consistency proofs, saved on TLmanager

.. code-block::

    all_consistency = tlverifier.get_all_consistency_proof()



Then, get a trusted global root. You usually get it from a monitor. 
You can also periodically retrive the global root from TL-Election.

.. code-block::

    global_root = tlverifier.get_trusted_global_root()
    # global_root == "a1b2c3d4e5f6g7"


Finally, call the verification function

.. code-block::

    tree_name = "tree1"
    result = tlverifier.verify_local_tree_history_consistency(all_leaf_global, all_consistency, global_root, tree_name)


Verifying global tree history consistency
===========================================

Function verifies if a GLOBAL tree is consistent. It makes the following:

1. Verify if the consistency proofs match with the stored global roots
2. Verify each consistency proof

How to use it:
-------------------------

First, get the stored_global_roots. Usually, periodically monitors retrieves the latest global root on TL-Election. 
It is not necessary to have *every* published global root.

.. code-block::

    stored_global_roots = tlverifier.get_partial_global_roots()


Then, get the consistency_proofs. Those proofs are provided by the TLmanager

.. code-block::

    consistency_proofs = tlverifier.get_all_consistency_proof_global()



Finally, call the verification function.

.. code-block::

    result = verify_global_tree_history_consistency(consistency_proofs, stored_global_roots)
