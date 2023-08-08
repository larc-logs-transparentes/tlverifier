=========================
Complex Verifications
=========================


Verifying local tree history consistency
=========================

Function verifies if a LOCAL tree is consistent.

.. This verification includes 1) the data is correctly registered in a local tree; 2) the root from the local tree is correctly
.. registered in a global tree; 3) the calculated global root is equal to a trusted global root.

.. code-block::

    How to use it:

    # import package tlverifier
    import tlverifier

    # using example data:
    all_leaf_global = tlverifier.get_all_leaf_global_tree()
    all_consistency = tlverifier.get_all_consistency_proof()
    global_root = tlverifier.get_trusted_global_root()
    tree_name = "tree1"

    # calling the function:
    result = tlverifier.verify_local_tree_history_consistency(all_leaf_global, all_consistency, global_root, tree_name)

.. code-block::

    # Details on calling the function
        Parameters needed:
            all_leaf_global as dict, looks like this:
            all_leaf_global = {
                  'status': 'ok',
                  'leaves': [
                    {
                      'index': 0,
                      'value': {
                        'value': '1a2b3c...',
                        'tree_name': 'tree1',
                        'tree_size': 2
                      }
                    },
                    {
                      'index': 1,
                      'value': {
                        'value': '1a2b3c...',
                        'tree_name': 'tree1',
                        'tree_size': 4
                      }
                    },
                    {...},
                    {...},
                  ]
                }

            all_consistency as dict, looks like this:
            all_consistency = {
                  'status': 'ok',
                  'proofs': [
                    {
                      'root': {
                        'value': '1a2b3c...',
                        'tree_name': 'tree1',
                        'tree_size': 2
                      },
                      'consistency_proof': None
                    },
                    {
                      'root': {
                        'value': '1a2b3c...',
                        'tree_name': 'tree1',
                        'tree_size': 4
                      },
                      'consistency_proof': {
                        'metadata': {
                          'timestamp': 1685743764,
                          'algorithm': 'sha256',
                          'encoding': 'utf_8',
                          'security': True
                        },
                        'offset': 0,
                        'path': [
                          [
                            1,
                            '1a2b3c...'
                          ],
                          [
                            1,
                            '1a2b3c...'
                          ]
                        ]
                      }
                    },
                    {
                      'root': {...},
                      'consistency_proof': {
                        'metadata': {...},
                        'offset': 0,
                        'path': [...]
                      }
                    },
                    {...}
                  ]
                }


            global_root as string:
            data = '1a2b3c...'

            tree_name as string:
            tree_name = 'tree1'

Verifying global tree history consistency
=========================

Function verifies if a GLOBAL tree is consistent.

.. code-block::

   How to use it:

    # import package tlverifier
    import tlverifier

    # using example data:
    consistency_proofs = tlverifier.get_all_consistency_proof_global()
    consistency_proofs_stored = tlverifier.get_partial_global_roots()

    # calling the function:
    result = verify_global_tree_history_consistency(consistency_proofs, consistency_proofs_stored)

.. code-block::

    # Details on calling the function
        Parameters needed:
            consistency_proofs as dict, looks like this:
            consistency_proofs = {
                  'status': 'ok',
                  'proofs': [
                    {
                      'root': {
                        'value': '1a2b3c...',
                        'tree_name': 'global_tree',
                        'tree_size': 1,
                        'signature': 'a1b2c3...',
                        'timestamp': '2023-06-20T12:20:12.573073'
                      },
                      'consistency_proof': None
                    },
                    {
                      'root': {
                        'value': '1a2b3c...',
                        'tree_name': 'global_tree',
                        'tree_size': 2,
                        'signature': 'a1b2c3...',
                        'timestamp': '2023-06-20T12:20:15.757602'
                      },
                      'consistency_proof': {
                        'metadata': {
                          'timestamp': 1687274415,
                          'algorithm': 'sha256',
                          'encoding': 'utf_8',
                          'security': True
                        },
                        'offset': 0,
                        'path': [
                          [
                            1,
                            'a1b2c3...'
                          ],
                          [
                            1,
                            'a1b2c3...'
                          ]
                        ]
                      }
                    },
                    {
                      'root': {...},
                      'consistency_proof': {
                        'metadata': {...},
                        'offset': 0,
                        'path': [...]
                      }
                    },
                    {...},
                    {...},
                  ]
                }

            consistency_proofs_stored as dict, looks like this:
            consistency_proofs_stored = {
                  'roots': [
                    {
                      'status': 'ok',
                      'value': None
                    },
                    {
                      'status': 'ok',
                      'value': '1a1b1c...',
                      'tree_name': 'global_tree',
                      'tree_size': 1,
                      'signature': '1a1b1c...',
                      'timestamp': '2023-06-20T12:20:12.573073'
                    },
                    {
                      'status': 'ok',
                      'value': '1a1b1c...',
                      'tree_name': 'global_tree',
                      'tree_size': 2,
                      'signature': '1a1b1c...',
                      'timestamp': '2023-06-20T12:20:15.757602'
                    },
                    {...},
                    {...},
                  ]
                }

.. code-block::

    # Return of function
        JSON with fields:
            "success" [Bool][obligatory]: True or False
            "exception" [String][optional]: Content of exception in case success is false


