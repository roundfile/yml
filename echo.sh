#!/bin/sh

#echo ${HOME}
##echo ${PASTA}
##export FAZOOL=${HOME}/butterball
#echo ${FAZOOecho ${PYTON}echo ${PYTON}echo ${PYTON}L}
#echo ${PYTHON}
#echo ${PYTHON_PATH}
#wget -c https://github.com/AppImage/pkg2appimage/releases/download/continuous/pkg2appimage-1807-x86_64.AppImage
echo ------------
echo wget -c https://github.com/AppImage/pkg2appimage/releases/expanded_assets/continuous
echo ------------
wget -c https://github.com/AppImage/pkg2appimage/releases/expanded_assets/continuous -O foo.txt
echo ------------
echo cat foo.txt
echo ------------
cat foo.txt

echo ------------
echo wget -c https://github.com/AppImage/pkg2appimage/releases/expanded_assets/continuous -O - pipe grep "pkg2appimage-.*-x86_64.AppImage" pipe head -n 1 pipe cut -d '"' -f 2
echo ------------
wget -c https://github.com/AppImage/pkg2appimage/releases/expanded_assets/continuous -O - | grep "pkg2appimage-.*-x86_64.AppImage" | head -n 1 | cut -d '"' -f 2
