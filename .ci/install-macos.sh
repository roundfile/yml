#!/bin/sh
# ABOUT
# CI install shell script for Artisan macOS builds
#
# LICENSE
# This program or module is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as published
# by the Free Software Foundation, either version 2 of the License, or
# version 3 of the License, or (at your option) any later versison. It is
# provided for educational purposes and is distributed in the hope that
# it will be useful, but WITHOUT ANY WARRANTY; without even the implied
# warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See
# the GNU General Public License for more details.
#
# AUTHOR
# Dave Baxter, Marko Luther 2023

#set -ex # increased logging
set -e # reduced logging

echo "** Running install-macos.sh"

#.ci/silence.sh brew update # this seems to help to work around some homebrew issues; and fails on others

# upgrade Python PYUPGRADE_V exists and has a value
if [ -n "${PYUPGRADE_V:-}" ]; then
    # first deactivate current venv
    source ${VIRTUAL_ENV}/bin/activate
    deactivate
    # brew update Python
    brew update && brew upgrade python
    # relink Python
    brew unlink python@${PYTHON_V} && brew link --force python@${PYTHON_V}
    # add path
    export PATH="$(brew --prefix)/Cellar/python@${PYTHON_V}/${PYUPGRADE_V}/bin:${PATH}"
    # create new venv
    python3 -m venv /Users/appveyor/venv${PYUPGRADE_V}
    source /Users/appveyor/venv${PYUPGRADE_V}/bin/activate
    # update symbolic link to point to our new venv
    ln -vfns /Users/appveyor/venv${PYUPGRADE_V} /Users/appveyor/venv${PYTHON_V}
    export PATH=/Users/appveyor/venv${PYUPGRADE_V}/bin:${PATH} # not exported?
fi 

hash -r
uname -srv
which python3
python3 --version
echo "PYTHON_PATH:    ${PYTHON_PATH}"
echo "PYTHONSITEPKGS: ${PYTHONSITEPKGS}"
exit 1

# to work around a wget open ssl issue: dyld: Library not loaded: /usr/local/opt/openssl/lib/libssl.1.0.0.dylib
# however for now we settled to use curl instead to download the upload script
#brew uninstall wget
#brew install wget


#brew install p7zip

python -m pip install --upgrade pip
sudo -H python -m pip install --root-user-action=ignore -r src/requirements.txt
sudo -H python -m pip install --root-user-action=ignore -r src/requirements-${ARTISAN_OS}.txt

# copy the snap7 binary installed by pip
cp -f ${PYTHONSITEPKGS}/snap7/lib/libsnap7.dylib /usr/local/lib
