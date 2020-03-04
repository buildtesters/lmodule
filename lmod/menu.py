import argparse
from lmod import LMODULE_VERSION

class LmoduleParser:

    def __init__(self):
        epilog = "Documentation: https://lmodule.readthedocs.io/en/latest/index.html"
        description = "lmodule is a Python 3 API for Lmod module system."
        self.parser = argparse.ArgumentParser(
            prog="lmodule",
            formatter_class=argparse.RawDescriptionHelpFormatter,
            description=description,
            usage="%(prog)s [options] [COMMANDS]",
            epilog=epilog,
        )
        self.parser.add_argument("-t", "--tree", help="Specify root of module tree separated by colon")
        self.parser.add_argument("-s", "--software", help="List unique software from Spider", action="store_true")
        self.parser.add_argument("-p", "--parents", help="List all parent modules from all module trees", action="store_true")
        self.parser.add_argument("-V", "--version", action="version", version=f"""lmodule version {LMODULE_VERSION}""")

    def parse_options(self):
        """This method parses the argument from ArgumentParser."""

        args = self.parser.parse_args()
        return args