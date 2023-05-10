#!/bin/bash

# requires environment variables...

# List of accepted arguments

# Check if an argument was passed
if [ $# -eq 0 ]; then
  echo "Error: no argument was passed"
  exit 1
fi

# Check if the argument matches one of the accepted strings
case "$1" in
    macos|linux)
        # the argument is valid
        ;;
    *)
        echo "Error: invalid argument \"$arg\""
        echo "Argument is invalid: $1. Must be 'macos' or 'linux'"
        exit 1
        ;;
esac
echo "** Argument supplied: $1"

#accepted_args="macos" "linux"
#found_match=false
#for arg in $accepted_args; do
#    if [ "$1" = "$arg" ]; then
#        # Argument is valid
#        echo "Argument is valid: $1"
#        found_match=true
#        break
#    fi
#done
#
#if [ "$found_match" = false ]; then
#    # Argument is invalid
#    echo "Argument is invalid: $1"
#    exit 1
#fi

#arg="$1"
#if [[ ! " ${accepted_args[@]} " =~ " ${arg} " ]]; then
#  echo "Error: invalid argument \"$arg\""
#  echo "Accepted arguments are: ${accepted_args[@]}"
#  exit 1
#fi


#
# Generate translation, ui, and help files dependent on repository sources
#
# convert help files from .xlsx to .py
echo "************* help files **************"
python3 ../doc/help_dialogs/Script/xlsx_to_artisan_help.py all
if [ $? -ne 0 ]; then exit $?; else echo "** Success"; fi

# ui / uix
echo "************* ui/uic **************"
find ui -iname "*.ui" | while read f
do
    fullfilename=$(basename $f)
    fn=${fullfilename%.*}
#    if [ "$PYUIC" == "pyuic5" ]; then
#        $PYUIC -o uic/${fn}.py --from-imports ui/${fn}.ui
#    else
    $PYUIC -o uic/${fn}.py -x ui/${fn}.ui
    if [ $? -ne 0 ]; then exit $?; fi
#    fi
done
echo "** Success"

# translations
echo "************* pylupdate **************"
python3 $PYLUPDATE
if [ $? -ne 0 ]; then exit $?; else echo "** Success"; fi

echo "************* lrelease **************"
echo "*** artisan.pro"
$QT_SRC_PATH/bin/lrelease -verbose artisan.pro
if [ $? -ne 0 ]; then exit $?; else echo "** Success"; fi
echo "*** translations/qtbase_*.ts"
for f in translations/qtbase_*.ts
do
    echo "Processing $f file..."
    $QT_SRC_PATH/bin/lrelease -verbose $f
    if [ $? -ne 0 ]; then exit $?; fi
done
echo "** Success"

# create a zip with the generated files
echo "************* zip generated files **************"
echo "** Argument supplied: $1"
zip -rq ../generated-$1.zip ../doc/help_dialogs/Output_html/ help/ translations/ uic/
if [ $? -ne 0 ]; then exit $?; else echo "** Success"; fi
#
#  End of generating dependent files
#
