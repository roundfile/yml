@echo off
:: the current directory on entry to this script must be the folder above src
::
:: script comandline option LEGACY used to flag a legacy build
::

:: ----------------------------------------------------------------------
:: normally these paths are set in appveyor.yml
:: when running locally these paths must be set here 
:: CAUTION: the paths in this section are not gurantted to be to date!! 
:: ----------------------------------------------------------------------
setlocal enabledelayedexpansion

echo Python Version
%PYTHON_PATH%\python -V

set PYINSTALLER_VER=5.7.0
::
:: custom build the pyinstaller bootloader or install a prebuilt
::
if /i "%BUILD_PYINSTALLER%"=="True" (
    echo ***** Start build pyinstaller v%PYINSTALLER_VER%
    ::
    :: download pyinstaller source
    echo ***** curl pyinstaller v%PYINSTALLER_VER%
    curl -L -O https://github.com/pyinstaller/pyinstaller/archive/refs/tags/v%PYINSTALLER_VER%.zip
    if not exist v%PYINSTALLER_VER%.zip (exit /b 100)
    7z x v%PYINSTALLER_VER%.zip
    del v%PYINSTALLER_VER%.zip
    if not exist pyinstaller-%PYINSTALLER_VER%\bootloader\ (exit /b 101)
    cd pyinstaller-%PYINSTALLER_VER%\bootloader
    ::
    :: build the bootlaoder and wheel
    echo ***** Running WAF
    %PYTHON_PATH%\python.exe ./waf all --target-arch=64bit  :: --check-c-compiler=msvc -vvv
    type C:\projects\yml\pyinstaller-5.7.0\bootloader\build\config.log
    cd ..
    echo ***** Building Wheel
    %PYTHON_PATH%\python.exe setup.py -q bdist_wheel
    if not exist dist\\pyinstaller-%PYINSTALLER_VER%-py3-none-any.whl (exit /b 102)
    echo ***** Finished build pyinstaller v%PYINSTALLER_VER%
    ::
    :: install pyinstaller
    echo ***** Start install pyinstaller v%PYINSTALLER_VER%
    %PYTHON_PATH%\python.exe -m pip install -q dist\\pyinstaller-%PYINSTALLER_VER%-py3-none-any.whl
    cd ..
)

echo ***** Finished installing pyinstaller v%PYINSTALLER_VER%
