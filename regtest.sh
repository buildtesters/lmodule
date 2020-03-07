#!/bin/bash
source /opt/apps/lmod/7.8.2/init/profile
module use $LMOD_PKG/modulefiles/Core
echo $MODULEPATH
cd $TRAVIS_BUILD_DIR
echo $MODULEPATH
echo $BASH_ENV
env | grep LMOD
module av
coverage run -m pytest -vra tests/
coverage report -m