#!/bin/bash 
set -ev
source /opt/apps/lmod/lmod/init/profile
module use $LMOD_PKG/modulefiles/Core
echo $MODULEPATH
cd $TRAVIS_BUILD_DIR
echo $MODULEPATH
echo $BASH_ENV
env | grep LMOD
module av
coverage run -m pytest -vra tests/
coverage report -m
