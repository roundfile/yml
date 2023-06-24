# ABOUT
# Artisan pyinstaller specification file

# LICENSE
# This program or module is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as published
# by the Free Software Foundation, either version 2 of the License, or
# version 3 of the License, or (at your option) any later version. It is
# provided for educational purposes and is distributed in the hope that
# it will be useful, but WITHOUT ANY WARRANTY; without even the implied
# warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See
# the GNU General Public License for more details.

# AUTHOR
# Marko Luther, 2023

# -*- mode: python -*-

# Function to perform file copy
def copy_file(source_file, destination_file):
    print(source_file)
    copy_command = 'copy "{}" "{}"'.format(source_file, destination_file)
    exit_code = os.system(copy_command)

    if exit_code != 0:
        sys.exit("Fatal Error: Copy operation failed with error code {}.".format(exit_code))

# Function to check if a file exists
def check_file_exists(file_path):
    if not os.path.isfile(file_path):
        sys.exit("Fatal Error: File '{}' does not exist.".format(file_path))

block_cipher = None

import os
if os.environ.get('APPVEYOR'):
  ARTISAN_SRC = r'C:\projects\artisan\src'
  PYTHON = r'c:\python38-x64'
else:
  ARTISAN_SRC = r'C:\Users\roast\Documents\artisan-roaster-scope\src'
  PYTHON = r'C:\Program Files\Python38'
NAME = 'artisan'

QT_TOOLS = os.environ.get('QT_TOOLS')
if QT_TOOLS:
  print("Env QT_TOOLS: %s",QT_TOOLS)
else:
  print("Env QT_TOOLS is not set")


##
TARGET = 'dist\\' + NAME + '\\'
PYTHON_PACKAGES = PYTHON + r'\Lib\site-packages'
PYQT_QT = PYTHON_PACKAGES + r'\PyQt5\Qt'
PYQT_QT_BIN = PYQT_QT + r'\bin'
PYQT_QT_TRANSLATIONS = PYQT_QT + r'\translations'
YOCTO_BIN = PYTHON_PACKAGES + r'\yoctopuce\cdll'
SNAP7_BIN = r'C:\Windows'
LIBUSB_BIN = r'C:\Windows\SysWOW64'

from PyInstaller.utils.hooks import is_module_satisfies
if is_module_satisfies('scipy >= 1.3.2'):
  SCIPY_BIN = PYTHON_PACKAGES + r'\scipy\.libs'
else:
  SCIPY_BIN = PYTHON_PACKAGES + r'\scipy\extra-dll'

#os.system(PYTHON + r'\Scripts\pylupdate5 artisan.pro')

a = Analysis(['artisan.py'],
             pathex=[PYQT_QT_BIN, ARTISAN_SRC, SCIPY_BIN],
             binaries=[],
             datas=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             hiddenimports=['charset_normalizer.md__mypyc', # part of requests 2.28.2 # see https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/534
                            'matplotlib.backends.backend_pdf',
                            'matplotlib.backends.backend_svg',
                            'scipy.spatial.transform._rotation_groups',
                            'scipy.special.cython_special',
                            'scipy._lib.messagestream',
                            'pywintypes',
                            'win32cred',
                            'win32timezone'
                            ],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)

pyz = PYZ(a.pure, a.zipped_data,cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name=NAME,
          debug=False,
          strip=False, # =True fails
          upx=True, # not installed
          icon='artisan.ico',
          version='version_info-win.txt',
          console=False) # was True

coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False, # =True fails
               upx=True, # not installed
               name=NAME)


# assumes the Microsoft Visual C++ 2015 Redistributable Package (x64), vc_redist.x64.exe, is located above the source directory
copy_file(r'..\vc_redist.x64.exe', TARGET)
#os.system(r'copy ..\vc_redist.x64.exe ' + TARGET)

