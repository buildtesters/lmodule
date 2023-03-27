Welcome to lmodule documentation!
===================================

|docs| |codecov| |version| |license| |pypi| |python|


.. |docs| image:: https://readthedocs.org/projects/lmodule/badge/?version=latest
    :target: https://readthedocs.org/projects/lmodule/builds/
    :alt: Documentation Status
.. |codecov| image:: https://codecov.io/gh/buildtesters/lmodule/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/buildtesters/lmodule
.. |license| image:: https://img.shields.io/github/license/buildtesters/lmodule.svg
    :target: https://github.com/buildtesters/lmodule/blob/master/LICENSE
.. |pypi| image:: https://img.shields.io/pypi/v/lmodule.svg
    :target: https://pypi.org/project/lmodule/
.. |python| image:: https://img.shields.io/pypi/pyversions/lmodule.svg
    :target: https://pypi.org/project/lmodule/
.. |version| image:: https://img.shields.io/github/release/buildtesters/lmodule.svg
    :target: https://github.com/buildtesters/lmodule/releases

`lmodule <https://github.com/buildtesters/lmodule>`_ is a Python API for `Lmod <https://lmod.readthedocs.io/en/latest>`_
module system. lmodule was originally part of `buildtest <https://github.com/buildtesters/buildtest>`_ and
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
   examples.rst
   api.rst

Presentations
-------------

.. csv-table::
    :header: "Conference", "Talk", "Date", "Link"
    :widths:  40, 50, 20, 20

    "`Improving Scientific Software Conference 2023 <https://sea.ucar.edu/conference/2023>`_", "**Lmodule - Python API for testing modules**", "Feb 17th 2023", "`PPTX <https://docs.google.com/presentation/d/1F2A1pUCvTSz8w3fU4dxBe-jQa7AgQU22/edit?usp=share_link&ouid=102126664227037583807&rtpof=true&sd=true>`_, `PDF <https://drive.google.com/file/d/1Ml19S5G39RbdlsAAYIbgxNkbI3wAEHvX/view?usp=share_link>`_"
    "`EasyBuild User Meeting <https://easybuild.io/eum/>`_", "**Automate Module Testing with Lmodule**", "Jan 29th 2021", "`PDF <https://drive.google.com/file/d/1Jvi8w0g4NzO2daRWi-bDXZl6LQdZ_q_4/view?usp=share_link>`_,  `Video <https://www.youtube.com/watch?v=RyUhPSzIrqQ&list=PLhnGtSmEGEQh0pCtmkFQsDzeoo6tbYnyZ&index=30>`_"



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
