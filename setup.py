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
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3.6",
        "Topic :: Software Development :: Testing",
    ],
    packages=find_packages(),
    include_package_data=True,
    entry_points={"console_scripts": ["lmodule=lmod.main:main"]},
)
