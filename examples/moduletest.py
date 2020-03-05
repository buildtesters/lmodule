import os, sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from lmod.module import Module

mod_names = ["GCCcore", "Python"]

a = Module(mod_names)
module_cmds = a.get_command()
rc = a.test_modules()

if rc == 0:
    print(f"The following modules:  {mod_names} were loaded successfully")
    print("\n")
    print(f"Command Executed: {module_cmds}")

# passing a module name ``invalid`` this is expected to fail during test
bad_names = ["GCCcore", "invalid"]
b = Module(bad_names)

print(f"Failed to load modules: {bad_names}")
print(f"Command Executed: {b.get_command()}")
print(f"return code: {b.test_modules()}")

# disable purge when loading modules
c = Module(mod_names, purge=False)
print(c.get_command())

# force purge modules
d = Module(mod_names, purge=True, force=True)
print(d.get_command())

e = Module(["Anaconda3/5.3.0", "M4/1.4.17"], debug=True)
e.test_modules()

f = Module("Anaconda3/5.3.0 M4/1.4.17", debug=True)
f.test_modules()
