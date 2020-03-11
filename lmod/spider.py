import json
import os
import subprocess


class Spider:
    """Class declaration of Spider class"""

    def __init__(self, tree=None):
        """Initialize method for Spider class.

        :param tree: User can specify a module tree to query from spider.
        :type tree: str
        """
        # set spider tree to value passed in to class or value of MODULEPATH
        self.tree = tree or os.getenv("MODULEPATH")

        # Lmod can be optionally installed for using modules
        self.spider_content = []
        if os.getenv("LMOD_DIR") and os.path.exists(os.getenv("LMOD_DIR", "")):
            spider_cmd = f"{os.getenv('LMOD_DIR')}/spider -o spider-json {self.tree}"
            out = subprocess.check_output(spider_cmd, shell=True).decode("utf-8")
            self.spider_content = json.loads(out)

    def get_trees(self):
        """" Return module trees used in spider command

        :return: return module trees used for querying from spider
        :rtype: str
        """
        return self.tree

    def get_names(self, name=[]):
        """Return all keys from spider. This is the unique software names.

        :return: return sorted list of all spider keys.
        :rtype: list
        """
        if name:
            name_list = set(name).intersection(self.spider_content.keys())
            return sorted(name_list)
        else:
            return sorted(list(self.spider_content.keys()))

    def get_modules(self, name=[]):
        """Retrieve all module names from all module tree.

        :return: returns  a sorted list of all full canonical module name from all spider records.
        :rtype: list
        """

        module_names = []

        for module in self.get_names(name):
            for mpath in self.spider_content[module].keys():
                # skip modules that start with .version and .modulerc since they are not modules.
                module_version = os.path.basename(self.spider_content[module][mpath]["fullName"])
                if module_version.startswith(".version") or module_version.startswith(".modulerc"):
                    continue

                module_names.append(self.spider_content[module][mpath]["fullName"])

        return sorted(module_names)

    def get_parents(self):
        """Return all parent modules from all spider trees. This will search all ``parentAA`` keys in spider
         content. The parent modules are used for setting MODULEPATH to other trees.

        :return: sorted list of all parent modules.
        :rtype: list
        """

        # we only care about unique modules. parentAA is bound to have duplicate modules.
        parent_set = set()

        for module in self.get_names():
            for mpath in self.spider_content[module].keys():
                if "parentAA" in self.spider_content[module][mpath].keys():
                    for parent_comb in self.spider_content[module][mpath]["parentAA"]:
                        [parent_set.add(parent_module) for parent_module in parent_comb]

        return sorted(list(parent_set))

    def get_all_versions(self, key):
        """Get all versions of a particular software name.
        :param key: name of software
        :type key: str

        :return: list of module name as versions
        """

        # return empty list of key is not found
        if key not in self.get_names():
            return []

        all_versions = []

        for modulefile in self.spider_content[key].keys():
            all_versions.append(self.spider_content[key][modulefile]["Version"])

        return all_versions
