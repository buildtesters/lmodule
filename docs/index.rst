.. lmodule documentation master file, created by
   sphinx-quickstart on Tue Mar  3 22:08:29 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to lmodule documentation!
===================================

`lmodule <https://github.com/HPC-buildtest/lmodule>`_ is a Python API for `Lmod <https://lmod.readthedocs.io/en/latest>`_
module system. lmodule was originally part of `buildtest <https://github.com/HPC-buildtest/buildtest-framework>`_ and
we decided that it could benefit the entire community for folks interested in using the API but not relying on buildtest.
The documentation is built for version |version| on |today|

What is lmodule?
-----------------

Lmodule is a Python 3 API that allows you to interact with the **module** command provided by Lmod in a programmatic way.
The API comes with three classes:

- Module:  This class emulates the ``module`` command

- Spider: This class runs the Lmod ``spider`` command to retrieve all module records in json

- ModuleLoadTest: This class automates ``module load`` of one or more module trees

Why use lmodule?
----------------

Here are few reasons why you would want to use lmodule

1. Currently, there is no Python API for Lmod, however there is a python interface ``LMOD_CMD python`` by Lmod that requires parsing and output is cryptic.
2. Automates ``module load`` test for each module in one or more module trees (Software Stack). This can be used to spot faulty modules in a large software stack. This type of test is meant to run using CI tool for continuous testing of module stack.


.. toctree::
   :maxdepth: 2
   :caption: Contents:

   installation.rst
   module.rst
   spider.rst
   moduleloadtest.rst



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
