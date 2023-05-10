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
    export QT_SRC_PATH=~/Qt6.5/6.5.0/macos
    export PYUIC=pyuic6
    #remove export PYRCC=pyrcc6
    export PYLUPDATE=./pylupdate6pro

    export MACOSX_DEPLOYMENT_TARGET=11.0
    export DYLD_LIBRARY_PATH=$PYTHON/lib:$DYLD_LIBRARY_PATH
    export PATH=$PYTHON/bin:$PYTHON/lib:$PATH
    export PATH=$QT_PATH/bin:$QT_PATH/lib:$PATH

    #export DYLD_FRAMEWORK_PATH=$QT_PATH/lib # with this line all Qt libs are copied into Contents/Frameworks. Why?
fi

echo "************* build dependent files **************"
./build-dependent.sh macos  #generate the dependent files
if [ $? -ne 0 ]; then echo "Failed in build-dependent.sh"; exit $?; else (echo "** Success"); fi


##
## Generate translation, ui, and help files dependent on repository sources
##
## convert help files from .xlsx to .py
#echo "************* help files **************"
#python3 ../doc/help_dialogs/Script/xlsx_to_artisan_help.py all
#if [ $? -ne 0 ]; then exit $?; else echo "** Success"; fi
#
## ui / uix
#echo "************* ui/uic **************"
#find ui -iname "*.ui" | while read f
#do
#    fullfilename=$(basename $f)
#    fn=${fullfilename%.*}
#    if [ "$PYUIC" == "pyuic5" ]; then
#        $PYUIC -o uic/${fn}.py --from-imports ui/${fn}.ui
#    else
#        $PYUIC -o uic/${fn}.py -x ui/${fn}.ui
#    fi
#    if [ $? -ne 0 ]; then exit $?; fi
#done
#echo "** Success"
#
## translations
#echo "************* pylupdate **************"
#python3 $PYLUPDATE
#if [ $? -ne 0 ]; then exit $?; else echo "** Success"; fi
#echo "************* lrelease **************"
#echo "*** artisan.pro"
#$QT_SRC_PATH/bin/lrelease -verbose artisan.pro
#if [ $? -ne 0 ]; then exit $?; else echo "** Success"; fi
#echo "*** translations/qtbase_*.ts"
#for f in translations/qtbase_*.ts
#do
#    echo "Processing $f file..."
#    $QT_SRC_PATH/bin/lrelease -verbose $f
#    if [ $? -ne 0 ]; then exit $?; fi
#done
#echo "** Success"
#
## create a zip with the generated files
#echo "************* zip generated files **************"
#zip -rq ../generated-macos.zip ../doc/help_dialogs/Output_html/ help/ translations/ uic/
#if [ $? -ne 0 ]; then exit $?; else echo "** Success"; fi
##
##  End of generating dependent files
##


# distribution
rm -rf build dist
sleep .3 # sometimes it takes a little for dist to get really empty
echo "************* p2app **************"
python3 setup-macos3.py py2app | egrep -v '^(creating|copying file|byte-compiling|locate)'


# Check that the packaged files are above an expected size
version=$(python3 -c "import artisanlib; print(artisanlib.__version__)")
basename="artisan-mac-$version"
echo "basename: $basename"
suffixes=".dmg" # array of suffixes to check
min_size=260000000
for suffix in $suffixes; do
    filename="$basename$suffix"
    size=$(($(du -k "$filename" | cut -f1) * 1024)) # returns kB so multiply by 1024 (du works on macOS)
    echo "$filename size: $size bytes"
    if [ "$size" -lt "$min_size" ]; then
        echo "$filename is smaller than $min_size bytes"
    else
        echo "$filename is larger than $min_size bytes"
    fi
done

#suffixes=(".dmg") # array of suffixes to check
#for suffix in "${suffixes[@]}"; do
#    filename="$basename$suffix"
#    #size=$(stat -c %s "$filename")
#    size=$(($(du -k "$filename" | cut -f1) * 1024))  #returns kB so multiply by 1024 (du works on macOS)
#    echo "$filename size: $size bytes"
#    if [ "$size" -lt "$min_size" ]; then
#        echo "$filename is smaller than $min_size bytes"
#    else
#        echo "$filename is larger than $min_size bytes"
#    fi
#done
#
