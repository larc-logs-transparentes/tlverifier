=========================
Simple Verifications
=========================


Verifying single data
=========================

This function verifies the path, both on the local tree and on the global tree, and compares the obtained root
with the trusted global root.

.. This verification includes 1) the data is correctly registered in a local tree; 2) the root from the local tree is correctly
.. registered in a global tree; 3) the calculated global root is equal to a trusted global root.

.. code-block:: 
    
    How to use it:

    # import package tlverifier
    import tlverifier

    # using example data:
    proof = tlverifier.get_proof()    # proof of local tree
    global_root = tlverifier.get_trusted_global_root()    # proof of local tree
    data = tlverifier.get_data()    # the data to be verified

    # calling the function:
    result = verify_single_data(proof, global_root, data)


.. code-block::

    # Details on calling the function
        Parameters needed:
            proof as dict, looks like this:
            proof = {
                        "status": "value",
                        "global root": {...},
                        "local_tree": {...},
                        "data": {...}
                    }

            global_root as string:
            global_root = "a1b2c3d4e5f6g7"

            data as bytes:
            data = b"xyz"

.. code-block::

    # Return of function
        JSON with fields:
            "success" [Bool][obligatory]: True or False
            "exception" [String][optional]: Content of exception in case success is false



Verifying inclusion proof
=========================

Function checks if inclusion proof is valid and correct.

.. code-block::

    How to use it:

    # import package tlverifier
    import tlverifier

    proof = tlverifier.get_proof()["local_tree"]["inclusion_proof"]    # incusion proof extracted from whole proof object
    root = tlverifier.get_local_root()
    data = tlverifier.get_data()   # raw data in bytes

    # calling the function:
    result = tlverifier.verify_single_data(proof, global_root, data)


.. code-block::

    # Details on calling the function
        Parameters needed:
            proof as dict, looks like this:
            proof = {
                    "metadata": {
                        "timestamp": 1685744410,
                        "algorithm": "sha256",
                        "encoding": "utf_8",
                        "security": true
                    },
                    "offset": 0,
                    "path": [
                        [
                            1,
                            "82d40d859b2d12db128a15b27fc1312b4126e13153d6614b2a0755030a6b1ecb"
                        ],
                        [
                            1,
                            "c1b94b4bfd87e4a97f98da242185664700ec497f3cd520f3e0097d924409d570"
                        ],
                        [
                            1,
                            "7eebbe187a1760d9235ff0bdf89f5186bb6f53c3106be56375aa429d757e9292"
                        ],
                        [
                            -1,
                            "d2935bb8382e8cb379a6a776e686b54821f804febaf0979ac752c11e60dc89b0"
                        ]
                    ]
            }

            root as string:
            root = "a1b2c3d4e5f6g7"

            data as bytes:
            data = b'xyz'


.. code-block::

    # Return of function
        JSON with fields:
            "success" [Bool][obligatory]: True or False
            "exception" [String][optional]: Content of exception in case success is false



Verifying consistency proof
=========================

Function checks if inclusion proof is consistent with the roots.

.. code-block::

    How to use it:

    # import package tlverifier
    import tlverifier

    # using example data:
    middle_root_value, middle_proof, last_root_value = tlverifier.get_middle_last_roots_from_partial_global()

    # calling the function:
    result = verify_consistency_proof(middle_root_value, last_root_value, middle_proof)

.. code-block::

    # Details on calling the function
        Parameters needed:
            middle_root_value as bytes:
            middle_root_value = b'340e7be7a0775255aa9c6d8e59308b0e19aac2035a65bb9c4dd39535155d8068'

            middle_proof as MerkleProof:
            middle_proof = MerkleProof() object

            last_root_value as bytes:
            last_root_value = b'340e7be7a0775255aa9c6d8e59308b0e19aac2035a65bb9c4dd39535155d8068'

.. code-block::

    # Return of function
        JSON with fields:
            "success" [Bool][obligatory]: True or False
            "exception" [String][optional]: Content of exception in case success is false
