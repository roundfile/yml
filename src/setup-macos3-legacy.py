"""This is a setup.py script generated by py2applet

Usage:
    python3 setup-mac3.py py2app
"""

# manually remove sample-data mpl subdirectory from Python installation:
# sudo rm -rf /Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages/matplotlib/mpl-data/sample_data

# THIS PATCH SEEMS NOT TO BE NEEDED ANYMORE:
#from distutils import sysconfig
#their_parse_makefile = sysconfig.parse_makefile
#def my_parse_makefile(filename, g):
#    their_parse_makefile(filename, g)
#    g['MACOSX_DEPLOYMENT_TARGET'] = os.environ['MACOSX_DEPLOYMENT_TARGET']
#sysconfig.parse_makefile = my_parse_makefile

import os
import sys
import subprocess
from setuptools import setup

import plistlib

import artisanlib

# current version of artisan
VERSION = artisanlib.__version__
LICENSE = 'GNU General Public License (GPL)'

QTDIR = os.environ['QT_PATH'] + r'/'

APP = ['artisan.py']

DATA_FILES = [
# standard QT translation needed to get the Application menu bar and
# the standard dialog elements translated
    ('../translations', [QTDIR + r'/translations/qtbase_ar.qm']),
    ('../translations', [QTDIR + r'/translations/qtbase_de.qm']),
    ('../translations', [QTDIR + r'/translations/qtbase_en.qm']),
    ('../translations', [QTDIR + r'/translations/qtbase_es.qm']),
    ('../translations', [QTDIR + r'/translations/qtbase_fi.qm']),
    ('../translations', [QTDIR + r'/translations/qtbase_fr.qm']),
    ('../translations', [QTDIR + r'/translations/qtbase_he.qm']),
    ('../translations', [QTDIR + r'/translations/qtbase_hu.qm']),
    ('../translations', [QTDIR + r'/translations/qtbase_it.qm']),
    ('../translations', [QTDIR + r'/translations/qtbase_ja.qm']),
    ('../translations', [QTDIR + r'/translations/qtbase_ko.qm']),
#    ("../translations", [QTDIR + r'/translations/qtbase_pt.qm']),    # empty/missing
    ('../translations', [QTDIR + r'/translations/qtbase_pl.qm']),
#    ("../translations", [QTDIR + r'/translations/qtbase_ru.qm']),
    ('../translations', [QTDIR + r'/translations/qtbase_uk.qm']),
#    ("../translations", [QTDIR + r'/translations/qtbase_sv.qm']),    # empty/missing
    ('../translations', [QTDIR + r'/translations/qtbase_tr.qm']),     # new in Qt 5.15.2
#    ("../translations", [QTDIR + r'/translations/qtbase_zh_CN.qm']), # empty/missing
    ('../translations', [QTDIR + r'/translations/qtbase_zh_TW.qm']),
    ('../translations', [r'translations/artisan_ar.qm']),
    ('../translations', [r'translations/artisan_de.qm']),
    ('../translations', [r'translations/artisan_el.qm']),
    ('../translations', [r'translations/artisan_es.qm']),
    ('../translations', [r'translations/artisan_fa.qm']),
    ('../translations', [r'translations/artisan_fi.qm']),
    ('../translations', [r'translations/artisan_fr.qm']),
    ('../translations', [r'translations/artisan_he.qm']),
    ('../translations', [r'translations/artisan_hu.qm']),
    ('../translations', [r'translations/artisan_id.qm']),
    ('../translations', [r'translations/artisan_it.qm']),
    ('../translations', [r'translations/artisan_ja.qm']),
    ('../translations', [r'translations/artisan_ko.qm']),
    ('../translations', [r'translations/artisan_pt.qm']),
    ('../translations', [r'translations/artisan_pt_BR.qm']),
    ('../translations', [r'translations/artisan_pl.qm']),
#    ("../translations", [r'translations/artisan_ru.qm']),
    ('../translations', [r'translations/artisan_uk.qm']),
    ('../translations', [r'translations/artisan_sv.qm']),
    ('../translations', [r'translations/artisan_no.qm']),
    ('../translations', [r'translations/artisan_nl.qm']),
    ('../translations', [r'translations/artisan_th.qm']),
    ('../translations', [r'translations/artisan_tr.qm']),
    ('../translations', [r'translations/artisan_vi.qm']),
    ('../translations', [r'translations/artisan_zh_CN.qm']),
    ('../translations', [r'translations/artisan_zh_TW.qm']),
    ('../translations', [r'translations/qtbase_da.qm']), # from Qt 6.1
    ('../translations', [r'translations/qtbase_el.qm']), # unfinished translations from https://code.qt.io/cgit/qt/qttranslations.git/
    ('../translations', [r'translations/qtbase_fa.qm']), # unfinished translations from https://code.qt.io/cgit/qt/qttranslations.git/
    ('../translations', [r'translations/qtbase_gd.qm']), # from Qt 6.1
    ('../translations', [r'translations/qtbase_lv.qm']), # from Qt 6.1
    ('../translations', [r'translations/qtbase_nl.qm']), # unfinished translations from https://code.qt.io/cgit/qt/qttranslations.git/
    ('../translations', [r'translations/qtbase_pt.qm']), # unfinished translations from https://code.qt.io/cgit/qt/qttranslations.git/
    ('../translations', [r'translations/qtbase_sk.qm']), # from Qt 6.1
    ('../translations', [r'translations/qtbase_pt_BR.qm']), # from Qt 6.1
    ('../translations', [r'translations/qtbase_sv.qm']), # unfinished translations from https://code.qt.io/cgit/qt/qttranslations.git/
    ('../translations', [r'translations/qtbase_zh_CN.qm']), # from Qt 6.1
#    ("../Resources", [r"qt.conf"]), # uncomment in QT Framework variant
    ('../Resources', [r'artisanProfile.icns']),
    ('../Resources', [r'artisanAlarms.icns']),
    ('../Resources', [r'artisanPalettes.icns']),
    ('../Resources', [r'artisanSettings.icns']),
    ('../Resources', [r'artisanTheme.icns']),
    ('../Resources', [r'artisanWheel.icns']),
    ('../Resources', [r'includes/alarmclock.eot']),
    ('../Resources', [r'includes/alarmclock.svg']),
    ('../Resources', [r'includes/alarmclock.ttf']),
    ('../Resources', [r'includes/alarmclock.woff']),
    ('../Resources', [r'includes/artisan.tpl']),
    ('../Resources', [r'includes/bigtext.js']),
    ('../Resources', [r'includes/sorttable.js']),
    ('../Resources', [r'includes/report-template.htm']),
    ('../Resources', [r'includes/roast-template.htm']),
    ('../Resources', [r'includes/ranking-template.htm']),
    ('../Resources', [r'includes/Humor-Sans.ttf']),
    ('../Resources', [r'includes/WenQuanYiZenHei-01.ttf']),
    ('../Resources', [r'includes/WenQuanYiZenHeiMonoMedium.ttf']),
    ('../Resources', [r'includes/SourceHanSansCN-Regular.otf']),
    ('../Resources', [r'includes/SourceHanSansHK-Regular.otf']),
    ('../Resources', [r'includes/SourceHanSansJP-Regular.otf']),
    ('../Resources', [r'includes/SourceHanSansKR-Regular.otf']),
    ('../Resources', [r'includes/SourceHanSansTW-Regular.otf']),
    ('../Resources', [r'includes/dijkstra.ttf']),
    ('../Resources', [r'includes/ComicNeue-Regular.ttf']),
    ('../Resources', [r'includes/xkcd-script.ttf']),
    ('../Resources', [r'includes/jquery-1.11.1.min.js']),
    ('../Resources', [r'includes/android-chrome-192x192.png']),
    ('../Resources', [r'includes/android-chrome-512x512.png']),
    ('../Resources', [r'includes/apple-touch-icon.png']),
    ('../Resources', [r'includes/browserconfig.xml']),
    ('../Resources', [r'includes/favicon-16x16.png']),
    ('../Resources', [r'includes/favicon-32x32.png']),
    ('../Resources', [r'includes/favicon.ico']),
    ('../Resources', [r'includes/mstile-150x150.png']),
    ('../Resources', [r'includes/safari-pinned-tab.svg']),
    ('../Resources', [r'includes/site.webmanifest']),
    ('../Resources', [r'includes/Machines']),
    ('../Resources', [r'includes/Themes']),
    ('../Resources', [r'includes/Icons']),
    ('../Resources', [r'includes/logging.yaml']),
  ]

