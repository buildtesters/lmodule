import os
from lmod.moduleloadtest import ModuleLoadTest

class TestModuleLoadTest:
    def test_disable_purge(self):
        ModuleLoadTest(purge=False)

    def test_enable_forcepurge(self):
        ModuleLoadTest(force=True)

    def test_filter_include(self):
        ModuleLoadTest(include=["lmod"])

    def test_filter_exclude(self):
        ModuleLoadTest(exclude=["lmod"])

    def test_filter_include_exclude(self):
        ModuleLoadTest(include=["lmod"],exclude=["lmod"])

    def test_filter_name(self):
        ModuleLoadTest(name=["lmod","settarg"])

    def test_by_count(self):
        ModuleLoadTest(count=1)

    def test_debug(self):
        ModuleLoadTest(debug=True)

    def test_lmod_tree(self):
        ModuleLoadTest(os.path.join(os.getenv("LMOD_PKG"),"modulefiles/Core"),debug=True)
