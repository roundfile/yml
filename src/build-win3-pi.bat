@echo off
:: on entry to this script the current path must be the src folder

::
:: comandline option LEGACY used to flag a legacy build
:: when running locally these paths need to be set here 
::
if "%APPVEYOR%" NEQ "True" (
    if "%~1" == "LEGACY" (
        set PYTHON_PATH=c:\Python38-64
        set ARTISAN_SPEC=win-legacy
        set PYUIC=%PYTHON_PATH%\scripts\pyuic5.exe
        set QT_PATH=c:\qt\5.15\msvc2019_64
    ) else (
        set PYTHON_PATH=c:\Python310-64
        set ARTISAN_SPEC=win
        set PYUIC=%PYTHON_PATH%\scripts\pyuic6.exe
        set QT_PATH=c:\qt\6.2\msvc2019_64
    )
)
set PATH=%PYTHON_PATH%;%PYTHON_PATH%\Scripts;%PATH%
 
::
:: convert ui files to py files
::
FOR /R %%a IN (ui\*.ui) DO (
    echo %%~na
    %PYUIC% -o uic\%%~na.py --from-imports ui\%%~na.ui
)

::
:: convert help files from .xlsx to .py
::
%PYTHON_PATH%\python.exe ..\doc\help_dialogs\Script\xlsx_to_artisan_help.py all

::
:: Process translation files
::
call "C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\VC\Auxiliary\Build\vcvarsall.bat" x86_amd64
echo *****Translating files defined in artisan.pro
%QT_PATH%\bin\lrelease -verbose artisan.pro
echo *****Translating qtbase_*.ts files
FOR /R %%a IN (translations\qtbase_*.ts) DO (
    %QT_PATH%\bin\lrelease -verbose %%~a
)

::
:: run pyinstaller and build the NSIS install .exe
::
:: set environment variables for version and build
FOR /F "usebackq delims==" %%a IN (`python -c "import artisanlib; print(artisanlib.__version__)"`) DO (set ARTISAN_VERSION=%%~a)
FOR /F "usebackq delims==" %%a IN (`python -c "import artisanlib; print(artisanlib.__build__)"`) DO (set ARTISAN_BUILD=%%~a)
::
::dave
path
:: create a version file for pyinstaller
create-version-file version-metadata.yml --outfile version_info-win.txt --version %ARTISAN_VERSION%.%ARTISAN_BUILD%
::
:: run pyinstaller
pyinstaller --noconfirm artisan-%ARTISAN_SPEC%.spec
::
:: Don't make assumptions as to where the 'makensis.exe' is - look in the obvious places
if exist "C:\Program Files (x86)\NSIS\makensis.exe" set NSIS_EXE="C:\Program Files (x86)\NSIS\makensis.exe"
if exist "C:\Program Files\NSIS\makensis.exe"       set NSIS_EXE="C:\Program Files\NSIS\makensis.exe"
if exist "%ProgramFiles%\NSIS\makensis.exe"         set NSIS_EXE="%ProgramFiles%\NSIS\makensis.exe"
if exist "%ProgramFiles(x86)%\NSIS\makensis.exe"    set NSIS_EXE="%ProgramFiles(x86)%\NSIS\makensis.exe"
::
:: run NSIS to build the install .exe file
%NSIS_EXE% /DPRODUCT_VERSION=%ARTISAN_VERSION%.%ARTISAN_BUILD% /DLEGACY=%ARTISAN_LEGACY% setup-install3-pi.nsi
