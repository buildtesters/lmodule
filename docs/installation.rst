Installation
==============

Requirements
--------------

You will need the following to use ``lmodule``.

- Python 3.6 or higher
- Lmod 7 or higher


PyPI Installation
--------------------

You can install lmdoule via pip as follows::

    pip install lmodule

Git
-------

If you prefer to use the latest codebase you can clone the repository as follows::

    $ git clone https://github.com/HPC-buildtest/lmodule.git

Next you will want to install lmodule in your python environment::

    # for user site installation
    $ python3 setup.py install --user

    # for virtual environment installation
    $ python3 setup.py install


Validation
-----------

If you are able to install lmodule in your python environment, you can test it as follows::


    $ python -c "from lmod.module import Module; print(Module().version())"
    7.8.16

The above command will import the Module class and return the Lmod version in your system.