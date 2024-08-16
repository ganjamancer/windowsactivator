@echo off
setlocal enabledelayedexpansion

:: Licenses
set "license_1=TX9XD-98N7V-6WMQ6-BX7FG-H8Q99"
set "license_2=3KHY7-WNT83-DGQKR-F7HPR-844BM"
set "license_3=7HNRX-D7KGG-3K4RQ-4WPJ4-YTDFH"
set "license_4=PVMJN-6DFY6–9CCP6–7BKTT-D3WVR"
set "license_5=W269N-WFGWX-YVC9B-4J6C9-T83GX"
set "license_6=MH37W-N47XK-V7XM9-C7227-GCQG9"
set "license_7=NW6C2-QMPVW-D7KKK-3GKT6-VCFB2"
set "license_8=2WH4N-8QGBV-H22JP-CT43Q-MDWWJ"
set "license_9=NPPR9-FWDCX-D2C8J-H872K-2YT43"
set "license_10=DPH2V-TTNVB-4X9Q3-TJR4H-KHJW4"

echo Please share this repo!
echo https://github.com/ganjamancer/windowsactivator/
echo.

:: Select version
echo Please select your version:
echo(
echo (1) Home
echo (2) Home N
echo (3) Home Single Language
echo (4) Home Country Specific
echo (5) Pro
echo (6) Pro N
echo (7) Educational
echo (8) Educational N
echo (9) Enterprise
echo (10) Enterprise N
echo.
set /p vs="Pick your version (1-10): "

:: Apply license
set "license_var=license_%vs%"
if defined !license_var! (
    slmgr /ipk !%license_var%!
    timeout /t 1 >nul
    echo Verifying the license...
    slmgr /skms kms8.msguides.com
    timeout /t 1 >nul
    echo Applying license...
    slmgr /ato
    echo If a small window showed saying "Product activated successfully", you're done!
) else (
    echo Invalid selection. Please try again.
)

endlocal
pause