Lmodule Examples
=================

Module Test Example
---------------------

You can use **Module** class to load arbitrary modules, in this example we
run few examples using the **Module** class to illustrate few of the features.

.. include:: ../examples/moduletest.py

Shown below is sample output

::

    $ python moduletest.py
    The following modules:  ['GCCcore', 'Python'] were loaded successfully


    Command Executed: module purge && module load GCCcore &&  module load Python
    Failed to load modules: ['GCCcore', 'invalid']
    Command Executed: module purge && module load GCCcore &&  module load invalid
    return code: 0
    module load GCCcore &&  module load Python
    module --force purge &&  module load GCCcore &&  module load Python
    [DEBUG] Executing module command: module purge && module load Anaconda3/5.3.0 &&  module load M4/1.4.17
    [DEBUG] Return Code: 0
    [DEBUG] Executing module command: module purge && module load Anaconda3/5.3.0 &&  module load M4/1.4.17
    [DEBUG] Return Code: 0

Automating Module Load Test for environmentmodules
----------------------------------------------------

If your system has environment-modules, you can make use of this script to
automate module load test using **Module** class.

.. include:: ../examples/environmentmodules_moduleloadtest.py

Collection Example
-------------------

.. include:: ../examples/collection.py

The next example shows how we can load a module and save into a collection.

.. include:: ../examples/saving_collection.py

Spider Example
---------------

This next example makes use of Spider class to get unique names, parent modules,
retrieve all version of GCC, and use Spider on directory tree to get all names and
test each module.

.. include:: ../examples/spider_example.py