with open('Info.plist', 'r+b') as fp:
    plist = plistlib.load(fp)
    plist['CFBundleDisplayName'] = 'Artisan'
    plist['CFBundleGetInfoString'] = 'Artisan, Roast Logger'
    plist['CFBundleIdentifier'] = 'org.artisan-scope.artisan'
    plist['CFBundleShortVersionString'] = VERSION
    plist['CFBundleVersion'] = 'Artisan ' + VERSION
    plist['LSMinimumSystemVersion'] = os.environ['MACOSX_DEPLOYMENT_TARGET']
    plist['LSMultipleInstancesProhibited'] = 'false'
#    plist['LSPrefersPPC'] = False # not in use longer
    plist['LSArchitecturePriority'] = ['x86_64']
    plist['NSHumanReadableCopyright'] = LICENSE
    plist['NSHighResolutionCapable'] = True
#    plist['NSRequiresAquaSystemAppearance'] = False # important to activate the automatic dark mode of Qt on OS X 10.14 or later (with linked against macOS before 10.14, like with PyQt 5.13.1
    fp.seek(0, os.SEEK_SET)
    fp.truncate()
    plistlib.dump(plist, fp)

OPTIONS = {
    'strip': True,
#    'xref': True,
    'argv_emulation': False, # this would confuses GUI processing
    'semi_standalone': False,
    'site_packages': True,
    'packages': ['yoctopuce','openpyxl','numpy','scipy','certifi', 'kiwisolver', 'psutil',
        'matplotlib','PIL', 'lxml', 'snap7', 'google.protobuf', 'google._upb', 'keyring.backends'], # MPL and PIL added for mpl v3.3.x
    'optimize':  2,
    'compressed': True,
    'iconfile': 'artisan.icns',
    'arch': 'x86_64',
    'matplotlib_backends': '-', # '-' for imported or explicit "Qt5Agg, PDF, PS, SVG"
    'includes': ['serial'],
    'excludes' :  ['tkinter','curses', # 'sqlite3',
                'test', # don't bundle the Python tests
                'setuptools', # not needed
                ],
    'plist'    : plist}

