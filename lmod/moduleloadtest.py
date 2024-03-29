import os
from lmod.module import Module
from lmod.spider import Spider


class ModuleLoadTest:
    """This is the class declaration of ModuleLoadTest. This class will automate module load
    test for all modules in one or more module tree (Software Stack) retrieved by Spider class. The output
    of ``module load`` is a 0 or 1 that can be used to determine PASS/FAIL on a module. Each module test will attempt
    to test the ``module load`` command using the ``Module().test_modules()``. In order to run tests properly,
    MODULEPATH must be set in your environment.
    """

    def __init__(
        self,
        tree=None,
        purge=True,
        force=False,
        debug=False,
        count=999999999,
        name=[],
        include=[],
        exclude=[],
        login=False,
    ):
        """This is the initializer method for ModuleLoadTest class.

        Parameters:
        -----------
        :param tree: specify one or more module trees to test. The module tree must be root directory where modulefiles
         are found. Use a colon ``:`` to define more than one module tree.
        :type tree: str

        :param purge: control whether to run ``module purge`` before loading each module
        :type purge: bool

        :param force: control whether to run ``module --force purge`` before loading each module
        :type purge: bool

        :param login: controls whether to run test in login shell when ``login=True``. By default tests are run in sub-shell.
        :type purge: bool

        :param count: control how many tests to run before exiting
        :type purge: int

        :param name: filter modules by software name to test
        :type name: list

        :param include: specify a list of modules to **include** by full canonical name for testing
        :type purge: list

        :param exclude: specify a list of modules to **exclude** by full canonical name for testing
        :type purge: list

        :return: Result of module load test
        :rtype: None
        """

        # setting module tree to argument passed in or default to MODULEPATH
        self.tree = tree or os.getenv("MODULEPATH")
        self.debug = debug
        self.purge = purge
        self.force = force
        self.login = login
        self.count = count
        self.name = name
        self.include = include
        self.exclude = exclude

        self.failed = 0
        self.passed = 0
        self.modulecount = 0

        if self.count < 1:
            raise SystemExit(
                "Please specify a number greater than 0 in order to test modules"
            )

        spider_cmd = Spider(self.tree)
        module_dict, modules = (
            spider_cmd.get_modules(self.name),
            list(spider_cmd.get_modules(self.name).values()),
        )

        if self.include:
            modules = [module for module in modules if module in self.include]

        # only do exclusion if include list is not specified
        if self.exclude:
            for name in self.exclude:
                if name in modules:
                    modules.remove(name)

        if not modules:
            raise SystemExit(
                "Unable to test any modules either no modules were detected or search criteria was too restrictive"
            )

        print(f"Testing the Following Module Trees: {self.tree}")
        print("{:_<80}".format(""))

        for module_name in modules:
            module_cmd = Module(
                module_name,
                purge=self.purge,
                force=self.force,
                debug=self.debug,
            )
            ret = module_cmd.test_modules(self.login)

            # extract modulefile based on module name. This is basically getting the key from dictionary (module_dict)
            # This is only used for printing purposes since it helps to know which module is tested. Simply putting
            # the full module canonical name is not enough.
            modulefile = list(module_dict.keys())[
                list(module_dict.values()).index(module_name)
            ]

            if ret == 0:
                print(
                    f"PASSED -  Module Name: {module_name} ( modulefile={modulefile} )"
                )
                self.passed += 1
            else:
                print(
                    f"FAILED -  Module Name: {module_name} ( modulefile={modulefile} )"
                )
                self.failed += 1

            self.modulecount += 1

            # terminate module load test once we have tested up to specified count
            if self.count <= self.modulecount:
                return

    def get_results(self):
        """This method returns a dictionary of test results

        :return: dictionary of test results
        :rtype: dict
        """
        return {
            "passed": self.passed,
            "failed": self.failed,
            "total": self.modulecount,
            "rate": self.passed / self.modulecount
            if self.modulecount
            else float("nan"),
        }
