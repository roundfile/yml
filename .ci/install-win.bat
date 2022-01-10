 @echo off
:: the current directory on entry to this script must be the folder above src

echo Appveyor %APPVEYOR%
::
:: script comandline option LEGACY used to flag a legacy build
:: when running locally these paths need to be set here 
::
if "%APPVEYOR%" NEQ "True" (echo How you get up there)
rem if "%APPVEYOR%" NEQ "True" (
rem     if "%~1" == "LEGACY" (
rem         set PYTHON_PATH=c:\Python38-64
rem         set QT_PATH=c:\qt\5.15\msvc2019_64
rem         set PYINSTALLER_VER=4.3
rem         set VC_REDIST=https://download.microsoft.com/download/9/3/F/93FCF1E7-E6A4-478B-96E7-D4B285925B00/vc_redist.x64.exe
rem     ) else (
rem         set PYTHON_PATH=c:\Python310-64
rem         set QT_PATH=c:\qt\6.2\msvc2019_64
rem         set PYINSTALLER_VER=4.7
rem         set VC_REDIST=https://aka.ms/vs/17/release/vc_redist.x64.exe
rem     )
rem )
:: path already updated in the Appveyor environment
if "%APPVEYOR%" NEQ "True" (
    set PATH=%PYTHON_PATH%;%PYTHON_PATH%\Scripts;%PATH%
)

echo Python Version
python -V

%PYTHON_PATH%\python.exe -m pip install --upgrade pip
%PYTHON_PATH%\python.exe -m pip install wheel

%PYTHON_PATH%\\python.exe -m pip install .ci\\pyinstaller-%PYINSTALLER_VER%-py3-none-any.whl
:: build the pyinstaller bootloader and install
rem curl -L -O https://github.com/pyinstaller/pyinstaller/archive/refs/tags/v%PYINSTALLER_VER%.zip
rem 7z x v%PYINSTALLER_VER%.zip
rem del v%PYINSTALLER_VER%.zip
rem cd pyinstaller-%PYINSTALLER_VER%\bootloader
rem %PYTHON_PATH%\python.exe ./waf all --target-arch=64bit
rem cd ..
rem %PYTHON_PATH%\python.exe setup.py -q install
rem cd ..
:: end: build the pyinstaller bootloader and install

%PYTHON_PATH%\python.exe -m pip install -r src\\requirements.txt
%PYTHON_PATH%\python.exe -m pip install -r src\\requirements-%ARTISAN_SPEC%.txt
echo curl vc_redist.x64.exe
curl -L -O %VC_REDIST%
echo curl snap7
curl -k -L -O https://netcologne.dl.sourceforge.net/project/snap7/1.4.2/snap7-full-1.4.2.7z
7z x snap7-full-1.4.2.7z
copy snap7-full-1.4.2\build\bin\win64\snap7.dll c:\windows
echo curl libusb-win32
curl -k -L -O https://netcologne.dl.sourceforge.net/project/libusb-win32/libusb-win32-releases/1.2.6.0/libusb-win32-bin-1.2.6.0.zip
7z x libusb-win32-bin-1.2.6.0.zip
copy libusb-win32-bin-1.2.6.0\bin\amd64\libusb0.dll C:\Windows\SysWOW64

 