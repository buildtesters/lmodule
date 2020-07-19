import os
import re
import subprocess
import sys
from lmod.module import Module

modules = subprocess.getoutput("module av -t")
modules = modules.split()

pass_counter = 0
fail_counter = 0
total = 0

for module in modules:
    # output of module tree is as follows '/path/to/tree:' so we remove trailing colon
    tree = module[:-1]
    # skip entry when it's module tree
    if os.path.exists(tree):
        print(f"Skipping tree: {tree}")
        continue
    if re.search("(\(default\))$",module):
        module = module.replace('(default)','')

    cmd = Module(module,debug=True)
    ret = cmd.test_modules(login=True)
    total += 1
    # if returncode is 0 mark as PASS
    if ret == 0:
        pass_counter+=1
    else:
        fail_counter+=1

pass_rate = pass_counter * 100 / total
fail_rate = fail_counter * 100 / total

print ("-------- SUMMARY ---------")
print (f"Total Pass: {pass_counter}/{total}")
print (f"Total Failure: {fail_counter}/{total}")
print (f"PASS RATE: {pass_rate:.3f}")
print (f"FAIL RATE: {fail_rate:.3f}")






