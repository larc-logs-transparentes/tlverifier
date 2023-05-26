
==========================================
Verify all election
==========================================

To completely audit the election results and the underline Transparent Log structure, you need to make the following verifications:

:list: Verify that the global tree is append-only (consistency)
:list: Verify that the local tree is append-only 
:list: Verify and sum all BUs 



Verify that the global tree is append-only
============================================

To make this verification, you need to have a trusted list of global roots.
This list is periodically published by the Election Authority, and stored by Monitors.
You can get this list from a trusted Monitor, or directly from the Election Authority.

.. code-block:: 

    # get the trusted list of global roots


Then, you get from the Election Authority, the consistency proofs between each published global roots. 
Those proofs are an evidence that no information were removed between two consecutive global roots.

.. code-block:: 

    # get the consistency proofs between each published global roots

Finally, you call tlverifier to verify the consistency proofs.


.. code-block:: 

    # verify all consistency proofs


Verify that the local tree is append-only
============================================

Verifying the global tree is not enought: you need also verify the local trees consistency.
To do so, you need to search all local roots stored on the global tree, and then verify the consistency 
between each of them.

.. code-block:: 

    # get all local roots from the global tree

    # get from the Election Authority all consistency proofs between each local roots (for a given tree)

    # verify all consistency proofs




Verify the sum of all BUs
============================================