setup(
    name='Artisan',
    version=VERSION,
    author='YOUcouldbeTOO',
    author_email='zaub.ERASE.org@yahoo.com',
    license=LICENSE,
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app']
)


subprocess.check_call(r'cp README.txt dist',shell = True)
subprocess.check_call(r'cp ../LICENSE dist/LICENSE.txt',shell = True)
subprocess.check_call(r'mkdir dist/Wheels',shell = True)
subprocess.check_call(r'mkdir dist/Wheels/Cupping',shell = True)
subprocess.check_call(r'mkdir dist/Wheels/Other',shell = True)
subprocess.check_call(r'mkdir dist/Wheels/Roasting',shell = True)
subprocess.check_call(r'cp Wheels/Cupping/* dist/Wheels/Cupping',shell = True)
subprocess.check_call(r'cp Wheels/Other/* dist/Wheels/Other',shell = True)
subprocess.check_call(r'cp Wheels/Roasting/* dist/Wheels/Roasting',shell = True)
os.chdir('./dist')

try:
    PYTHONPATH = os.environ['PYTHONPATH'] + r'/'
except Exception: # pylint: disable=broad-except
    PYTHONPATH = r'/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/'

#try:
#    PYTHON_V = os.environ["PYTHON_V"]
#except Exception: # pylint: disable=broad-except
#    PYTHON_V = '3.11'
# (independent) matplotlib (installed via pip) shared libs are not copied by py2app (both cp are needed!)
# UPDATE 9/2020: pip install of MPL v3.3.x does not come with a .dylibs directory any longer
#subprocess.check_call(r'mkdir Artisan.app/Contents/Resources/lib/python' + PYTHON_V + '/lib-dynload/matplotlib/.dylibs',shell = True)
#subprocess.check_call(r'cp -R ' + PYTHONPATH + r'site-packages/matplotlib/.dylibs/* Artisan.app/Contents/Resources/lib/python' + PYTHON_V + '/lib-dynload/#matplotlib/.dylibs',shell = True)
#subprocess.check_call(r'cp ' + PYTHONPATH + r'site-packages/matplotlib/.dylibs/* Artisan.app/Contents/Frameworks',shell = True)

