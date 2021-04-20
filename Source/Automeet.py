"""
Automeet: Google Meet Automater
Meeting Automation for https://www.meet.google.com
Licensed under CC0-1.0 License to Pavana Narayana Bhat
------------------------------------------------------------------------------------------------------------------------
Code by: PiXinCreate
------------------------------------------------------------------------------------------------------------------------
Description:
    Automeet is a selenium based python script to
join and exit online sessions / meetings on Google
Meet that is scheduled in Google Calendar with a
single login to Google Account via stackoverflow
Automatically.

NOTE: Password is invisible. Check the readme.md for more information.
"""
try:
    # Importing packages
    import os
    import gc
    import sys
    import time
    import datetime as dt
    from msvcrt import getch

    from selenium import webdriver
    from selenium_stealth import stealth

    from selenium.webdriver.common.by import By
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions

    from selenium.common.exceptions import TimeoutException
    from selenium.common.exceptions import WebDriverException
    from selenium.common.exceptions import JavascriptException
    from selenium.common.exceptions import NoSuchWindowException
    from selenium.common.exceptions import NoSuchElementException
    from selenium.common.exceptions import NoAlertPresentException
    from selenium.common.exceptions import StaleElementReferenceException
    from selenium.common.exceptions import ElementNotInteractableException
    from selenium.common.exceptions import ElementClickInterceptedException


    # Setting console size
    os.system('mode con: cols=93 lines=30')
    os.system('powershell -command "&{$H=get-host;$W=$H.ui.rawui;$B=$W.buffersize;$B.height=5000;$W.buffersize=$B;}"')


    # Required Functions to be called

    def white_password(prompt):       # Secure password input, an alternative to getpass
        print(prompt, end='', flush=True)
        buf = b''
        while True:
            ch = getch()
            if ch in {b'\n', b'\r', b'\r\n'}:
                print('')
                break
            elif ch == b'\x08':  # Backspace
                buf = buf[:-1]
                print(f'\r{(len(prompt) + len(buf) + 1) * ""}\r{prompt}{"" * len(buf)}', end='', flush=True)
            elif ch == b'\x03':  # Ctrl+C
                raise KeyboardInterrupt
            else:
                buf += ch
                print('', end='', flush=True)       # Prints nothing instead of Password on the screen
        return buf.decode(encoding='utf-8')


    def resource_path(another_way):       # Provides the facility to run on both terminal as well as python console
        try:
            usual_way = sys._MEIPASS
        except AttributeError:
            usual_way = os.path.dirname(__file__)
        return os.path.join(usual_way, another_way)


    def login(username, password):       # Logs in the user
        try:
            driver.get("https://stackoverflow.com/users/login")
            time.sleep(0.1)
            WebDriverWait(driver, 60).until(expected_conditions.presence_of_element_located((By.XPATH, '//*[@id="openid-buttons"]/button[1]'))).click()
            time.sleep(0.2)
            try:
                WebDriverWait(driver, 60).until(expected_conditions.presence_of_element_located((By.ID, "Email"))).send_keys(username)
            except TimeoutException:
                print("Internet seems to be slow, check and Re-Start the Automeet.")
                exit_now()
            time.sleep(0.2)
            WebDriverWait(driver, 60).until(expected_conditions.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/div[2]/div[1]/form/div/div/input"))).click()
            time.sleep(0.5)

            try:
                try:
                    time.sleep(0.1)
                    WebDriverWait(driver, 60).until(expected_conditions.presence_of_element_located((By.ID, "password"))).send_keys(password)
                except TimeoutException:
                    print("Internet seems to be slow, check and Re-Start the Automeet.")
                    exit_now()
                time.sleep(0.2)
                WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable((By.ID, "submit"))).click()
            except TimeoutException or NoSuchElementException:
                print('\nUsername/Password seems to be incorrect, please re-check\nand Re-Run the program.')
                exit_now()
        except WebDriverException:
            exit_now()

        try:
            time.sleep(0.1)
            WebDriverWait(driver, 60).until(lambda webpage: "https://stackoverflow.com/" in webpage.current_url)
            print('\nLogin Successful!\n')
            del username, password
        except TimeoutException:
            print('\nUsername/Password seems to be incorrect, please re-check\nand Re-Run the program.')
            del username, password
            exit_now()


    def time_table():       # Checking for today's sessions
        meetings_today = driver.find_elements_by_class_name("wKIIs")  # VdLOD yUoCvf
        timetable_list = []
        for meetings in meetings_today:
            class_data = meetings.text.split('\n')
            class_time = ""
            driver.implicitly_wait(5)
            try:
                try:
                    class_time = dt.datetime.strptime(class_data[0], "%I:%M %p")
                except ValueError:
                    class_time = dt.datetime.strptime(class_data[0], "%H:%M")
            except ValueError:
                try:
                    class_time = dt.datetime.strptime(class_data[0], "%I:%M %p")
                except ValueError:
                    class_time = dt.datetime.strptime(class_data[0], "%H:%M")
            except Exception as e:
                print(e, end="\n")
                print("\n Please re-run the Automeet.")
                exit_now()

            driver.implicitly_wait(5)
            timetable_list.append([class_time,
                                   class_data[1],
                                   meetings])
        return timetable_list


    def present_time():       # Grabs the current time
        presenttime = dt.datetime.now().strftime("%I:%M %p")
        current_time_in_seconds = int((dt.datetime.strptime(presenttime, "%I:%M %p") - dt.datetime(1900, 1, 1)).total_seconds())
        return current_time_in_seconds


    def timer(seconds):       # Adds timer for the upcoming sessions to wait
        while seconds:
            mins, secs = divmod(seconds, 60)
            count_down = '{:02d}:{:02d}'.format(mins, secs)
            print('Will join in :  ' + count_down, end='\r', flush=True)
            time.sleep(1)
            seconds -= 1


    def stale_element_relief():       # Refreshing DOM. It waits for the element to not be stale
        time_table()
        time.sleep(4)
        ignored_exceptions = (NoSuchElementException, StaleElementReferenceException,)
        join = WebDriverWait(driver, 60, ignored_exceptions=ignored_exceptions) \
            .until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "wKIIs")))
        join.click()


    def auto_close_popup_message():       # Closes the pop-up message in the browser
        time.sleep(5)
        try:
            driver.implicitly_wait(10)
            driver.switch_to.alert.accept()
        except NoAlertPresentException:
            try:
                driver.implicitly_wait(10)
                driver.switch_to.alert.accept()
            except NoAlertPresentException:
                pass


    def live_count():       # Print Live count of participants
        try:
            try:
                driver.implicitly_wait(60)
                live_count.number_of_participants = driver.find_element_by_class_name("ZaI3hb").find_element_by_class_name("wnPUne").text

                if live_count.number_of_participants == '':
                    live_count.number_of_participants = driver.find_element_by_class_name("rua5Nb").text.strip("()")

            except StaleElementReferenceException:
                driver.implicitly_wait(60)
                live_count.number_of_participants = driver.find_element_by_class_name("ZaI3hb").find_element_by_class_name("wnPUne").text

                if live_count.number_of_participants == '':
                    live_count.number_of_participants = driver.find_element_by_class_name("rua5Nb").text.strip("()")

            except ValueError:
                live_count.number_of_participants = driver.find_element_by_class_name("rua5Nb").text.strip("()")

            except AttributeError or TypeError:
                print("Browser instance unexpectedly closed by the user. Please try again.")
                exit_now()
            except WebDriverException as e:
                if "not connected to DevTools" in e:
                    print("Please check your Internet connection and Re-Start the Automeet.")
                    exit_now()
            if int(live_count.number_of_participants) > live_count.max_count:
                live_count.max_count = int(live_count.number_of_participants)

            print(f'{"Live count of participants: " + live_count.number_of_participants + "    "}\r', end='', flush=True)       # Prints the live count
            time.sleep(0.5)

            # Several Participants left the meeting or recording Stopped.
            try:
                live_count.left_or_rec_stop = driver.find_element_by_class_name("aGJE1b").text
            except NoSuchElementException:
                pass
            except StaleElementReferenceException:
                try:
                    live_count.left_or_rec_stop = driver.find_element_by_class_name("aGJE1b").text
                except NoSuchElementException:
                    pass
            except WebDriverException as e:
                if "not connected to DevTools" in e:
                    print("Please check your Internet connection and Re-Start the Automeet.")
                    exit_now()

        except NoSuchElementException:  # An exception if Network change is detected.
            try:
                connection_lost = driver.find_element_by_class_name("RkzbPb").text
                if "You lost your network connection. Trying to reconnect." in connection_lost:
                    try:
                        WebDriverWait(driver, 180).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "crqnQb")))
                    except TimeoutException:
                        print("Please check your Internet connection and Re-Start the Automeet.")
                        exit_now()
            except NoSuchElementException:
                live_count()
                pass


    def end_class():       # Ends the current session
        live_count.max_count = 0
        live_count.left_or_rec_stop = ""
        time.sleep(10)
        # Clicks leave call button
        try:
            driver.find_element_by_xpath("//div[@aria-label='Leave call']").click()  # "class_name = U26fgb"
        except NoSuchElementException:
            driver.find_element_by_class_name("EIlDfe").click()  # An empty click to make bottom bar visible
            driver.implicitly_wait(2)
            driver.find_element_by_xpath("//div[@aria-label='Leave call']").click()
        except ElementNotInteractableException:
            driver.find_element_by_class_name("EIlDfe").click()  # An empty click to make bottom bar visible
            driver.implicitly_wait(2)
            driver.find_element_by_xpath("//div[@aria-label='Leave call']").click()
        except StaleElementReferenceException:
            try:
                driver.find_element_by_xpath("//div[@aria-label='Leave call']").click()  # "class_name = U26fgb"
            except NoSuchElementException:
                driver.find_element_by_class_name("EIlDfe").click()  # An empty click to make bottom bar visible
                driver.implicitly_wait(2)
                driver.find_element_by_xpath("//div[@aria-label='Leave call']").click()
            except ElementNotInteractableException:
                driver.find_element_by_class_name("EIlDfe").click()  # An empty click to make bottom bar visible
                driver.implicitly_wait(2)
                driver.find_element_by_xpath("//div[@aria-label='Leave call']").click()

        double_quotes = "\""
        print(f"{'The meeting ' + double_quotes + classTitle + double_quotes + ' ended now.'}\r", end='', flush=True)
        print(end='\n\n')
        time.sleep(3)
        # Returns to the Home Screen
        driver.get('https://meet.google.com/')       # Get's the user to the home page


    def exit_now():       # Exits the script
        print('-' * 90, end='\n')
        try:
            del USERNAME, PASSWORD
        except UnboundLocalError:
            pass
        try:
            driver.quit()       # Closes the browser instance
        except WebDriverException:
            pass
        input("Press any key to exit...")
        exit()


    # In The Beginning //
    print('\n')
    print("        ••      ••    ••  ••••••••  ••••••••  ••••  ••••  ••••••••  ••••••••  ••••••••  ")
    print("       ••••     ••    ••     ••     ••    ••  •• •••• ••  ••        ••           ••     ")
    print("      ••  ••    ••    ••     ••     ••    ••  ••  ••  ••  ••••••    ••••••       ••     ")
    print("     ••••••••   ••    ••     ••     ••    ••  ••      ••  ••        ••           ••     ")
    print("    ••      ••  ••••••••     ••     ••••••••  ••      ••  ••••••••  ••••••••     ••     ")
    print("                         Google Meet Automater by PiXinCreate                           ", end='\n\n')
    print("-" * 90, end='\n')

    # Login Credentials
    print('Google Account Login:\n---------------------', end='\n')
    USERNAME = input("User Name : ")
    PASSWORD = white_password(prompt="Password  : ")

    # Assigning Drivers
    options = Options()
    options.add_argument("start-maximized")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)

    # 1 to allow permissions and 2 to block them
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_experimental_option("prefs",
                                    {"profile.default_content_setting_values.media_stream_mic": 1,
                                     "profile.default_content_setting_values.media_stream_camera": 1,
                                     "profile.default_content_setting_values.geolocation": 2,
                                     "profile.default_content_setting_values.notifications": 2})

    driverPath = 'chromedriver.exe'

    try:
        try:
            # For 64 Bit Brave
            options.binary_location = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
        except WebDriverException:
            # For 32 Bit Brave
            options.binary_location = "C:\\Program Files (x86)\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
        driver = webdriver.Chrome(options=options, executable_path=resource_path(driverPath))
    except WebDriverException:
        # For Chrome
        driver = webdriver.Chrome(executable_path=resource_path(driverPath), options=options)

    except FileNotFoundError:
        print("Webdriver seems to be outdated, download the LATEST VERSION of AUTOMEET from here: "
              "'https://github.com/pixincreate/Automeet/releases/latest'", end='\n')
        exit_now()

    stealth(driver,
            user_agent='DN',
            languages=["en-US", "en"],
            vendor="Google Inc.",
            platform="Win32",
            webgl_vendor="Intel Inc.",
            renderer="Intel Iris OpenGL Engine",
            fix_hairline=True,
            )       # Before Login, using stealth

    # Logging in
    login(USERNAME, PASSWORD)
    print('-' * 90, end='\n')

    stealth(driver,
            user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36',
            languages=["en-US", "en"],
            vendor="Google Inc.",
            platform="Win32",
            webgl_vendor="Intel Inc.",
            renderer="Intel Iris OpenGL Engine",
            fix_hairline=True,
            )       # After logging in, revert back user agent to normal.


    # Redirecting to Google Meet Web-Page
    time.sleep(2)
    driver.execute_script("window.open('https://meet.google.com')")
    driver.switch_to.window(driver.window_handles[1])       # Redirecting to Google Meet from stackoverflow after logging in
    driver.switch_to.window(driver.window_handles[0])
    driver.close()
    driver.switch_to.window(driver.window_handles[0])

    # Automation Starts from here
    # Declarations
    lastClass = False
    live_count.max_count = 0
    live_count.left_or_rec_stop = live_count.rec_button = scheduledTimeInSeconds = classTime = classTitle = ""

    # Deleting the user data, i.e., taken in the beginning
    del USERNAME, PASSWORD

    # If no classes Exist today
    if not time_table():
        driver.execute_script("alert('No meetings has been scheduled for today. Automeet closes in 5 seconds:)')")
        print('No meetings has been scheduled for today.', end='\n\n')
        auto_close_popup_message()
        exit_now()

    # If classes Exist
    else:
        # Printing Timetable on the console
        print("Today's timeTable:\n------------------", end='\n')
        for sessions in time_table():
            print(sessions[0].strftime("%I:%M %p"), end="    ")
            print(sessions[1], end="  \n")
        print(end='\n')

        # Printing Logs/Happenings on the console
        print('-' * 90, end='\n')
        print('Activity Logs:\n--------------', end='\n')

        for i in range(0, len(time_table())):
            try:
                classTitle = time_table()[i][1].upper()
                classTime = time_table()[i][0].strftime("%I:%M %p")
                scheduledTimeInSeconds = int((dt.datetime.strptime(classTime, "%I:%M %p") - dt.datetime(1900, 1, 1)).total_seconds())
                try:
                    classTimeNextSession = time_table()[i + 1][0].strftime("%I:%M %p")
                    scheduledTimeInSecondsForNextSession = int((dt.datetime.strptime(classTimeNextSession, "%I:%M %p")
                                                                - dt.datetime(1900, 1, 1)).total_seconds())
                    if (scheduledTimeInSecondsForNextSession - present_time()) < 240 and (present_time() - scheduledTimeInSeconds) > 600:
                        classTitle = time_table()[i + 1][1].upper()
                        i += 1
                except IndexError:
                    lastClass = True
                    driver.execute_script("alert('This is the last session for today.')")
                    auto_close_popup_message()
            except IndexError:
                try:
                    driver.execute_script("alert('This was the last session for today. Tab closes in 5 seconds.')")
                    auto_close_popup_message()
                except JavascriptException:
                    pass
                print('\nLast session ended.\n')
                time.sleep(5)
                exit_now()

            # Joining the class 90 seconds before the scheduled time.
            if ((scheduledTimeInSeconds - present_time()) <= 90) or "\nNOW" in time_table()[i][2].text.upper():
                print('Joining \"' + classTitle + '\" now...', end='    ', flush=True)
                try:
                    # Clicks on the specific class which is scheduled.
                    time_table()[i][2].click()
                except StaleElementReferenceException:
                    stale_element_relief()

            else:
                # When waiting time to class is more than 1m 30s
                driver.execute_script("alert('Will join 1m 30s before the session starts.')")
                auto_close_popup_message()
                try:
                    waitingTime = (scheduledTimeInSeconds - 90) - present_time()
                    timer(waitingTime)
                except ValueError:
                    pass
                print('Joining \"' + classTitle + '\" now...', end='    ', flush=True)
                try:
                    # Clicks on the specific class which is scheduled.
                    time_table()[i][2].click()
                except StaleElementReferenceException:
                    stale_element_relief()

            # Turning Mic and Camera Off (Can be turned ON manually)
            time.sleep(1)
            try:
                blockPopUp = driver.find_element_by_xpath("/html/body/div[2]/div[3]/div/div[2]/div[2]/div[1]/div/span/span").click()
            except NoSuchElementException:
                pass

            try:
                turnOffMic = driver.find_element_by_xpath("//div[@aria-label='Turn off microphone (CTRL + D)']").click()
            except NoSuchElementException:
                turnOffMic = driver.find_element_by_xpath("//div[@aria-label='Turn off microphone (ctrl + d)']").click()
            try:
                turnOffCamera = driver.find_element_by_xpath("//div[@aria-label='Turn off camera (CTRL + E)']").click()
            except NoSuchElementException:
                turnOffCamera = driver.find_element_by_xpath("//div[@aria-label='Turn off camera (ctrl + e)']").click()

            try:
                bgBlur = driver.find_element_by_xpath(
                    "/html/body/div[2]/c-wiz/div/div/div[5]/div[3]/div/div[2]/div/div/div[1]/div/div[6]").click()
            except NoSuchElementException:
                pass

            # Clicks the JOIN NOW button
            # JoinNow = driver.find_element_by_class_name("NPEfkd")
            JoinNow = driver.find_element_by_xpath("//div[@role='button']//span[contains(text(), 'Join now')]")
            if "Join now" in JoinNow.text:
                try:
                    JoinNow.click()
                except ElementClickInterceptedException:
                    time.sleep(3)
                    JoinNow.click()
                except NoSuchElementException:
                    # Clicks the ASK TO JOIN button
                    AskToJoin = driver.find_element_by_xpath("//div[@role='button']//span[contains(text(), 'Ask to join')]")
                    if "Ask to join" in AskToJoin.text:
                        try:
                            AskToJoin.click()
                            WebDriverWait(driver, 600).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "kPEoYc GOJTSe")))
                        except TimeoutException:
                            driver.refresh()
                            try:
                                AskToJoin.click()
                                print('Kindly ask the host to allow you in.')
                                driver.execute_script("alert('Kindly ask the host to allow you in.')")
                                auto_close_popup_message()
                                AskToJoin.click()
                                WebDriverWait(driver, 596).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "kPEoYc GOJTSe")))
                            except TimeoutException:
                                driver.execute_script("alert('Please restart the Automeet and ask the host to allow you in."
                                                      "Automeet will now exit.')")
                                auto_close_popup_message()
                                print('Please restart the Automeet and ask the host to allow you in.\n'
                                      'Automeet will now exit.')
                                exit_now()
            print('Success.', end='\n')

            try:
                recordingJoinNow = driver.find_element_by_xpath("//div[@role='button']//span[contains(text(), 'Join now')]")
            except NoSuchElementException:
                pass

            # Clicks END button if conditions are satisfied.
            # Ends session when either of the condition is satisfied
            while True:
                live_count()

                try:
                    if int(live_count.number_of_participants) <= int(live_count.max_count) // 4:
                        print('Meeting will end now as Number of People Reduced to 1/4th the total strength.', end='\r', flush=True)
                        end_class()
                        break
                    elif "Several participants left the meeting." in live_count.left_or_rec_stop:
                        print('Meeting will end now as Several participants left the meeting.', end='\r', flush=True)
                        end_class()
                        break
                    elif "stopped recording" in live_count.left_or_rec_stop:
                        print('Meeting will end now as the recording stopped.', end='\r', flush=True)
                        end_class()
                        break
                    else:
                        pass
                except ValueError:
                    pass
                except AttributeError:
                    pass

            if lastClass:
                try:
                    driver.execute_script("alert('This was the last session for today. Tab closes in 5 seconds.')")
                    auto_close_popup_message()
                except JavascriptException:
                    pass
                print('Last session ended.\n')
                time.sleep(5)
                exit_now()

except NoSuchWindowException as exception:
    gc.collect()
    print('-' * 90, end='\n')
    print(exception)
    try:
        del USERNAME, PASSWORD
    except UnboundLocalError:
        pass
    try:
        driver.quit()  # Closes the browser instance
    except WebDriverException:
        pass
    input("Press any key to exit...")
    exit()
