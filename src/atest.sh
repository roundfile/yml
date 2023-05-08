echo "---------------------------------"
echo "We are in atest.sh"


# List of accepted arguments
accepted_args=("macos" "linux")

# Check if an argument was passed
if [ $# -eq 0 ]; then
  echo "Error: no argument was passed"
  exit 1
fi

# Check if the argument matches one of the accepted strings
arg="$1"
if [[ ! " ${accepted_args[@]} " =~ " ${arg} " ]]; then
  echo "Error: invalid argument \"$arg\""
  echo "Accepted arguments are: ${accepted_args[@]}"
  exit 1
fi

# Echo the argument
echo "Argument: $arg"

# Extract the version number from the __version__ string
version=$(grep -oP "__version__ = '\K[0-9]+\.[0-9]+\.[0-9]+'" "artisanlib/__init__.py"  | tr -d "'")
echo "Version: $version"
echo "artisan-mac-$version.dmg"


echo " Now we'll do it by running python"
# Import the module and extract the version number
version=$(python3 -c "import artisanlib; print(artisanlib.__version__)")
echo "Version: $version"
echo "artisan-mac-$version.dmg"


echo " do the zip"
zip -rq ../generated-$arg.zip ../doc/help_dialogs/Output_html/ help/ translations/ uic/

exit 1

