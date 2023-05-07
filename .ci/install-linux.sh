#!/bin/sh

#pip install PyQt6==6.5.0
#
#echo ${PYTHON_PATH}
#ls -l ${PYTHON_PATH}
#echo ${QT_PATH}
#ls -l ${QT_PATH}
#echo .
#ls -l .
#echo ${HOME}/Qt/6.4.2/gcc_64/bin
#ls -l ${HOME}/Qt/6.4.2/gcc_64/bin
#echo whereis lrelease
#whereis lrelease
#exit 1

set -ex
sudo apt-get update -y -q
sudo apt-get install -y -q ruby-dev build-essential p7zip-full rpm gdb libudev-dev qt5-default
sudo apt-get install -y -q fakeroot

# add libs not installed by default on Qt5.15 any longer
sudo apt-get install -y -q libdbus-1-3 libxkbcommon-x11-0 libxcb-icccm4 libxcb-image0 libxcb-keysyms1 libxcb-randr0 libxcb-render-util0 libxcb-xinerama0 libxcb-xfixes0

gem install fpm -v 1.12.0 # Linux build fails using 1.13.0
pip install --upgrade pip
pip install -r src/requirements.txt
pip install -r src/requirements-${ARTISAN_OS}.txt

# copy the snap7 binary installed by pip
sudo cp -f ${PYTHONSITEPKGS}/snap7/lib/libsnap7.so /usr/lib

.ci/install-libusb.sh
