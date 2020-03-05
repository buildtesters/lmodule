Automating Module Load Test
============================

lmodule provides a class ``ModuleLoadTest`` to automate module load test for all modules in a module tree. To get
started you will need to import the following

.. code-block:: python

    >>> from lmod.moduleloadtest import ModuleLoadTest

To test all modules set by MODULEPATH you can run the invoke ``ModuleLoadTest()`` without any arguments

.. code-block:: python

    >>> a = ModuleLoadTest()
    Testing the Following Module Trees: /mxg-hpc/users/ssi29/easybuild-HMNS/modules/all/Core:/mxg-hpc/users/ssi29/spack/modules/linux-rhel7-x86_64/Core:/mxg-hpc/users/ssi29/easybuild/modules/all:/etc/modulefiles:/usr/share/modulefiles:/usr/share/modulefiles/Linux:/usr/share/modulefiles/Core:/usr/share/lmod/lmod/modulefiles/Core
    ________________________________________________________________________________
    PASSED -  Module Name: Anaconda3/5.3.0
    PASSED -  Module Name: Autoconf/2.69-GCCcore-6.4.0
    PASSED -  Module Name: Autoconf/2.69-GCCcore-8.3.0
    PASSED -  Module Name: Automake/1.15.1-GCCcore-6.4.0
    PASSED -  Module Name: Automake/1.16.1-GCCcore-8.3.0
    PASSED -  Module Name: Autotools/20170619-GCCcore-6.4.0
    PASSED -  Module Name: Autotools/20180311-GCCcore-8.3.0

Tweak Number of Tests
-----------------------
We can control how many tests to run by passing ``count`` argument. Shown below we run 3 test and stop.

.. code-block:: python

    >>> b = ModuleLoadTest(count=3)
    Testing the Following Module Trees: /mxg-hpc/users/ssi29/easybuild-HMNS/modules/all/Core:/mxg-hpc/users/ssi29/spack/modules/linux-rhel7-x86_64/Core:/mxg-hpc/users/ssi29/easybuild/modules/all:/etc/modulefiles:/usr/share/modulefiles:/usr/share/modulefiles/Linux:/usr/share/modulefiles/Core:/usr/share/lmod/lmod/modulefiles/Core
    ________________________________________________________________________________
    PASSED -  Module Name: Anaconda3/5.3.0
    PASSED -  Module Name: Autoconf/2.69-GCCcore-6.4.0
    PASSED -  Module Name: Autoconf/2.69-GCCcore-8.3.0

We can configure which module trees to test by specifying the ``tree`` argument and enable debug mode by passing ``debug=True``.

.. code-block:: python

    >>> c = ModuleLoadTest("/usr/share/lmod/lmod/modulefiles/Core", debug=True)
    Testing the Following Module Trees: /usr/share/lmod/lmod/modulefiles/Core
    ________________________________________________________________________________
    [DEBUG] Executing module command: module purge && module load lmod
    [DEBUG] Return Code: 0
    PASSED -  Module Name: lmod
    [DEBUG] Executing module command: module purge && module load settarg
    [DEBUG] Return Code: 0
    PASSED -  Module Name: settarg

If you would like to specify  more than one tree you can specify them separating by a colon ``:`` character.

Tweaking module purge behavior when testing
---------------------------------------------

You will notice that ``module purge`` is run before loading each module. By default, ``module purge`` is enabled by
but this can be disabled by passing ``purge=False``.

.. code-block:: python

    >>> d = ModuleLoadTest("/usr/share/lmod/lmod/modulefiles/Core", purge=False, debug=True)
    Testing the Following Module Trees: /usr/share/lmod/lmod/modulefiles/Core
    ________________________________________________________________________________
    [DEBUG] Executing module command: module load lmod
    [DEBUG] Return Code: 0
    PASSED -  Module Name: lmod
    [DEBUG] Executing module command: module load settarg
    [DEBUG] Return Code: 0
    PASSED -  Module Name: settarg

