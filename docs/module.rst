Module Class
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

By default tests are run in a sub-shell if you are interested in running test in a login shell see :ref:`Login Shell Test`

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

.. _Login Shell Test:

Testing Modules in Login Shell
-------------------------------

If you would like to test your module in a login shell you can pass ``login=True`` to ``test_modules`` method. The
test will be conducted using bash

The format of the test will be as follows::

    bash -l -c "<command>"

Shown below is GCCcore/8.3.0 tested using a login shell. You may get different results if MODULEPATH is different in your
current shell as pose to when you login.

.. code-block:: python

    >>> a = Module("GCCcore/8.3.0",debug=True)
    >>> a.test_modules(login=True)
    [DEBUG] Executing module command: bash -l -c "module purge && module load GCCcore/8.3.0  "
    [DEBUG] Return Code: 0
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


Module Spider
---------------

The ``module spider`` command can be used to provide extra details for available modules along with details about specific
versions and module description. The ``spider`` method can be used to mimic this behavior. Running ``module spider`` without
any arguments will return all available modules in MODULEPATH.

The following snippet below will mimic ``module spider`` command and the output is a string type which we can print.

.. code-block:: python

    >>> m = Module()
    >>> out = m.spider()
    >>> print(out)

    ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    The following is a list of the modules and extensions currently available:
    ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
      lmod: lmod
        Lmod: An Environment Module System

      settarg: settarg

    ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    To learn more about a package execute:

       $ module spider Foo

    where "Foo" is the name of a module.

    To find detailed information about a particular package you
    must specify the version if there is more than one version:

       $ module spider Foo/11.1

    ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


If we specify modules during instance creation time, those modules will be used when invoking ``spider`` class.
In this next example we mimic ``module spider lmod`` command.

.. code-block:: python

    >>> m = Module("lmod")
    >>> out = m.spider()
    >>> print(out)

    ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
      lmod: lmod
    ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        Description:
          Lmod: An Environment Module System


        This module can be loaded directly: module load lmod

You may specify modules through ``spider`` method which can be a string or list type. If you want to
specify multiple modules you can do one of the following

.. code-block:: python

   >>> m = Module()
   >>> out = m.spider("gcc python")

.. code-block:: python

   >>> m = Module()
   >>> out = m.spider([gcc, python])

If you specify a list, each item will be converted to string before invoking ``module spider`` command. If you specify
modules during instance creation but specify modules in ``spider`` method then we will use modules specified by spider output
as we can see below.

.. code-block:: python

    >>> m = Module("xyz")
    >>> m.spider()
    >>> print(m.spider())
    Lmod has detected the following error: Unable to find: "xyz".

    >>> print(m.spider("lmod"))

    ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
      lmod: lmod
    ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        Description:
          Lmod: An Environment Module System


        This module can be loaded directly: module load lmod

Get Lmod Version
------------------

You can get the Lmod version by using the ``version()`` method.

.. code-block:: python

    >>> a = Module()
    >>> a.version()
    '7.8.16'

Retrieve User Collections
--------------------------

Lmod user collection are typically found in **$HOME/.lmod.d** and you can get all collections by running ``module -t savelist``.

Similarly, we have a method ``get_user_collections`` that can return a **list** of user collections as shown below

.. code-block:: python

    >>> from lmod.module import get_user_collections
    >>> get_user_collections()
    ['GCC', 'Python', 'default', 'gcc_zlib', 'settarg', 'zlib']

This could be used in conjunction with ``Module`` class with options like ``get_collection``, ``test_collection``, ``describe``
to perform operation on the user collections.

Shown below is an example of showing all user collections in a simple for-loop using the ``describe`` method from Module class

.. code-block:: python

    >>> for collection in get_user_collections():
    ...     Module().describe(collection)
    ...
    Collection "GCC" contains:
       1) GCCcore/8.3.0

    Collection "Python" contains:
       1) GCCcore/8.3.0                    7)  SQLite/3.29.0-GCCcore-8.3.0
       2) bzip2/1.0.8-GCCcore-8.3.0        8)  XZ/5.2.4-GCCcore-8.3.0
       3) zlib/1.2.11-GCCcore-8.3.0        9)  GMP/6.1.2-GCCcore-8.3.0
       4) ncurses/6.1-GCCcore-8.3.0        10) libffi/3.2.1-GCCcore-8.3.0
       5) libreadline/8.0-GCCcore-8.3.0    11) Python
       6) Tcl/8.6.9-GCCcore-8.3.0

    Collection "default" contains:
       1) settarg

    Collection "gcc_zlib" contains:
       1) GCCcore/8.3.0    2) zlib

    Collection "settarg" contains:
       1) settarg

    Collection "zlib" contains:
       1) zlib


Likewise, we can easily test all user collection using ``test_collection`` which gives opportunity to ensure all your
user collection are valid before using them in your script

.. code-block:: python

    >>> for collection in get_user_collections():
    ...     Module(debug=True).test_collection(collection)
    ...
    [DEBUG] Executing command: module restore GCC
    [DEBUG] Return Code: 0
    0
    [DEBUG] Executing command: module restore Python
    [DEBUG] Return Code: 0
    0
    [DEBUG] Executing command: module restore default
    [DEBUG] Return Code: 0
    0
    [DEBUG] Executing command: module restore gcc_zlib
    [DEBUG] Return Code: 0
    0
    [DEBUG] Executing command: module restore settarg
    [DEBUG] Return Code: 0
    0
    [DEBUG] Executing command: module restore zlib
    [DEBUG] Return Code: 0
    0
