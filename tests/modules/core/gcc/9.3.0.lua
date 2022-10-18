local gcc_root = pathJoin(os.getenv("LMODULE_MODULE_ROOT"), 'gcc')
prepend_path("MODULEPATH", gcc_root)