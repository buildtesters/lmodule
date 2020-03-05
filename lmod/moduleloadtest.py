import os
from lmod.module import Module
from lmod.spider import Spider


class ModuleLoadTest:
    """This is the class declaration of ModuleLoadTest. This class will automate module load
    test for all modules in one or more module tree (Software Stack).
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
    ):
        """This is the initializer method that automates testing of modules

        :param tree: specify one or more module trees to test. The module tree must be root directory where modulefiles
        are found. Use a colon ``:`` to define more than one module tree.
        :type tree: str

        :param purge: control whether to run ``module purge`` before loading each module
        :type purge: bool

        :param force: control whether to run ``module --force purge`` before loading each module
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
        self.count = count
        self.name = name
        self.include = include
        self.exclude = exclude
        filter_modules = None

        spider_cmd = Spider(self.tree)
        modules = spider_cmd.get_modules(self.name)

        if self.include:
            filter_modules = set(self.include).intersection(modules)

        # only do exclusion if include list is not specified
        if self.exclude and not self.include:
            filter_modules = set(modules).difference(self.exclude)

        modules = filter_modules or modules

        modulecount = 0
        print(f"Testing the Following Module Trees: {self.tree}")
        print("{:_<80}".format(""))
        for module_name in modules:
            module_cmd = Module(
                module_name, purge=self.purge, force=self.force, debug=self.debug
            )
            ret = module_cmd.test_modules()

            if ret == 0:
                print(f"PASSED -  Module Name: {module_name} ")
            else:
                print(f"FAILED -  Module Name: {module_name} ")

            modulecount += 1

            # terminate module load test once we have tested up to specified count
            if self.count <= modulecount:
                return
