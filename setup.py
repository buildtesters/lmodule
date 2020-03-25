from setuptools import setup, find_packages
from lmod import LMODULE_VERSION

setup(
    name="lmodule",
    version=LMODULE_VERSION,
    author="Shahzeb Siddiqui",
    author_email="shahzebmsiddiqui@gmail.com",
    description="Lmod Module API",
    long_description=open("README.rst").read(),
    url="https://github.com/HPC-buildtest/lmodule",
    license="MIT",
    python_requires="~=3.6",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3.6",
        "Topic :: Software Development :: Libraries",
    ],
    packages=find_packages(),
    include_package_data=True,
)
