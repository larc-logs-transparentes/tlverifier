=========================
Inclusion checks
=========================

TL-Elections provides efficient methods to verify the inclusion and the integrity of a data entry.

Verify data entry
=========================

Verifies if a data entry is correctly registered in TL-Election. It verifies 

1. if the data entry hash is equal to leaf hash;
2. if the leaf is included in local tree; 
3. if the local root is included in global tree;
4. if the global root is equal to "trusted global root"; 


Usage:
-------------------------

First, get the data entry proof. You can request it to the TL-Election by passing the object id 
(e.g., /get-bu-proof?bu_id=123).

.. code-block:: python

    # obs: using dummy functions
    proof = tlverifier.get_dummie_proof()



Then, get a trusted global root. You usually get it from a monitor, which periodically retrive it from TL-Election.

.. code-block:: python

    global_root = tlverifier.get_dummie_trusted_global_root()
    # global_root == "a1b2c3d4e5f6g7"


Next, get the data entry you want to verify

.. code-block:: python

    data = tlverifier.get_dummie_data()
    # data == b"xyz"           
   

Finally, call the verification function.

.. code-block:: python

    result = verify_data_entry(proof, global_root, data)

    # Return of function
        JSON with fields:
            "success" [Bool][required]: True or False
            "exception" [String][optional]: Content of exception in case success is false

