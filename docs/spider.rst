Working with Lmod Spider
=========================

lmodule provides an API to retrieve results from spider command. To get started you need to import the ``Spider`` class
as follows

.. code-block:: python

    >>> from lmod.spider import Spider

To create a Spider object you can do the following

.. code-block:: python

    >>> a = Spider()

Getting Unique Software
------------------------

If you want to get a list of unique software names, you can use the ``get_names()`` method.

.. code-block:: python

    >>> a = Spider()
    >>> a.get_names()
    ['Anaconda3', 'Autoconf', 'Automake', 'Autotools', 'Bison', 'CMake', 'CUDA', 'Clang', 'EasyBuild', 'FFTW', 'GCC', 'GCCcore', 'GMP', 'M4', 'OSU-Micro-Benchmarks', 'OpenBLAS', 'OpenMPI', 'PyCharm', 'Python', 'SQLite', 'ScaLAPACK', 'Tcl', 'XZ', 'binutils', 'bzip2', 'diffutils', 'flex', 'foss', 'gdbm', 'gettext', 'gompi', 'help2man', 'hwloc', 'libffi', 'libiconv', 'libpciaccess', 'libreadline', 'libsigsegv', 'libtool', 'libxml2', 'lmod', 'm4', 'ncurses', 'numactl', 'pkgconf', 'readline', 'settarg', 'tar', 'util-macros', 'xorg-macros', 'xz', 'zlib']


This would be all unique software based on value of ``MODULEPATH``. We can also tweak which module trees to search
with spider as follows.

.. code-block:: python

    >>> b = Spider("/usr/share/lmod/lmod/modulefiles/Core")
    >>> b.get_unique_software()
    ['lmod', 'settarg']

Get Module Trees
------------------

You can get all module trees used by spider command using the method ``get_trees()``.

.. code-block:: python

    >>> a.get_trees()
    '/usr/share/lmod/lmod/modulefiles/Core'


Retrieve all Module Names
--------------------------
We can retrieve a list of full canonical module names by using ``get_modules()`` method.

.. code-block:: python

    >>> c = Spider("/mxg-hpc/users/ssi29/spack/modules/linux-rhel7-x86_64/Core")
    >>> c.get_modules()
    ['bzip2/1.0.8-etzfbao', 'diffutils/3.7-jthvt3v', 'gdbm/1.18.1-r4vohzu', 'gettext/0.20.1-c4ovdd2', 'libiconv/1.16-xcmzb6a', 'libpciaccess/0.13.5-cavw42z', 'libsigsegv/2.12-oywfhvk', 'libtool/2.4.6-swiq7rt', 'libxml2/2.9.9-azmlgc5', 'm4/1.4.18-dipchcn', 'ncurses/6.1-3jjw2re', 'pkgconf/1.6.3-oqak6dh', 'readline/8.0-bp7xnfp', 'tar/1.32-gem5z6s', 'util-macros/1.19.1-s4xjvop', 'xz/5.2.4-lvajsnj', 'zlib/1.2.11-zolwez4']


Retrieve all Parent Modules
----------------------------
We can retrieve parent modules (modules that set MODULEPATH) to other trees by using method ``get_parents``. This
is useful for finding modules in Hierarchical Module Naming Scheme.

.. code-block:: python

    >>> e = Spider()
    >>> e.get_parents()
    ['GCCcore/8.1.0', 'GCCcore/9.2.0']

In this case we know that loading ``GCCcore/8.1.0`` will set MODULEPATH to another module tree. Notice in command below
we see ``prepend_path("MODULEPATH",...`` is set to indicate another tree is added to ``MODULEPATH``. This helps users
and site-administrator to find all sub-trees in your software stack.

.. code-block:: shell

    $ module --redirect show GCCcore/8.1.0 | grep MODULEPATH
    prepend_path("MODULEPATH","/mxg-hpc/users/ssi29/easybuild-HMNS/modules/all/Compiler/GCCcore/8.1.0")

Getting all versions of a particular software
----------------------------------------------

We can retrieve a list of all versions of a particular software using the ``get_all_version`` method which takes an argument
for the software name. Shown below we can query all versions of the ``GCC`` module.

.. code-block:: python

    >>> e.get_all_versions("GCC")
    ['6.4.0-2.28', '7.1.0-2.28', '9.2.0-2.32', '8.1.0-2.30', '8.1.0-2.30', '8.3.0', '7.4.0-2.31.1']
