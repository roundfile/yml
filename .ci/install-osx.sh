#!/bin/sh

#set -ex # increased logging
set -e # reduced logging

#.ci/slience.sh brew update # this seems to help to work around some homebrew issues; and fails on others

#------------
# Python 3.7.5 is installed by default
# to update use either:
#brew upgrade python
# or, to avoid issues with brew auto updates by deactivating them,
#HOMEBREW_NO_AUTO_UPDATE=1 brew install python

#brew uninstall numpy gdal postgis
#brew unlink python@2
#brew unlink python
#brew upgrade python

#brew install python@3.8
#brew link --force --overwrite python@3.8


# following https://stackoverflow.com/questions/51125013/how-can-i-install-a-previous-version-of-python-3-in-macos-using-homebrew/51125014#51125014
# to install Python 3.6.5
#brew remove --ignore-dependencies python 1>/dev/null 2>&1
#brew install https://raw.githubusercontent.com/Homebrew/homebrew-core/f2a764ef944b1080be64bd88dca9a1d80130c558/Formula/python.rb 1>/dev/null 2>&1
#------------

## upgrade python from 3.9 to 3.10
# 3.10.2 now already installed on AppVeyor
#brew install python@3.10
#brew unlink python@3.9
#brew link --force python@3.10
#export PATH="/usr/local/opt/python@${PYTHON_V}/bin:$PATH"
export PATH="$PYTHONPATH/bin:$PATH"

hash -r
which python3
python3 --version


# to work around a wget open ssl issue: dyld: Library not loaded: /usr/local/opt/openssl/lib/libssl.1.0.0.dylib
# however for now we settled to use curl instead to download the upload script
#brew uninstall wget
#brew install wget


#brew install p7zip

python3 -m pip install --upgrade pip
sudo -H python3 -m pip install --root-user-action=ignore -r src/requirements.txt
sudo -H python3 -m pip install --root-user-action=ignore -r src/requirements-${ARTISAN_OS}.txt

#debug
sudo -H python3 -m pip show snap7

# copy the snap7 binary installed by pip
cp -f ${PYTHONPATH}/lib/site-packages/snap7/lib/libsnap7.dylib /usr/local/lib


