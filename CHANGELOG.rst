v0.3.0 - Oct 18th, 2022
-------------------------

- Make sure all commands work in login shell with `Module` class `#23 <https://github.com/buildtesters/lmodule/pull/23>`_.
- Update Documentation for modules class
- Update codecov setting for commenting on PRs `#25 <https://github.com/buildtesters/lmodule/pull/25>`_
- Update black setting in regression test, pre-commit and applying to source code `#31 <https://github.com/buildtesters/lmodule/pull/31>`_
- Increase regression test coverage for `spider` class `#34 <https://github.com/buildtesters/lmodule/pull/34>`_

v0.2.0 - Oct 24 2021
---------------------

Add ``spider`` method in Module class which mimics ``module spider`` command. This was implemented in
`#16 <https://github.com/buildtesters/lmodule/pull/16>`_

A few additional improvement to project such as including api docs (`#15 <https://github.com/buildtesters/lmodule/pull/15>`_),
black integration (`#17 <https://github.com/buildtesters/lmodule/pull/17>`_) and enable github workflow for
running regression test (`#18 <https://github.com/buildtesters/lmodule/pull/18>`_)


v0.1.0 - March 25 2020
----------------------

The first release of lmodule v0.1.0 includes three python classes: ``Module``, ``Spider``, and ``ModuleLoadTest``

The features for Module class include:

- Pass modules to Module class and you can use get_command to retrieve module load command with list of modules
- You can test modules using test_command
- Save modules into a user collection via save and show collection content via describe.
- You can get & test collection via get_collection and test_collection
- Get Lmod version via version
- Check if module is avail via is_avail and avail
- Return a list of user collection via get_user_collections
- Features for Spider class include:

- **get_trees** will return a list of module trees used by spider
- **get_names** will return a list of software names
- **get_modules** will return a list of full canonical module names
- **get_parents** will return a list of parent modules
- **get_all_version** will return a list of versions for a particular software

**ModuleLoadTest** will automate module load test for one or more module trees.

This class include features such as

  - testing one or more module trees, by default it resorts to MODULEPATH when testing
  - tweak module purge and module --force purge when testing modules
  - test modules in login shell, defaults to subshell
  - Enable debug to view extra output during the test
  - Filter module by software name when testing
  - Filter include and exclude module by full canonical module name
  - Run test up to a count threshold