copy_file('README.txt',TARGET)
#os.system('copy README.txt ' + TARGET)
copy_file(r'..\LICENSE', TARGET + r'\LICENSE.txt')
#os.system(r'copy ..\LICENSE ' + TARGET + r'\LICENSE.txt')
#os.system('copy qt-win.conf ' + TARGET + 'qt.conf')
os.system('mkdir ' + TARGET + 'Wheels')
os.system('mkdir ' + TARGET + r'Wheels\Cupping')
os.system('mkdir ' + TARGET + r'Wheels\Other')
os.system('mkdir ' + TARGET + r'Wheels\Roasting')
os.system(r'copy Wheels\Cupping\* ' + TARGET + r'Wheels\Cupping')
os.system(r'copy Wheels\Other\* ' + TARGET + r'Wheels\Other')
os.system(r'copy Wheels\Roasting\* ' + TARGET + r'Wheels\Roasting')

os.system('mkdir ' + TARGET + 'translations')
os.system(r'copy translations\*.qm ' + TARGET + 'translations')
for tr in [
    'qtbase_ar.qm',
    'qtbase_de.qm',
    'qtbase_en.qm',
    'qtbase_es.qm',
    'qtbase_fi.qm',
    'qtbase_fr.qm',
    'qtbase_he.qm',
    'qtbase_hu.qm',
    'qtbase_it.qm',
    'qtbase_ja.qm',
    'qtbase_ko.qm',
    'qtbase_pl.qm',
    'qtbase_uk.qm',
    'qtbase_tr.qm',
    'qtbase_zh_TW.qm',
    ]:
  copy_file(QT_TOOLS + '\\' + tr, TARGET + 'translations')
  #copy_file(PYQT_QT_TRANSLATIONS + '\\' + tr, TARGET + 'translations')
  #os.system(r'copy "' + PYQT_QT_TRANSLATIONS + '\\' + tr + '" ' + TARGET + 'translations')

os.system('rmdir /q /s ' + TARGET + 'mpl-data\\sample_data')
# YOCTO HACK BEGIN: manually copy over the dlls
os.system(r'mkdir ' + TARGET + 'yoctopuce\cdll')
os.system(r'copy "' + YOCTO_BIN + r'\yapi.dll" ' + TARGET + 'yoctopuce\cdll')
os.system(r'copy "' + YOCTO_BIN + r'\yapi64.dll" ' + TARGET + 'yoctopuce\cdll')
# YOCTO HACK END

# copy Snap7 lib
os.system('copy "' + SNAP7_BIN + r'\snap7.dll" ' + TARGET)

# copy libusb0.1 lib

os.system('copy "' + LIBUSB_BIN + r'\libusb0.dll" ' + TARGET)

for fn in [
    'artisan.png',
    'artisanAlarms.ico',
    'artisanProfile.ico',
    'artisanPalettes.ico',
    'artisanTheme.ico',
    'artisanSettings.ico',
    'artisanWheel.ico',
    r'includes\Humor-Sans.ttf',
    r'includes\dijkstra.ttf',
    r'includes\WenQuanYiZenHei-01.ttf',
    r'includes\WenQuanYiZenHeiMonoMedium.ttf',
    r'includes\SourceHanSansCN-Regular.otf',
    r'includes\SourceHanSansHK-Regular.otf',
    r'includes\SourceHanSansJP-Regular.otf',
    r'includes\SourceHanSansKR-Regular.otf',
    r'includes\SourceHanSansTW-Regular.otf',
    r'includes\alarmclock.eot',
    r'includes\alarmclock.svg',
    r'includes\alarmclock.ttf',
    r'includes\alarmclock.woff',
    r'includes\artisan.tpl',
    r'includes\bigtext.js',
    r'includes\sorttable.js',
    r'includes\report-template.htm',
    r'includes\roast-template.htm',
    r'includes\ranking-template.htm',
    r'includes\jquery-1.11.1.min.js',
    r'includes\logging.yaml',
    ]:
  os.system('copy ' + fn + ' ' + TARGET)

os.system(r'mkdir ' +  TARGET + 'Machines')
os.system(r'xcopy includes\Machines ' + TARGET + 'Machines /y /S')

os.system(r'mkdir ' +  TARGET + 'Themes')
os.system(r'xcopy includes\Themes ' + TARGET + 'Themes /y /S')

os.system(r'mkdir ' +  TARGET + 'Icons')
os.system(r'xcopy includes\Icons ' + TARGET + 'Icons /y /S')
