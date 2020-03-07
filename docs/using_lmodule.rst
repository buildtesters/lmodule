Using Lmodule API
===================

The get started we will show how to use the ``Module`` class to interact with the Lmod module system. First
off we need to import the Module class using ``from lmod.module import Module``

In this simple example we can pass ``GCCcore/8.3.0`` as module name to the class. The class accepts string or
list. We can use the ``get_command()`` method to get the module command that would be run.

.. code-block:: python

    >>> from lmod.module import Module
    >>> a = Module("GCCcore/8.3.0")
    >>> a.get_command()
    'module purge && module load GCCcore/8.3.0  '

Similarly, we can pass a list of modules to the class

.. code-block:: python

    >>> b = Module(["GCCcore/8.3.0", "zlib"])
    >>> b.get_command()
    'module purge && module load GCCcore/8.3.0 &&  module load zlib  '

You can get the same behavior if you pass modules by a string separated by a space

.. code-block:: python

    >>> b = Module("GCCcore/8.3.0 zlib")
    >>> b.get_command()
    'module purge && module load GCCcore/8.3.0 &&  module load zlib  '


Testing Modules
----------------

You can use the ``test_modules()`` method to test if modules are loaded properly. The method will return an exit
code.

.. code-block:: python

    >>> b.test_modules()
    0

Saving Modules to User Collection
----------------------------------

Modules can be stored into a user collection using the ``save()`` method. If no arguments are passed in, it will
save your modules to the ``default`` collection. This is equivalent to running ``module save``


.. code-block:: python

    >>> b.save()
    Saving modules ['GCCcore/8.3.0', 'zlib'] to module collection name: default
    Saved current collection of modules to: "default"

Likewise you can specify a collection name by passing a name to the ``save()`` method.

.. code-block:: python

    >>> b.save("gcc_zlib")
    Saving modules ['GCCcore/8.3.0', 'zlib'] to module collection name: gcc_zlib
    Saved current collection of modules to: "gcc_zlib"

Show Modules associated to a  User Collection
----------------------------------------------

You can view the user collection using ``describe()`` method. If no argument is passed in, it will show
the ``default`` collection

.. code-block:: python

    >>> b.describe()
    Collection "default" contains:
       1) GCCcore/8.3.0    2) zlib

Similarly, you can pass a collection name to ``describe()`` method to view a particular collection.

.. code-block:: python

    >>> b.describe("gcc_zlib")
    Collection "gcc_zlib" contains:
       1) GCCcore/8.3.0    2) zlib

Get collection command
------------------------

The ``get_collection()`` method can fetch the command to restore the user collection. If no argument is passed in
it will resort to the ``default`` collection

.. code-block:: python

    >>> b.get_collection()
    'module restore default'

Likewise you can pass a collection name to ``get_collection`` method to fetch any collection name.

.. code-block:: python

    >>> b.get_collection("gcc_zlib")
    'module restore gcc_zlib'

Testing a User Collection
----------------------------------

We can also test if a user collection is working. This can be done using the ``test_collection`` method. The method
will return the exit code of the command which can be useful for testing output validity.

.. code-block:: python

    >>> b.test_collection()
    0
    >>> b.test_collection("xyz")
    1


Tweaking Module Purge Behavior
--------------------------------

By default, when you pass modules to ``Module`` class, it will purge the modules. You can tweak this behavior by passing
the ``purge=False`` option to ``Module``. By default purge is set to ``True``

.. code-block:: python

    >>> c = Module("OpenMPI/3.0.0", purge=False)
    >>> c.get_command()
    'module load OpenMPI/3.0.0  '

Enable Force Purge
-------------------

You can force purge modules by passing ``force=True``. This will purge sticky modules that may be setup in your site.

.. code-block:: python

    >>> c = Module("OpenMPI/3.0.0", force=True)
    >>> c.get_command()
    'module --force purge &&  module load OpenMPI/3.0.0  '

Note if you set ``purge=False`` and also pass ``force=True`` to the class, it will not purge any modules. Purge
takes precedence over force.

.. code-block:: python

    >>> c = Module("OpenMPI/3.0.0", purge=False, force=True)
    >>> c.get_command()
    'module load OpenMPI/3.0.0  '


Enabling Debug
---------------

To enable debug you can pass ``debug=True`` to the ``Module`` class. This works with most methods.

.. code-block:: python

    >>> a = Module("GCCcore/8.3.0",debug=True)
    >>> a.test_modules()
    [DEBUG] Executing module command: module purge && module load GCCcore/8.3.0
    [DEBUG] Return Code: 0
    0

Debug works on user collection methods as well

.. code-block:: python

    >>> a.describe()
    [DEBUG] Executing module command: module describe default
    [DEBUG] Return Code: 0
    Collection "default" contains:
       1) GCCcore/8.3.0    2) zlib

    >>> a.test_collection()
    [DEBUG] Executing command: module restore default
    [DEBUG] Return Code: 0
    0

    >>> a.save("GCC")
    [DEBUG] Executing module command: module purge && module load GCCcore/8.3.0   && module save GCC
    [DEBUG] Return Code: 0
    Saving modules ['GCCcore/8.3.0'] to module collection name: GCC
    Saved current collection of modules to: "GCC"

The Module class will throw a ``TypeError`` if it detects modules are not of type ``str`` or ``list``

.. code-block:: python

    >>> a=Module(1)
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      File "/mxg-hpc/users/ssi29/lmodule/lmod/module.py", line 44, in __init__
        f"Expecting of type 'list' or 'string' for argument modules. Got of type {type(modules)}"
    TypeError: Expecting of type 'list' or 'string' for argument modules. Got of type <class 'int'>


Is Module Available?
-----------------------

The ``module is-avail`` command can check if a module file is available in your system. The command will return an
exit code either ``0`` or ``1``. This could be useful in finding module in system before loading them in your script.
To demonstrate, we will use the ``is_avail()`` method to check for module files.

.. code-block:: python

    >>> a = Module()
    >>> a.is_avail("GCC")
    0

    >>> a.is_avail("cuda")
    1

Similarly ``module avail`` command is mapped to the method ``avail()``. To check if ``lmod`` is available (i.e ``module avail lmod``)
you can do the following

.. code-block:: python

    >>> a = Module()
    >>> a.avail("lmod")
    ['/usr/share/lmod/lmod/modulefiles/Core:', 'lmod']

If you want to get a listing of all modules (i.e ``module avail``), then don't pass any argument to ``avail()`` method.

.. code-block:: python

    >>> a = Module()
    >>> a.avail()
    module -t avail
    ['/usr/share/lmod/lmod/modulefiles/Core:', 'lmod', 'settarg']

Get Lmod Version
------------------

You can get the Lmod version by using the ``version()`` method.

.. code-block:: python

    >>> a = Module()
    >>> a.version()
    '7.8.16'

