#!/bin/sh

#set -ex # increased logging
set -e # reduced logging

#.ci/silence.sh brew update # this seems to help to work around some homebrew issues; and fails on others

#------------
# Python 3.7.5 is installed by default
# to update use either:
#brew upgrade python
# or, to avoid issues with brew auto updates by deactivating them,
#HOMEBREW_NO_AUTO_UPDATE=1 brew install python

#brew uninstall numpy gdal postgis
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
#export PATH="/usr/local/opt/python@$3.10/bin:$PATH"

brew update && brew upgrade python
brew unlink python@3.11 && brew link --force python@3.11
#export PATH="/usr/local/Cellar/python@3.11/3.11.3bin:$PATH"
# upgrade venv
python3 -m venv --upgrade /Users/appveyor/venv3.11.0
# or create new
#python3.11 -m venv /Users/appveyor/venv3.11.3
echo $PATH


hash -r
uname -srv
which python3
python3 --version

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
