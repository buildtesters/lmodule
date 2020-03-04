import os
from lmod.spider import Spider

class TestSpider:

    def test_get_spider_trees(self):
        """Check if spider will return the module trees. It should be value of MODULEPATH when no argument is passed
        into Spider class"""

        a = Spider()
        assert a.get_trees() == os.getenv("MODULEPATH")

        tree = "/opt/apps/lmod/lmod/modulefiles/Core"
        b = Spider(tree)
        assert b.get_trees() == tree 

    def test_get_unique_software(self):
        """Retrieve unique software and modules from Spider class."""

        a = Spider()
        # the return type is expected to be a list
        assert isinstance(a.get_unique_software(), list)

        # The Travis build should have lmod module that should be available
        assert "lmod" in a.get_unique_software()

        # this will return the full canonical module name which should be a list.
        assert isinstance(a.get_modules(), list)

        parent_modules = a.get_all_parents()
        assert isinstance(parent_modules, list)
        