# copy snap7 dylib (we try both directories)
try:
    subprocess.check_call(r'cp -f /usr/local/lib/libsnap7.dylib Artisan.app/Contents/Frameworks/libsnap7.dylib',shell = True)
except Exception: # pylint: disable=broad-except
    subprocess.check_call(r'cp -f /usr/lib/libsnap7.dylib Artisan.app/Contents/Frameworks/libsnap7.dylib',shell = True)

# add localization stubs to make OS X translate the systems menu item and native dialogs
for lang in ['ar', 'da', 'de','el','en','es','fa','fi','fr','gd', 'he','hu','id','it','ja','ko','lv', 'nl','no','pl','pt_BR','pt','ru','sk', 'sv','th','tr','vi','zh_CN','zh_TW']:
    loc_dir = r'Artisan.app/Contents/Resources/' + lang + r'.lproj'
    subprocess.check_call(r'mkdir ' + loc_dir,shell = True)
    subprocess.check_call(r'touch ' + loc_dir + r'/Localizable.string',shell = True)



# copy brew installed libusb (note the slight name change of the dylib!)
    # cannot be run brew as root thus the following does not work
    # subprocess.check_call(r'cp $(brew list libusb | grep libusb-1.0.0.dylib) Artisan.app/Contents/Frameworks/libusb-1.0.dylib',shell = True)

# you need to do a
#
#  # brew install libusb
#
# to get libusb installed
try:
    subprocess.check_call(r'cp /usr/local/Cellar/libusb/1.0.27/lib/libusb-1.0.0.dylib Artisan.app/Contents/Frameworks/libusb-1.0.dylib',shell = True)
except Exception: # pylint: disable=broad-except
    try:
        subprocess.check_call(r'cp /usr/local/Cellar/libusb/1.0.26/lib/libusb-1.0.0.dylib Artisan.app/Contents/Frameworks/libusb-1.0.dylib',shell = True)
    except Exception: # pylint: disable=broad-except
        try:
            subprocess.check_call(r'cp /usr/local/Cellar/libusb/1.0.25/lib/libusb-1.0.0.dylib Artisan.app/Contents/Frameworks/libusb-1.0.dylib',shell = True)
        except Exception: # pylint: disable=broad-except
            try:
                subprocess.check_call(r'cp /usr/local/Cellar/libusb/1.0.24/lib/libusb-1.0.0.dylib Artisan.app/Contents/Frameworks/libusb-1.0.dylib',shell = True)
            except Exception: # pylint: disable=broad-except
                print('ERROR: failed to locate libusb')
                sys.exit(1)



# for Qt
print('*** Removing unused Qt frameworks ***')

