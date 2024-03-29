# Original Script is found in easybuilders/easybuild-framework:  https://github.com/easybuilders/easybuild-framework/blob/develop/easybuild/scripts/install_eb_dep.sh
#!/bin/bash
if [ $# -ne 1 ]; then
    echo "Usage: $0 <version>"
    exit 1
fi
VERSION=$1
LMOD_PACKAGE=Lmod-$VERSION
PREFIX=/opt/apps

PKG_URL="https://github.com/TACC/Lmod/archive/${VERSION}.tar.gz"
export PATH=$PREFIX/lmod/$VERSION/libexec:$PATH
export MOD_INIT=$PREFIX/lmod/$VERSION/init/profile

sudo apt-get update
sudo apt-get install -y lua5.3 liblua5.3-0 liblua5.3-dev lua-posix-dev lua-posix tcl tcl-dev tcl8.6 tcl8.6-dev lua-term lua-json lua-filesystem


echo "Installing ${LMOD_PACKAGE} @ ${PREFIX}..."
mkdir -p ${PREFIX}
set +e
wget ${PKG_URL} && tar xfz *${VERSION}.tar.gz
set -e
cd $LMOD_PACKAGE
./configure --prefix=$PREFIX && make && make install
