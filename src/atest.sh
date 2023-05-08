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
version=$(grep -oP "__version__ = \K[0-9]+\.[0-9]+\.[0-9]+" "artisanlib/__init__.py")
echo "Version: $version"
echo "artisan-mac-$version.dmg"

exit 1

