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
echo                        Google Meet Automater by PiXinCreate                      
echo.
echo.
echo Automeet:
echo.
pyinstaller --noconfirm --onefile --console --icon "E:\Coding\Python\My_Projects\GoogleMeetAutomation\Executables\Automeet.ico" --add-data "E:\Coding\Python\My_Projects\GoogleMeetAutomation\Executables\stealth;." --add-binary "E:/Coding/Python/My_Projects/GoogleMeetAutomation/Executables/Drivers/chromedriver.exe;." "E:/Coding/Python/My_Projects/GoogleMeetAutomation/Automeet.py"
echo.
echo Automeet.exe has been successfully created for Automeet.py 
echo.
echo.
pause.
exit


