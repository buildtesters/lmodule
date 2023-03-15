import os
import pytest

from lmod.spider import Spider

lmodule_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.environ["LMODULE_MODULE_ROOT"] = os.path.join(lmodule_root, "tests", "modules")
module_tree = os.path.join(os.getenv("LMODULE_MODULE_ROOT"), "core")


class TestSpider:
    def test_get_spider_trees(self):
        """Check if spider will return the module trees. It should be value of MODULEPATH when no argument is passed
        into Spider class"""

        a = Spider()
        assert a.get_trees() == os.getenv("MODULEPATH")

        tree = "$LMOD_PKG/modulefiles/Core"
        b = Spider(tree)
        assert b.get_trees() == tree

        with pytest.raises(SystemExit):
            Spider("/xyz")

    def test_get_names(self):
        """Retrieve unique software from Spider class."""

        a = Spider()
        # the return type is expected to be a list
        assert isinstance(a.get_names(), list)

        # The Travis build should have lmod module that should be available
        assert "lmod" in a.get_names()

    def test_get_modules(self):
        """This test will retrieve full canonical module names from ``get_modules`` method which is expected to return a
        dictionary"""
        a = Spider(module_tree)
        # this will return the full canonical module name which should be a list.
        assert isinstance(a.get_modules(), dict)

    def test_get_parents(self):
        """This will retrieve all parent modules. The method ``get_parents`` is expected to return of type list"""
        a = Spider()
        parent_modules = a.get_parents()
        assert isinstance(parent_modules, list)

        a = Spider(module_tree)
        assert "gcc/9.3.0" in a.get_parents()

    def test_get_all_versions(self):

        a = Spider(module_tree)
        openmpi_versions = a.get_all_versions("openmpi")
        assert "3.0" in openmpi_versions
        assert "3.1" in openmpi_versions

        assert not a.get_all_versions("lmod")
