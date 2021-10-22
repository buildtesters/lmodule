import json
import os
import subprocess


class Spider:
    """This is the class declaration of Spider class which emulates the spider tool provided by Lmod. The spider command
    is typically used to build the spider cache in your site. We use the spider tool to fetch all module files.

    Public Methods:

    get_trees: returns all module trees used with spider command
    get_names: returns all top-level keys from spider which is the software name
    get_modules: returns all full canonical module name.
    get_parents: return all parent modules, parent modules are modules that set MODULEPATH to another tree.
    get_all_versions: returns all versions of a specified module.
    """

    def __init__(self, tree=None):
        """Initialize method for Spider class. The spider tool is provided by Lmod typically found in ``LMOD_DIR/spider``.
        We are running ``spider -o spider-json <module-tree>``. If no argument is specified, then we default to
        MODULEPATH as the tree. One can pass one or more module tree separated by colon (``:``). The output will
        be a json structure (``dict``) that is stored in class variable ``self.spider_content``.


        Parameters:

        :param tree: User can specify one or more module trees to query from spider. Trees must be separated by colon (``:``)
        :type tree: str, optional
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
        """ "Return module trees used in spider command.

        :return: return module trees used for querying from spider
        :rtype: str
        """
        return self.tree

    def get_names(self, name=[]):
        """Returns a list of software names which are found by returning the top-level key from json structure.
        One can specify a list of module names to filter output.

        Parameters:

        :param name: a list of software name to filter output
        :type name: list, optional

        :return: return sorted list of all spider keys.
        :rtype: list
        """

        if name:
            name_list = set(name).intersection(self.spider_content.keys())
            return sorted(name_list)
        else:
            return sorted(list(self.spider_content.keys()))

    def get_modules(self, name=[]):
        """Retrieve all full-canonical module names. This can be retrieved by fetching ``fullName`` key
        in the json output. The full-canonical module name represents the actual module name. One can
        filter output by passing a list of software names, if no argument is specified we will return all
        modules. We ignore spider records that contain ``.version`` or ``.modulerc`` whih are not actual
        modules.

        Parameters:

        :param name: a list of software name to filter output
        :type name: type, required

        :return: returns  a sorted list of all full canonical module name from all spider records.
        :rtype: dict
        """

        module_names = {}

        for module in self.get_names(name):
            for mpath in self.spider_content[module].keys():
                # skip modules that start with .version and .modulerc since they are not modules.
                module_version = os.path.basename(
                    self.spider_content[module][mpath]["fullName"]
                )
                if module_version.startswith(".version") or module_version.startswith(
                    ".modulerc"
                ):
                    continue

                module_names[mpath] = self.spider_content[module][mpath]["fullName"]

        return module_names

    def get_parents(self):
        """Return all parent modules from all spider trees. This will search all ``parentAA`` keys in spider
        content. The parent modules are used for setting MODULEPATH to other trees. The parentAA is a nested list
        containing one or more parent module combination required to load a particular module. The spider output
        can contain several occurrences of parent modules in parentAA key so use a ``set`` to add unique parent modules.

        :return: sorted list of all parent modules.
        :rtype: list
        """

        # we only care about unique modules. parentAA is bound to have many modules.
        parent_set = set()

        for module in self.get_names():
            for mpath in self.spider_content[module].keys():
                if "parentAA" in self.spider_content[module][mpath].keys():
                    for parent_comb in self.spider_content[module][mpath]["parentAA"]:
                        [parent_set.add(parent_module) for parent_module in parent_comb]

        return sorted(list(parent_set))

    def get_all_versions(self, key):
        """Get all versions of a particular software name. This is can be retrieved by reading ``Version`` key
        in spider output.

        Parameters:

        :param key: name of software
        :type key: str, required

        :return: list of module name as versions
        :rtype: list
        """

        # return empty list of key is not found
        if key not in self.get_names():
            return []

        all_versions = []

        for modulefile in self.spider_content[key].keys():
            all_versions.append(self.spider_content[key][modulefile]["Version"])

        return all_versions
