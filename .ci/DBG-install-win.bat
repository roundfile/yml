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

set PYINSTALLER_VER=5.6.2
::
:: custom build the pyinstaller bootloader or install a prebuilt
::
echo ***** VSWhere
"C:\Program Files (x86)\Microsoft Visual Studio\Installer\vswhere.exe"
:: MSVC
:: C:\Program Files\Microsoft Visual Studio\2022\Community\VC\Tools\MSVC\14.34.31933\bin\HostX64\x64\CL.exe 

echo ***** set
set
rem dir "C:\Program Files\Microsoft Visual Studio\2022\Community\VC\Tools\MSVC\14.34.31933\bin\HostX64\x64"
:: ['C:\\Program Files (x86)\\Microsoft Visual Studio\\Installer\\vswhere.exe', '-products', '*', '-legacy', '-format', 'json']
rem dir "C:\Program Files (x86)"
rem dir "C:\Program Files (x86)\Microsoft Visual Studio\Installer"

rem exit /b 99

echo ***** Start build pyinstaller v%PYINSTALLER_VER%
if not exist pyinstaller-%PYINSTALLER_VER%\bootloader\ (exit /b 101)
cd pyinstaller-%PYINSTALLER_VER%\bootloader

echo ***** Running WAF
%PYTHON_PATH%\python.exe ./waf all --target-arch=64bit  --check-c-compiler=msvc -vvv
echo ***** Echo Log
dir C:\projects\yml\pyinstaller-%PYINSTALLER_VER%\bootloader\build
type C:\projects\yml\pyinstaller-%PYINSTALLER_VER%\bootloader\build\config.log
cd ..

echo ***** Building Wheel
%PYTHON_PATH%\python.exe setup.py -q bdist_wheel
if not exist dist\\pyinstaller-%PYINSTALLER_VER%-py3-none-any.whl (exit /b 102)

echo ***** Finished build pyinstaller v%PYINSTALLER_VER%

echo ***** Start install pyinstaller v%PYINSTALLER_VER%
%PYTHON_PATH%\python.exe -m pip install -q dist\\pyinstaller-%PYINSTALLER_VER%-py3-none-any.whl
cd ..

echo ***** Finished installing pyinstaller v%PYINSTALLER_VER%



rem 
rem if /i "%BUILD_PYINSTALLER%"=="True" (
rem     echo ***** Start build pyinstaller v%PYINSTALLER_VER%
rem     ::
rem     :: download pyinstaller source
rem     echo ***** curl pyinstaller v%PYINSTALLER_VER%
rem     curl -L -O https://github.com/pyinstaller/pyinstaller/archive/refs/tags/v%PYINSTALLER_VER%.zip
rem     if not exist v%PYINSTALLER_VER%.zip (exit /b 100)
rem     7z x v%PYINSTALLER_VER%.zip
rem     del v%PYINSTALLER_VER%.zip
rem     if not exist pyinstaller-%PYINSTALLER_VER%\bootloader\ (exit /b 101)
rem     cd pyinstaller-%PYINSTALLER_VER%\bootloader
rem     ::
rem     :: build the bootlaoder and wheel
rem     echo ***** Running WAF
rem     %PYTHON_PATH%\python.exe ./waf all --target-arch=64bit  :: --check-c-compiler=msvc -vvv
rem     type C:\projects\yml\pyinstaller-5.7.0\bootloader\build\config.log
rem     cd ..
rem     echo ***** Building Wheel
rem     %PYTHON_PATH%\python.exe setup.py -q bdist_wheel
rem     if not exist dist\\pyinstaller-%PYINSTALLER_VER%-py3-none-any.whl (exit /b 102)
rem     echo ***** Finished build pyinstaller v%PYINSTALLER_VER%
rem     ::
rem     :: install pyinstaller
rem     echo ***** Start install pyinstaller v%PYINSTALLER_VER%
rem     %PYTHON_PATH%\python.exe -m pip install -q dist\\pyinstaller-%PYINSTALLER_VER%-py3-none-any.whl
rem     cd ..
rem )
rem 
rem echo ***** Finished installing pyinstaller v%PYINSTALLER_VER%
