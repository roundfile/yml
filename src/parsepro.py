import re
import os
import subprocess
import sys

try:
    # read the artisan.pro project file
    with open('artisan.pro') as f:
        file_content = f.read()

    # grab content from SOURCES to a blank line
    print("Looking for sources")
    start = file_content.index(r"SOURCES = ") +len("SOURCES = ") +3  #get past the backslash
    end = file_content.index("\n\n", start)
    if end == -1:
        end = len(file_content)
    sources = [s.strip().rstrip("\\") for s in file_content[start:end].split("\n")]
    # distill to the unique top directories
    unique_top_dirs = set([os.path.split(source)[0] for source in sources])

    # grab content from TRANSLATIONS to a blank line
    print("Looking for translations")
    start = file_content.find("TRANSLATIONS = ")+len("TRANSLATIONS = ") +3  #get past the backslash
    end = file_content.find("\n\n", start)
    if end == -1:
        end = len(file_content)
    translations = [s.rstrip("\\").strip() for s in file_content[start:end].split("\n")]

    # Build a pylupdate6 command line
    cmdline = f'pylupdate6 {" ".join(unique_top_dirs)} -ts {" -ts ".join(translations)[:-5]}'
#    print(cmdline)

    # run the pylupdate6 command line
    completed_process = subprocess.run(cmdline, capture_output=True, text=True)
    if completed_process.returncode == 0:
        print("*** parsepro.py completed successfully!")
        exit(0)
    else:
        print(f"*** parsepro.py returned an error: {completed_process.stderr}")
        exit(1)
except Exception as e:  # pylint: disable=broad-except
    print("*** parsepro.py got an exception")
    print(e)
    _, _, exc_tb = sys.exc_info()
    print(str(e),getattr(exc_tb, 'tb_lineno', '?'))
    exit(1)