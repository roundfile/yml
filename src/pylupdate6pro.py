# ABOUT
# Qt Translation processing for Artisan
#
# LICENSE
# This program or module is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as published
# by the Free Software Foundation, either version 2 of the License, or
# version 3 of the License, or (at your option) any later versison. It is
# provided for educational purposes and is distributed in the hope that
# it will be useful, but WITHOUT ANY WARRANTY; without even the implied
# warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See
# the GNU General Public License for more details.
#
# AUTHOR
# Dave Baxter, Marko Luther 2023

# Parses artisan.pro file.  Format of the .pro file:  Must have SOURCES and TRANSLATION files
# each on its own line.  

import os
import subprocess
import sys

try:
    # read the artisan.pro project file
    with open('artisan.pro', encoding='utf-8') as f:
        file_content = f.read()

    # grab content from SOURCES to a blank line
    print("Looking for sources")
    start:int = file_content.index(r"SOURCES = ") +len("SOURCES = ") +3  #get past the backslash
    end:int = file_content.index("\n\n", start)
    if end == -1:
        end = len(file_content)
    sources:str = [s.strip().rstrip("\\") for s in file_content[start:end].split("\n")]
    # distill to the unique top directories
    #unique_top_dirs:list = set([os.path.split(source)[0] for source in sources])
    unique_top_dirs:list = {os.path.split(source)[0] for source in sources}

    # grab content from TRANSLATIONS to a blank line
    print("Looking for translations")
    start = file_content.find("TRANSLATIONS = ")+len("TRANSLATIONS = ") +3  #get past the backslash
    end = file_content.find("\n\n", start)
    if end == -1:
        end = len(file_content)
    translations:str = [s.rstrip("\\").strip() for s in file_content[start:end].split("\n")]

    # Build a pylupdate6 command line
    cmdline:str = f'pylupdate6 {" ".join(unique_top_dirs)} -ts {" -ts ".join(translations)[:-5]}'
    #print("*** cmdline:  ",cmdline)

    # run the pylupdate6 command line
    completed_process = subprocess.run(cmdline, capture_output=True, text=True, check=False)
    if completed_process.returncode == 0:
        print("*** pylupdate6pro.py completed successfully!")
    else:
        print(f"*** pylupdate6pro.py returned an error: {completed_process.stderr}")
except Exception as e:  # pylint: disable=broad-except
    print("*** pylupdate6pro.py got an exception")
    _, _, exc_tb = sys.exc_info()
    print(str(e),getattr(exc_tb, 'tb_lineno', '?'))
