.. tlverifier documentation master file, created by
   sphinx-quickstart on Tue May 23 17:01:58 2023.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

"""""""""""""""""
tlverifier
"""""""""""""""""
|Python >= 3.6|

.. |Python >= 3.6| image:: https://img.shields.io/badge/python-%3E%3D%203.6-blue.svg


...........................
Transparenty Logs Verifier
...........................


TLverifier is a tool that verifies the integrity of the logs from the TL-Election. 
Works with `TLmanager`_.

.. _TLmanager: https://github.com/larc-logs-transparentes/logs-transparentes/tree/main/tlmanager


=================
Installation
=================


.. code-block:: bash

   pip install tlverifier

=================
Usage 
=================
.. code-block:: python

   from tlverifier import tlverifier

   # obs: using dummy functions
   proof = tlverifier.get_proof()                       # get proof from the tlmanager
   global_root = tlverifier.get_trusted_global_root()   # get trustable root (e.g., from a monitor)
   data = tlverifier.get_data()                         # get data to verify (e.g., BU)


   result = verify_data_entry(proof, global_root, data)


.. toctree::
   :maxdepth: 0
   :hidden:

   Inclusion checks <inclusion-checks>
   Consistency checks <consistency-checks>
   References <modules>




Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
