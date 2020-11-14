@ECHO OFF
color 09
echo Immediate direct Conversion of Automeet.py to Automeet.exe standalone
echo.
echo.
echo         **      **    **  ********  ********  ****  ****  ********  ********  ********  
echo        ****     **    **     **     **    **  ** **** **  **        **           **     
echo       **  **    **    **     **     **    **  **  **  **  ******    ******       **     
echo      ********   **    **     **     **    **  **      **  **        **           **     
echo     **      **  ********     **     ********  **      **  ********  ********     **     
echo                      Google Meet Automater by Pavana Narayana Bhat                      
echo.
echo.
echo Automeet:
echo.
pyinstaller --noconfirm --onefile --console --icon "Drive:\path\to\icon\ pixincreate Automeet.ico" --add-binary "Drive:/path/to/pixincreate chromedriver.exe;./selenium/webdriver" --add-binary "Drive:/path/to/pixincreate geckodriver-32.exe;./selenium/webdriver" --add-binary "Drive:/path/to/pixincreate geckodriver-64.exe;./selenium/webdriver" "Drive:/path/to/pixincreate Automeet.py source code"
echo.
echo Automeet.exe has been successfully created for Automeet.py by PiXinCreate
echo.
echo.
pause.
exit


