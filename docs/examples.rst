Lmodule Examples
=================

Module Test Example
---------------------

You can use **Module** class to load arbitrary modules, in this example we
run few examples using the **Module** class to illustrate few of the features.

.. program-output:: cat ../examples/moduletest.py

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

.. program-output:: cat ../examples/environmentmodules_moduleloadtest.py

Collection Example
-------------------

This example, get's all module collections and print their name and tests collection 
command. Next, we test **Python** collection in debug mode followed by Default collection.
Finally, we wrap up by testing an invalid module collection which should raise error. 

.. program-output:: cat ../examples/collection.py

This next example will load **zlib** module, save into module collection named **zlib** and 
show content of collection of newly created collection **zlib**.

.. program-output:: cat ../examples/saving_collection.py

Spider Example
---------------

This next example makes use of Spider class to get unique names, parent modules,
retrieve all version of GCC, and use Spider on directory tree to get all names and
test each module.

.. program-output:: cat ../examples/spider_example.py