If you want to force purge modules, then pass in the ``force=True``. You may get unexpected result depending on your site
configuration.

.. code-block:: python

    >>> e = ModuleLoadTest("/usr/share/lmod/lmod/modulefiles/Core", force=True, debug=True)
    Testing the Following Module Trees: /usr/share/lmod/lmod/modulefiles/Core
    ________________________________________________________________________________
    [DEBUG] Executing module command: module --force purge &&  module load lmod
    [DEBUG] Return Code: 0
    PASSED -  Module Name: lmod
    [DEBUG] Executing module command: module --force purge &&  module load settarg
    [DEBUG] Return Code: 0
    PASSED -  Module Name: settarg



Filtering Modules
------------------

Next we will show how we can filter modules while testing. Currently, we can filter modules by software name, and include
and exclude modules by full canonical module name. This can be useful for site-administrators to tweak how behavior
of ``ModuleLoadTest`` to their liking.

For example, some sites may have some modules like ``VASP``, ``Matlab``, ``Gaussian`` that can only be loaded
by a specific unix group because site-administrator want to restrict this software to be loaded by anyone and end
up running the software which may take up a license seat.

To filter by module names you can pass ``name`` option which is a list of software names to test.

.. code-block:: python

    >>> g = ModuleLoadTest("/mxg-hpc/users/ssi29/easybuild/modules/all",name=["Automake","Bison"])
    Testing the Following Module Trees: /mxg-hpc/users/ssi29/easybuild/modules/all
    ________________________________________________________________________________
    PASSED -  Module Name: Automake/1.15.1-GCCcore-6.4.0
    PASSED -  Module Name: Automake/1.16.1-GCCcore-8.3.0
    PASSED -  Module Name: Bison/3.0.4
    PASSED -  Module Name: Bison/3.0.4-GCCcore-6.4.0
    PASSED -  Module Name: Bison/3.0.4-GCCcore-7.1.0
    PASSED -  Module Name: Bison/3.0.4-GCCcore-8.1.0
    PASSED -  Module Name: Bison/3.0.5
    PASSED -  Module Name: Bison/3.0.5-GCCcore-6.4.0
    PASSED -  Module Name: Bison/3.0.5-GCCcore-8.1.0
    PASSED -  Module Name: Bison/3.2.2-GCCcore-7.4.0
    PASSED -  Module Name: Bison/3.3.2
    PASSED -  Module Name: Bison/3.3.2-GCCcore-8.3.0

Note, when you use ``name`` it will test all modules with the name ``Automake`` and ``Bison`` found in all module trees.
If you would like to filter and include by a full canonical name you can specify the ``include`` option. Shown below
we will only test module ``CUDA/10.0.130``.

.. code-block:: python

    >>> h = ModuleLoadTest("/mxg-hpc/users/ssi29/easybuild/modules/all",include=["CUDA/10.0.130"])
    Testing the Following Module Trees: /mxg-hpc/users/ssi29/easybuild/modules/all
    ________________________________________________________________________________
    PASSED -  Module Name: CUDA/10.0.130


Likewise, we can exclude module by full canonical name using the ``exclude`` argument which is a list of module names. In
example below we test the module tree ``"/usr/share/lmod/lmod/modulefiles/Core"`` which comes with ``lmod`` and ``settarg``
typically found when installing Lmod. In the second example we exclude ``lmod`` from the module test.

.. code-block:: python

    >>> a = ModuleLoadTest("/usr/share/lmod/lmod/modulefiles/Core")
    Testing the Following Module Trees: /usr/share/lmod/lmod/modulefiles/Core
    ________________________________________________________________________________
    PASSED -  Module Name: lmod
    PASSED -  Module Name: settarg

    >>> b = ModuleLoadTest("/usr/share/lmod/lmod/modulefiles/Core",exclude=["lmod"])
    Testing the Following Module Trees: /usr/share/lmod/lmod/modulefiles/Core
    ________________________________________________________________________________
    PASSED -  Module Name: settarg

