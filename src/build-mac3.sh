#!/bin/sh

#set -ex
set -e  # reduced logging

# add argument "legacy" to make a build that supports older OS X systems using an outdated Qt

if [ ! -z $APPVEYOR ]; then
    # Appveyor CI builds
    echo "NOTICE: Appveyor build"
    export PYTHON=/usr/local/opt/python@${PYTHON_V}
    export PYTHONBIN=$PYTHON/bin
    #PYTHONPATH set in appveyor.yml
#    export PYTHONPATH=/usr/local/lib/python${PYTHON_V}

# for PyQt6
    export QT_PATH=${PYTHONPATH}/site-packages/PyQt6/Qt6
    export QT_SRC_PATH==${QT_PATH}
    export PYUIC=pyuic6
    export PYRCC=pyrcc6
    export PYLUPDATE=./pylupdate6pro

#dave    export MACOSX_DEPLOYMENT_TARGET=10.15
#    export DYLD_LIBRARY_PATH=$PYTHON/lib:$DYLD_LIBRARY_PATH
fi

export PATH=$PYTHON/bin:$PYTHON/lib:$PATH
export PATH=$QT_PATH/bin:$QT_PATH/lib:$PATH
#export DYLD_FRAMEWORK_PATH=$QT_PATH/lib # with this line all Qt libs are copied into Contents/Frameworks. Why?


# ui / qrc
if [ -z $APPVEYOR ]; then
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

#    # qrc
#    find qrc -iname "*.qrc" | while read f
#    do
#        fullfilename=$(basename $f)
#        fn=${fullfilename%.*}
#        $PYRCC -o uic/${fn}_rc.py qrc/${fn}.qrc
#    done
fi

# translations
echo "************* 1 **************"

if [ -f "$PYLUPDATE" ]; then
    $PYLUPDATE artisan.pro
fi

# there is no full Qt installation on Travis, thus don't run  lrelease
if [ -z $APPVEYOR ]; then
    echo "************* 2 **************"
    $QT_SRC_PATH/bin/lrelease -verbose artisan.pro || true
    for f in translations/qtbase_*.ts
    do
        echo "Processing $f file..."
        $QT_SRC_PATH/bin/lrelease -verbose $f || true
    done
fi

# distribution
rm -rf build dist
sleep .3 # sometimes it takes a little for dist to get really empty
echo "************* 3 **************"
$PYTHONBIN/python3 setup-mac3.py py2app | egrep -v '^(creating|copying file|byte-compiling|locate)'
 is no full Qt installation on Travis, thus don't run  lrelease
if [ -z $APPVEYOR ]; then
    echo "************* 2 **************"
    $QT_SRC_PATH/bin/lrelease -verbose artisan.pro || true
    for f in translations/qtbase_*.ts
    do
        echo "Processing $f file..."
        $QT_SRC_PATH/bin/lrelease -verbose $f || true
    done
fi

# distribution
rm -rf build dist
sleep .3 # sometimes it takes a little for dist to get really empty
echo "************* 3 **************"
$PYTHONBIN/python3 setup-mac3.py py2app | egrep -v '^(creating|copying file|byte-compiling|locate)'
 