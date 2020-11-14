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
pyinstaller --noconfirm --onefile --console --icon "E:\Coding\Python\My_Projects\GoogleMeetAutomation\Executables\Automeet.ico" --add-binary "E:/Coding/Python/My_Projects/GoogleMeetAutomation/Executables/Drivers/chromedriver.exe;./selenium/webdriver" --add-binary "E:/Coding/Python/My_Projects/GoogleMeetAutomation/Executables/Drivers/geckodriver-32.exe;./selenium/webdriver" --add-binary "E:/Coding/Python/My_Projects/GoogleMeetAutomation/Executables/Drivers/geckodriver-64.exe;./selenium/webdriver" "E:/Coding/Python/My_Projects/GoogleMeetAutomation/Automeet.py"
echo.
echo Automeet.exe has been successfully created for Automeet.py 
echo.
echo.
pause.
exit

