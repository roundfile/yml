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
    #remove export PYRCC=pyrcc6
    export PYLUPDATE=./pylupdate6pro

    export MACOSX_DEPLOYMENT_TARGET=10.15
    export DYLD_LIBRARY_PATH=$PYTHON/lib:$DYLD_LIBRARY_PATH
    export PATH=$PYTHON/bin:$PYTHON/lib:$PATH
    export PATH=$QT_PATH/bin:$QT_PATH/lib:$PATH

    #export DYLD_FRAMEWORK_PATH=$QT_PATH/lib # with this line all Qt libs are copied into Contents/Frameworks. Why?

fi

echo "ls help before Help"
ls ./help

# convert help files from .xlsx to .py
echo "************* help **************"
python3 ../doc/help_dialogs/Script/xlsx_to_artisan_help.py all

echo "ls help after Help"
ls ./help
echo "ls help html after Help"
ls ../doc/help_dialogs/Output_html

echo "ls uic before PYUIC"
ls ./uic

# ui / qrc
echo "************* ui/uic **************"
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
echo "ls uic after PYUIC"
ls ./uic


# translations
echo "ls translations before pylupdate"
ls translations

if [ -f "$PYLUPDATE" ]; then
    echo "************* pylupdate **************"
    $PYLUPDATE artisan.pro
else
    echo "************* skip pylupdate **************"
fi

echo "ls translations after pylupdate"
ls translations
#pwd
#echo "ls $QT_SRC_PATH"
#ls $QT_SRC_PATH
##ls /Users/appveyor/Qt/6.4.0/macos/bin/lrelease
##ls /Users/appveyor/Qt/6.4/macos/bin/lrelease
##ls ~
##ls ~/Qt/6.4/macos/bin/lrelease
##echo "~/Qt/6.4/macos/bin/lrelease"
##ls ~/Qt/6.4/macos/bin/lrelease

# there is no full Qt installation on Travis, thus don't run  lrelease
echo "************* lrelease **************"
$QT_SRC_PATH/bin/lrelease -verbose artisan.pro
for f in translations/qtbase_*.ts
do
    echo "Processing $f file..."
    $QT_SRC_PATH/bin/lrelease -verbose $f
done

echo "ls translations after lrelease"
ls translations


# create a zip with the generated files
echo "************* generated zip **************"
zip -rq ../generated-macos.zip ../doc/help_dialogs/Output_html/
zip -rq ../generated-macos.zip translations/
zip -rq ../generated-macos.zip uic/

# distribution
rm -rf build dist
sleep .3 # sometimes it takes a little for dist to get really empty
echo "************* p2app **************"
python3 setup-macos3.py py2app | egrep -v '^(creating|copying file|byte-compiling|locate)'
