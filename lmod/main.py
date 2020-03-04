

def main():
    """Entry point for lmodule"""
    from lmod.menu import LmoduleParser
    from lmod.spider import Spider
    parser = LmoduleParser()
    args = parser.parse_options()

    if args.software:
        a = Spider(args.tree)
        unique_software = a.get_unique_software()
        [print (x) for x in unique_software]

    if args.parents:
        a = Spider(args.tree)
        parent_modules = a.get_all_parents()
        [print (x) for x in parent_modules]




if __name__ == "main":
    """Entry point for lmodule"""
    main()