# QT modules to keep frameworks:
Qt_modules = [
    'QtCore',
    'QtGui',
    'QtWidgets',
    'QtSvg',
    'QtPrintSupport',
    'QtNetwork',
    'QtDBus',
#    'QtBluetooth', # replaced by bleak
    'QtConcurrent', # not on PyQt6
# needed for QtWebEngine HTML2PDF export:
    'QtWebEngineWidgets',
    'QtWebEngineCore',
    'QtWebEngine', # not on PyQt6
    'QtQuick',
    'QtQuickWidgets',
    'QtQml',
    'QtQmlModels',
    'QtWebChannel',
    'QtPositioning',
    'QtOpenGL' # required by QtWebEngineCore
]
Qt_frameworks = [module + '.framework' for module in Qt_modules]

qt_plugin_dirs = [
    'iconengines',
    'imageformats',
    'platforms',
    'printsupport',
    'styles'
]

qt_plugin_files = [
    'libqsvgicon.dylib', # needed to render MPL toolbar as SVG icons (fallback is PNG; built-in support)
#    'libqgif.dylib',
#    'libqicns.dylib',
#    'libqico.dylib',
    'libqjpeg.dylib',
#    'libqmacjp2.dylib',
#    'libqpdf.dylib',
	'libqsvg.dylib',
#    'libqtga.dylib',
#   'libqtiff.dylib',
#    'libqwbmp.dylib',
#    'libqwebp.dylib',
    'libqcocoa.dylib',
    'libcocoaprintersupport.dylib',
    'libqmacstyle.dylib'
]


# remove unused Qt frameworks libs (not in Qt_modules_frameworks)
for subdir, dirs, _files in os.walk('./Artisan.app/Contents/Frameworks'):
    for di in dirs:
        if di.startswith('Qt') and di.endswith('.framework') and di not in Qt_frameworks:
            file_path = os.path.join(subdir, di)
            print(f'rm -rf {file_path}')
            subprocess.check_call(f'rm -rf {file_path}',shell = True)


# remove duplicate Qt plugins folder
# (py2app v0.26.1 copes non-relocated PlugIns to the toplevel)
try:
    subprocess.check_call('rm -rf ./Artisan.app/Contents/plugins',shell = True)
except Exception: # pylint: disable=broad-except
    pass


for python_version in ['python3.8', 'python3.9', 'python3.10', 'python3.11']:
    rootdir = f'./Artisan.app/Contents/Resources/lib/{python_version}'

    if os.path.isdir(f'{rootdir}/PyQt6'):
        # if PyQt6 exists we remove PyQt5 completely
        try:
            subprocess.check_call(f'rm -rf {rootdir}/PyQt5',shell = True)
        except Exception: # pylint: disable=broad-except
            pass
    # remove Qt artefacts
    for qt_dir in [
            'PyQt5/Qt',
            'PyQt5/bindings',
            'PyQt5/uic',
            'PyQt5/Qt5/translations',
            'PyQt5/Qt5/qml',
            'PyQt5/Qt5/qsci',
#            "PyQt5/Qt5/lib", # comment for the non-Framework variant
            'PyQt6/Qt',
            'PyQt6/bindings',
            'PyQt6/lupdate',
            'PyQt6/uic',
            'PyQt6/Qt6/translations',
            'PyQt6/Qt6/qml'
            'PyQt6/Qt6/qsci',
#            "PyQt6/Qt6/lib", # comment for the non-Framework variant
        ]:
        try:
            subprocess.check_call(f'rm -rf {rootdir}/{qt_dir}',shell = True)
        except Exception: # pylint: disable=broad-except
            pass
    for pyqt_dir in ['PyQt5', 'PyQt6']:
        # remove unused PyQt libs (not in Qt_modules)
        for subdir, _dirs, files in os.walk(f'{rootdir}/{pyqt_dir}'):
            for file in files:
                if file.endswith('.pyi'):
                    file_path = os.path.join(subdir, file)
                    subprocess.check_call(f'rm -rf {file_path}',shell = True)
                if file.endswith(('.abi3.so', '.pyi')) and file.split('.')[0] not in Qt_modules:
                    file_path = os.path.join(subdir, file)
                    subprocess.check_call(f'rm -rf {file_path}',shell = True)

