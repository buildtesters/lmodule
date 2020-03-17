from lmod.moduleloadtest import ModuleLoadTest

a = ModuleLoadTest()
b = ModuleLoadTest(count=5)
c = ModuleLoadTest("/usr/share/lmod/lmod/modulefiles/Core", debug=True)
d = ModuleLoadTest("/usr/share/lmod/lmod/modulefiles/Core", force=True, debug=True)
e = ModuleLoadTest("/usr/share/lmod/lmod/modulefiles/Core", purge=False, debug=True)
f = ModuleLoadTest(
    "/usr/share/lmod/lmod/modulefiles/Core:/mxg-hpc/users/ssi29/spack/modules/linux-rhel7-x86_64/Core",
    purge=False,
)
g = ModuleLoadTest(
    "/mxg-hpc/users/ssi29/easybuild/modules/all", name=["Automake", "Bison"]
)
h = ModuleLoadTest(
    "/mxg-hpc/users/ssi29/easybuild/modules/all", include=["CUDA/10.0.130"]
)
i = ModuleLoadTest("/usr/share/lmod/lmod/modulefiles/Core", exclude=["lmod"])
j = ModuleLoadTest(
    "/usr/share/lmod/lmod/modulefiles/Core", include=["settarg"], exclude=["lmod"]
)
k = ModuleLoadTest("/mxg-hpc/users/ssi29/spack/modules/linux-rhel7-x86_64/Core")
l = ModuleLoadTest("/usr/share/lmod/lmod/modulefiles/Core", debug=True,login=True)
