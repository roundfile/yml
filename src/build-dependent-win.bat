::
:: Generate translation, ui, and help files dependent on repository sources
::

:: convert help files from .xlsx to .py
echo ************* help files **************
python ..\doc\help_dialogs\Script\xlsx_to_artisan_help.py all
if ERRORLEVEL 1 (exit /b 1) else (echo ** Success)

:: convert .ui files to .py files
echo ************* ui/uic **************
for /r %%a IN (ui\*.ui) DO (
    #echo %%~na
    %PYUIC% -o uic\%%~na.py ui\%%~na.ui
    if ERRORLEVEL 1 (exit /b 1)
)
echo ** Success
 
:: Process translation files
call "C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\VC\Auxiliary\Build\vcvarsall.bat" x86_amd64
echo ************* pylupdate **************
if /i "%ARTISAN_LEGACY%" == "True" (
    echo *** Processing translation files defined in artisan.pro with pylupdate5.py
    %PYTHON_PATH%\Scripts\pylupdate5.exe artisan.pro
    if ERRORLEVEL 1 (exit /b 1) else (echo ** Success)
) else (
    echo *** Processing translation files with pylupdate6pro.py
    python pylupdate6pro.py
    if ERRORLEVEL 1 (exit /b 1) else (echo ** Success)
)
echo ************* lrelease **************
echo *** Processing artisan.pro
%QT_PATH%\bin\lrelease -verbose artisan.pro
if ERRORLEVEL 1 (exit /b 1) else (echo ** Success)
echo *** Processing translation qtbase_*.ts files
for /r %%a IN (translations\qtbase_*.ts) DO (
    %QT_PATH%\bin\lrelease -verbose %%~a
    if ERRORLEVEL 1 (exit /b 1)
)
echo ** Success

:: Zip the generated files
7z a ..\generated-%ARTISAN_SPEC%.zip ..\doc\help_dialogs\Output_html\ help\ translations\ uic\
if ERRORLEVEL 1 (exit /b 1) else (echo ** Success)
::
::  End of generating dependent files
::
