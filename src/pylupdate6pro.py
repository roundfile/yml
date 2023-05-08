# ABOUT
# Qt Translation processing for Artisan
# Parses artisan.pro file.  Format of the .pro file:  Must have SOURCES and TRANSLATION files
# each on its own line.  
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

import os
import subprocess
import sys
from typing import List, Set  #for Python >= 3.9: can remove 'List' since type hints can now use the generic 'list'

try:
#    print("os.environ: ",os.environ)
#    scriptdir = os.environ['PYTHON_PATH']
#    print("Script dir: ",scriptdir)

    # read the artisan.pro project file
    with open('artisan.pro', encoding='utf-8') as f:
        file_content = f.read()

    # grab content from SOURCES to a blank line
    print("Looking for sources")
    start:int = file_content.index(r"SOURCES = ") +len("SOURCES = ") +3  #get past the backslash
    end:int = file_content.find("\n\n", start)  #find will not raise an exception if it runs to the end of the file
    if end == -1:
        end = len(file_content)
    sources:List[str] = [s.strip().rstrip("\\") for s in file_content[start:end].split("\n")]
    # distill to the unique top directories
    #unique_top_dirs:list = set([os.path.split(source)[0] for source in sources])
    unique_top_dirs:Set[str] = {os.path.split(source)[0] for source in sources}

    # grab content from TRANSLATIONS to a blank line
    print("Looking for translations")
    start = file_content.index("TRANSLATIONS = ")+len("TRANSLATIONS = ") +3  #get past the backslash
    end = file_content.find("\n\n", start)  #find will not raise an exception if it runs to the end of the file
    if end == -1:
        end = len(file_content)
    translations: List[str] = [s.rstrip("\\").strip() for s in file_content[start:end].split("\n")[:-1]]
#    translated_strings: List[str] = []
#    for t in translations:
#        translated_strings.extend(['--ts', t])
#    print("translated_strings: ",translated_strings)

    cmdline:List[str] = ['pylupdate6']
    cmdline.extend(unique_top_dirs)
    #combined_list.extend(translations)
    for t in translations:
        cmdline.extend(['--ts', t])
    
    # Build a pylupdate6 command line
#    cmdline:str = f'{scriptdir}/bin/pylupdate6 {" ".join(unique_top_dirs)} -ts {" -ts ".join(translations)[:-5]}'
    print("*** cmdline:  ",cmdline)


#    #cmdline = [f'{scriptdir}/bin/pylupdate6', 'artisanlib', '--ts', 'translations/artisan_ar.ts']
#    cmdline = ['pylupdate6', 'artisanlib', '--ts', 'translations/artisan_ar.ts']
    completed_process = subprocess.run(cmdline, capture_output=True, text=True, check=False)



    # run the pylupdate6 command line
    completed_process = subprocess.run(cmdline, capture_output=True, text=True, check=False)

    # prints to make entries in the Appveyor log (or on the console))
    if completed_process.returncode == 0:
        print("*** pylupdate6pro.py completed successfully!")
        sys.exit(0)
    else:
        print(f"*** pylupdate6pro.py returned an error: {completed_process.stderr}")
#        sys.exit(1)
except Exception as e:   #pylint: disable=broad-except
    print("*** pylupdate6pro.py got an exception")
    print(f"{e} line:{sys.exc_info()[2].tb_lineno}") #type: ignore
    sys.exit(1)
