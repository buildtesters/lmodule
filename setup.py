from setuptools import setup, find_packages
from lmod import LMODULE_VERSION

setup(
    name="lmodule",
    version=LMODULE_VERSION,
    author="Shahzeb Siddiqui",
    author_email="shahzebmsiddiqui@gmail.com",
    description="Lmod Module API",
    long_description=open("README.rst").read(),
    url="https://github.com/buildtesters/lmodule",
    license="MIT",
    python_requires=">=3.6, <4",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Software Development :: Libraries",
    ],
    packages=find_packages(),
    include_package_data=True,
    project_urls={
        "Source Code": "https://github.com/buildtesters/lmodule",
        "Documentation": "https://lmodule.readthedocs.io/",
        "Bug Report": "https://github.com/buildtesters/lmodule/issues",
    },
)
