#!/bin/sh

#set -ex
set -e  # reduced logging

if [ ! -z $APPVEYOR ]; then
    # Appveyor CI builds
    echo "NOTICE: Appveyor build"

else
    # standard local builds
    echo "NOTICE: Standard build"
    export PYTHON_V=3.11
    export PYTHON=/Library/Frameworks/Python.framework/Versions/${PYTHON_V}
    export PYTHONBIN=$PYTHON/bin
    export PYTHONPATH=$PYTHON/lib/python${PYTHON_V}

# for PyQt6:
    export QT_PATH=${PYTHONPATH}/site-packages/PyQt6/Qt6
    export QT_SRC_PATH=~/Qt/6.4.1/macos
    export PYUIC=pyuic6
    export PYRCC=pyrcc6
    export PYLUPDATE=./pylupdate6pro

    export MACOSX_DEPLOYMENT_TARGET=10.15
    export DYLD_LIBRARY_PATH=$PYTHON/lib:$DYLD_LIBRARY_PATH
    export PATH=$PYTHON/bin:$PYTHON/lib:$PATH
    export PATH=$QT_PATH/bin:$QT_PATH/lib:$PATH

    #export DYLD_FRAMEWORK_PATH=$QT_PATH/lib # with this line all Qt libs are copied into Contents/Frameworks. Why?

fi

# ui / qrc
echo "************* 0 **************"
# ui
find ui -iname "*.ui" | while read f
do
    fullfilename=$(basename $f)
    fn=${fullfilename%.*}
    if [ "$PYUIC" == "pyuic5" ]; then
        $PYUIC -o uic/${fn}.py --from-imports ui/${fn}.ui
    else
        $PYUIC -o uic/${fn}.py -x ui/${fn}.ui
    fi
done

# translations

if [ -f "$PYLUPDATE" ]; then
echo "************* 1 **************"
    $PYLUPDATE artisan.pro
fi

pwd
ls ~/Qt/6.4.2/macos/bin
ls ~/Qt/6.4/macos/bin

# there is no full Qt installation on Travis, thus don't run  lrelease
echo "************* 2 **************"
$QT_SRC_PATH/bin/lrelease -verbose artisan.pro
for f in translations/qtbase_*.ts
do
    echo "Processing $f file..."
    $QT_SRC_PATH/bin/lrelease -verbose $f
done

# convert help files from .xlsx to .py
echo "************* 3 **************"
python3 ..\doc\help_dialogs\Script\xlsx_to_artisan_help.py all

# distribution
rm -rf build dist
sleep .3 # sometimes it takes a little for dist to get really empty
echo "************* 4 **************"
python3 setup-macos3.py py2app | egrep -v '^(creating|copying file|byte-compiling|locate)'
