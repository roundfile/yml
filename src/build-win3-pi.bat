dir c:\qt\6.2.2
dir c:\qt\6.2.2\tools
exit
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
    set QT_PATH=%PYTHON_PATH%\lib\site-packages\qt5_applications\Qt
) else (
    set PYUIC=%PYTHON_PATH%\scripts\pyuic6.exe
    set QT_PATH=%PYTHON_PATH%\lib\site-packages\qt6_applications\Qt
)

rem echo PYTHON_PATH %PYTHON_PATH%

:: Process trasnlation files
echo *****Exectuting artisan.pro
echo %QT_PATH%
%QT_PATH%\bin\lrelease -verbose artisan.pro
echo *****Done Executing artisan.pro
FOR /R %%a IN (translations\qtbase_*.ts) DO (
    echo *****Translation file %%~a
    %QT_PATH%\bin\lrelease - verbose %%na
)
dir translations\qtbase_*.ts

rem :: build the py files from ui files
rem FOR /R %%a IN (ui\*.ui) DO (
rem     echo %%~na
rem     %PYUIC% -o uic\%%~na.py --from-imports ui\%%~na.ui
rem )
rem 
rem :: convert help files
rem %PYTHON_PATH%\python.exe ..\doc\help_dialogs\Script\xlsx_to_artisan_help.py all
rem 
rem :: set environment variables for version and build
rem FOR /F "usebackq delims==" %%a IN (`python -c "import artisanlib; print(artisanlib.__version__)"`) DO (set ARTISAN_VERSION=%%~a)
rem FOR /F "usebackq delims==" %%a IN (`python -c "import artisanlib; print(artisanlib.__build__)"`) DO (set ARTISAN_BUILD=%%~a)
rem 
rem :: create a version file for pyinstaller
rem create-version-file version-metadata.yml --outfile version_info-win.txt --version %ARTISAN_VERSION%.%ARTISAN_BUILD%
rem pyinstaller --noconfirm artisan-%ARTISAN_SPEC%.spec
rem 
rem :: Don't make assumptions as to where the 'makensis.exe' is - look in the obvious places
rem if exist "C:\Program Files (x86)\NSIS\makensis.exe" set NSIS_EXE="C:\Program Files (x86)\NSIS\makensis.exe"
rem if exist "C:\Program Files\NSIS\makensis.exe"       set NSIS_EXE="C:\Program Files\NSIS\makensis.exe"
rem if exist "%ProgramFiles%\NSIS\makensis.exe"         set NSIS_EXE="%ProgramFiles%\NSIS\makensis.exe"
rem if exist "%ProgramFiles(x86)%\NSIS\makensis.exe"    set NSIS_EXE="%ProgramFiles(x86)%\NSIS\makensis.exe"
rem 
rem :: build the installer
rem %NSIS_EXE% /DPRODUCT_VERSION=%ARTISAN_VERSION%.%ARTISAN_BUILD% /DLEGACY=%ARTISAN_LEGACY% setup-install3-pi.nsi
