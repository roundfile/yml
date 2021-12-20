@echo off

:: comandline option LEGACY used to flag a legacy build in NSIS
if "%~1" == "LEGACY"  (set ARTISAN_LEGACY="True") else (set ARTISAN_LEGACY="False")
if "%~1" == "LEGACY"  (set ARTISAN_SPEC=win-legacy) else (set ARTISAN_SPEC=win)
 
:: set the path to pyuic
if "%APPVEYOR%" == "True" (
    set PYTHON_PATH=%PYTHON%
) else (
    set PYTHON_PATH=c:\Python38-64
)
if %ARTISAN_LEGACY% == "True" (
    set PYUIC=%PYTHON_PATH%\scripts\pyuic5.exe
) else (
    set PYUIC=%PYTHON_PATH%\scripts\pyuic6.exe
)

echo PYTHON_PATH %PYTHON_PATH%

:: build the py files from ui files
FOR /R %%a IN (ui\*.ui) DO (
    echo %%~na
    %PYUIC% -o uic\%%~na.py --from-imports ui\%%~na.ui
)

:: convert help files
%PYTHON_PATH%\python.exe ..\doc\help_dialogs\Script\xlsx_to_artisan_help.py all

rem set environment variables for version and build
FOR /F "usebackq delims==" %%a IN (`python -c "import artisanlib; print(artisanlib.__version__)"`) DO (set ARTISAN_VERSION=%%~a)
FOR /F "usebackq delims==" %%a IN (`python -c "import artisanlib; print(artisanlib.__build__)"`) DO (set ARTISAN_BUILD=%%~a)

rem create a version file for pyinstaller
create-version-file version-metadata.yml --outfile version_info-win.txt --version %ARTISAN_VERSION%.%ARTISAN_BUILD%
pyinstaller --noconfirm artisan-%ARTISAN_SPEC%.spec

rem Don't make assumptions as to where the 'makensis.exe' is - look in the obvious places
if exist "C:\Program Files (x86)\NSIS\makensis.exe" set NSIS_EXE="C:\Program Files (x86)\NSIS\makensis.exe"
if exist "C:\Program Files\NSIS\makensis.exe"       set NSIS_EXE="C:\Program Files\NSIS\makensis.exe"
if exist "%ProgramFiles%\NSIS\makensis.exe"         set NSIS_EXE="%ProgramFiles%\NSIS\makensis.exe"
if exist "%ProgramFiles(x86)%\NSIS\makensis.exe"    set NSIS_EXE="%ProgramFiles(x86)%\NSIS\makensis.exe"

rem build the installer
%NSIS_EXE% /DPRODUCT_VERSION=%ARTISAN_VERSION%.%ARTISAN_BUILD% /DLEGACY=%ARTISAN_LEGACY% setup-install3-pi.nsi