# uncomment for non-Framework variant
    # remove unused Qt frameworks libs (not in Qt_modules_frameworks)
    for qt_dir in ['PyQt5/Qt5/lib', 'PyQt6/Qt6/lib']:
        qt = f'{rootdir}/{qt_dir}'
        for _root, dirs, _files in os.walk(qt):
            for di in dirs:
                if di.startswith('Qt') and di.endswith('.framework') and di not in Qt_frameworks:
                    file_path = os.path.join(qt, di)
                    subprocess.check_call(f'rm -rf {file_path}',shell = True)

    # remove unused plugins
    for qt_dir in ['PyQt5/Qt5/plugins', 'PyQt6/Qt6/plugins']:
        for root, dirs, _ in os.walk(f'{rootdir}/{qt_dir}'):
            for d in dirs:
                if d not in qt_plugin_dirs:
                    subprocess.check_call('rm -rf ' + os.path.join(root,d),shell = True)
                else:
                    for subdir, _, files in os.walk(os.path.join(root,d)):
                        for file in files:
                            if file not in qt_plugin_files:
                                file_path = os.path.join(subdir, file)
                                subprocess.check_call(f'rm -rf {file_path}',shell = True)
# comment for non-Framework variant
#        # move plugins directory from Resources/lib/python3.x/PyQtX/QtX/plugins to the root of the app
#        try:
#            shutil.move(f"{rootdir}/{qt_dir}", "./Artisan.app/Contents/PlugIns")
#        except Exception: # pylint: disable=broad-except
#            pass


# remove duplicate mpl_data folder
try:
    subprocess.check_call('rm -rf ./Artisan.app/Contents/Resources/mpl-data',shell = True)
except Exception: # pylint: disable=broad-except
    pass
try:
    subprocess.check_call(f'rm -rf ./Artisan.app/Contents/Resources/lib/{python_version}/matplotlib/mpl-data/sample_data',shell = True)
except Exception: # pylint: disable=broad-except
    pass

print('*** Removing unused files ***')
for root, dirs, files in os.walk('.'):
    for file in files:
        if 'debug' in file:
#            print('Deleting', file)
            os.remove(os.path.join(root,file))
        elif file.startswith('test_'):
#            print('Deleting', file)
            os.remove(os.path.join(root,file))
        elif file.endswith('.pyc') and file != 'site.pyc' and os.path.isfile(os.path.join(root,file[:-3] + 'pyo')):
#            print('Deleting', file)
            os.remove(os.path.join(root,file))
        # remove also all .h .in .cpp .cc .html files
        elif file.endswith('.h') and file != 'pyconfig.h':
#            print('Deleting', file)
            os.remove(os.path.join(root,file))
        elif file.endswith('.in'):
#            print('Deleting', file)
            os.remove(os.path.join(root,file))
        elif file.endswith('.cpp'):
#            print('Deleting', file)
            os.remove(os.path.join(root,file))
        elif file.endswith('.cc'):
#            print('Deleting', file)
            os.remove(os.path.join(root,file))
# .afm files should not be removed as without matplotlib will fail on startup
#        elif file.endswith('.afm'):
#            print('Deleting', file)
#            os.remove(os.path.join(root,file))
    # remove test files
    for di in dirs:
        if 'tests' in di:
            for r,_d,f in os.walk(os.path.join(root,di)):
                for fl in f:
#                    print('Deleting', os.path.join(r,fl))
                    os.remove(os.path.join(r,fl))

os.chdir('..')
subprocess.check_call(r'rm -f artisan-mac-' + VERSION + r'.dmg',shell = True)
subprocess.check_call(r'hdiutil create artisan-mac-' + VERSION + r'.dmg -volname "artisan" -fs HFS+ -srcfolder "dist"',shell = True)
# otool -L dist/Artisan.app/Contents/MacOS/Artisan
