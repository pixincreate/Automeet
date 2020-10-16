"""
Automeet: Google Meet Automater
Content Automation for https://www.meet.google.com
Licensed under CC0-1.0 License to Pavana Narayana Bhat
------------------------------------------------------------------------------------------------------------------------
Code by: Pavana Narayana Bhat AKA PiXinCreate
Finalised on 7 - 10 - 2020 at 12:04 PM IST
------------------------------------------------------------------------------------------------------------------------
Description:
    Selenium + Chromedriver based python script to
automate google meet meetings/online classes which
is scheduled on Google Calendar by logging in via
stackoverflow.com in an instance of Browser i.e.
created by selenium when the code is executed.
NOTE: Password is invisible. Check the readme.md for more information.
"""
# Importing packages /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
import os
import sys
import time
import datetime as dt
from msvcrt import getch

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import ElementNotInteractableException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import JavascriptException


# Setting console size ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
os.system('mode con: cols=93 lines=30')
os.system('powershell -command "&{$H=get-host;$W=$H.ui.rawui;$B=$W.buffersize;$B.height=5000;$W.buffersize=$B;}"')


# Required Functions to be called ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
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
    except Exception:
        usual_way = os.path.dirname(__file__)
    return os.path.join(usual_way, another_way)


def login(username, password):       # Logs in the user
    driver.get('https://accounts.google.com/o/oauth2/auth/identifier?client_id=717762328687-iludtf96g1hinl76e4lc1b9a82g457nn.apps.googleusercontent'
               '.com&scope=profile%20email&redirect_uri=https%3A%2F%2Fstackauth.com%2Fauth%2Foauth2%2Fgoogle&state=%7B%22sid%22%3A1%2C%22st%22%3A%2'
               '259%3A3%3Abbc%2C16%3A561fd7d2e94237c0%2C10%3A1599663155%2C16%3Af18105f2b08c3ae6%2C2f06af367387a967072e3124597eeb4e36c2eff92d3eef697'
               '1d95ddb5dea5225%22%2C%22cdl%22%3Anull%2C%22cid%22%3A%22717762328687-iludtf96g1hinl76e4lc1b9a82g457nn.apps.googleusercontent.com%22%'
               '2C%22k%22%3A%22Google%22%2C%22ses%22%3A%2226bafb488fcc494f92c896ee923849b6%22%7D&response_type=code&flowName=GeneralOAuthFlow')

    driver.find_element_by_name("identifier").send_keys(username)
    WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, "//*[@id='identifierNext']/div/button/div[2]"))).click()
    driver.implicitly_wait(4)

    try:
        driver.find_element_by_name("password").send_keys(password)
        WebDriverWait(driver, 2).until(expected_conditions.element_to_be_clickable((By.XPATH, "//*[@id='passwordNext']/div/button/div[2]"))).click()
    except TimeoutException:
        print('\nUsername/Password seems to be incorrect, please re-check\nRe-Run the program.')
        del username, password
        exit_now()
    except NoSuchElementException:
        print('\nUsername/Password seems to be incorrect, please re-check\nRe-Run the program.')
        del username, password
        exit_now()
    try:
        WebDriverWait(driver, 5).until(lambda webpage: "https://stackoverflow.com/" in webpage.current_url)
        print('\nLogin Successful!\n')
    except TimeoutException:
        print('\nUsername/Password seems to be incorrect, please re-check\nRe-Run the program.')
        exit_now()


def time_table():       # Checking for today's classes
    current_time = dt.datetime.now()
    classes_today = driver.find_elements_by_class_name("wKIIs")
    timetable_list = []
    for classes in classes_today:
        class_data = classes.text.split('\n')
        driver.implicitly_wait(5)
        try:
            class_time = dt.datetime.strptime(class_data[0], "%I:%M %p").replace(year=current_time.year,
                                                                                 month=current_time.month,
                                                                                 day=current_time.day)
        except ValueError:
            class_time = dt.datetime.strptime(class_data[0], "%H:%M").replace(year=current_time.year,
                                                                              month=current_time.month,
                                                                              day=current_time.day)

        driver.implicitly_wait(5)
        timetable_list.append([class_time,
                               class_data[1],
                               classes])
    return timetable_list


def present_time():       # Grabs the current time
    presenttime = dt.datetime.now().strftime("%I:%M %p")
    current_time_in_seconds = int((dt.datetime.strptime(presenttime, "%I:%M %p") - dt.datetime(1900, 1, 1)).total_seconds())
    return current_time_in_seconds


def stale_element_relief():       # Refreshing DOM. It waits for the element to not be stale
    time_table()
    time.sleep(4)
    ignored_exceptions = (NoSuchElementException, StaleElementReferenceException,)
    join = WebDriverWait(driver, 60, ignored_exceptions=ignored_exceptions) \
        .until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "wKIIs")))
    join.click()


def live_count():       # Print Live count of participants
    driver.implicitly_wait(5)
    live_count.number_of_participants = driver.find_element_by_class_name("ZaI3hb").find_element_by_class_name("wnPUne").text

    if live_count.number_of_participants == '':
        live_count.number_of_participants = driver.find_element_by_class_name("rua5Nb").text.strip('()')

    if int(live_count.number_of_participants) > live_count.max_count:
        live_count.max_count = int(live_count.number_of_participants)

    print(f'{"Live count of participants: " + live_count.number_of_participants + " "}\r', end='', flush=True)       # Prints the live count
    time.sleep(1)

    # Several Participants left the meeting.
    try:
        live_count.left = driver.find_element_by_class_name("aGJE1b").text
    except NoSuchElementException:
        pass
    except StaleElementReferenceException:
        try:
            live_count.left = driver.find_element_by_class_name("aGJE1b").text
        except NoSuchElementException:
            pass

    # Check for stop record to end meeting
    try:
        live_count.rec_stop = driver.find_element_by_class_name("aGJE1b").text
    except NoSuchElementException:
        pass
    except StaleElementReferenceException:
        try:
            live_count.rec_stop = driver.find_element_by_class_name("aGJE1b").text
        except NoSuchElementException:
            pass
        

def end_class():       # Ends the current session
    time.sleep(3)
    # Clicks leave call button
    leave_call = driver.find_element_by_class_name("rG0ybd").find_element_by_class_name("q2u11")
    try:
        leave_call.find_element_by_xpath("//*[@id='ow3']/div[1]/div/div[5]/div[3]/div[9]/div[2]/div[2]/div").click()
    except ElementNotInteractableException:
        driver.find_element_by_class_name("EIlDfe").click()  # An empty click to make bottom bar visible
        driver.implicitly_wait(2)
        leave_call.find_element_by_xpath("//*[@id='ow3']/div[1]/div/div[5]/div[3]/div[9]/div[2]/div[2]/div").click()
    except NoSuchElementException:
        driver.find_element_by_class_name("EIlDfe").click()  # An empty click to make bottom bar visible
        driver.implicitly_wait(2)
        leave_call.find_element_by_xpath("//*[@id='ow3']/div[1]/div/div[5]/div[3]/div[9]/div[2]/div[2]/div").click()

    print(f'{"The class " + classTitle + " ended now.                                     "}\r', end='', flush=True)
    print(end='\n\n')
    live_count.max_count = 0
    time.sleep(3)
    # Returns to the Home Screen
    driver.get('https://meet.google.com/')       # Get's the user to the home page


def exit_now():       # Exits the script
    print('-' * 90, end='\n')
    try:
        driver.quit()       # Closes the browser instance
    except WebDriverException:
        pass
    input("Press any key to exit...")
    exit()


# In The Beginning ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
print('\n')
print("      ••      ••    ••  ••••••••  ••••••••  ••••  ••••  ••••••••  ••••••••  ••••••••  ")
print("     ••••     ••    ••     ••     ••    ••  •• •••• ••  ••        ••           ••     ")
print("    ••  ••    ••    ••     ••     ••    ••  ••  ••  ••  ••••••    ••••••       ••     ")
print("   ••••••••   ••    ••     ••     ••    ••  ••      ••  ••        ••           ••     ")
print("  ••      ••  ••••••••     ••     ••••••••  ••      ••  ••••••••  ••••••••     ••     ")
print("                   Google Meet Automater by Pavana Narayana Bhat                      ", end='\n\n')
print("-" * 90, end='\n')

# Login Credentials //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
print('Google Account Login:\n---------------------', end='\n')
USERNAME = input("User Name : ")
PASSWORD = white_password(prompt="Password  : ")

# Assigning Drivers //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
options = Options()
options.add_argument("start-maximized")
driverPath = './driver/chromedriver.exe'
driverPathF64 = './driver/geckodriver-64'
driverPathF32 = './driver/geckodriver-32'

# 1 to allow permissions and 2 to block them
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_experimental_option("prefs",
                                {"profile.default_content_setting_values.media_stream_mic": 1,
                                 "profile.default_content_setting_values.media_stream_camera": 1,
                                 "profile.default_content_setting_values.geolocation": 2,
                                 "profile.default_content_setting_values.notifications": 2})
try:
    try:
        # For 64 Bit Brave
        options.binary_location = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
    except WebDriverException:
        # For 32 Bit Brave
        options.binary_location = "C:\\Program Files (x86)\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
    driver = webdriver.Chrome(options=options, executable_path=resource_path(driverPath))

except WebDriverException:
    try:
        driver = webdriver.Chrome(resource_path(driverPath), options=options)
    except WebDriverException:
        try:
            # For 64 Bit Firefox
            driver = webdriver.Firefox(executable_path=driverPathF64)
        except WebDriverException:
            # For 32 Bit Firefox
            driver = webdriver.Firefox(executable_path=driverPathF32)

# Logging in /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
try:
    login(USERNAME, PASSWORD)
except WebDriverException:
    print('Please check your internet connection and try again.')
    exit_now()
print('-' * 90, end='\n')

# Redirecting to Google Meet Web-Page ////////////////////////////////////////////////////////////////////////////////////////////////////////////////
time.sleep(2)
driver.get('https://meet.google.com')       # Redirecting to Google Meet from stackoverflow after logging in

# Automation Starts from here ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Declarations
lastClass = False
live_count.max_count = 0
live_count.left = live_count.rec_stop = live_count.rec_button = scheduledTimeInSeconds = classTime = classTitle = ""
global cond

# Deleting the user data, i.e., taken in the beginning
del USERNAME, PASSWORD

# If no classes Exist today
if not time_table():
    driver.execute_script("alert('No classes has been scheduled for today. AutoMeet closes in 5 seconds:)')")
    print('No classes has been scheduled for today.', end='\n\n')
    time.sleep(4)
    try:
        driver.implicitly_wait(4)
        driver.switch_to.alert.accept()
    except NoAlertPresentException:
        pass
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
        except IndexError:
            lastClass = True

        try:
            classTimeNextSession = time_table()[i + 1][0].strftime("%I:%M %p")
            scheduledTimeInSecondsForNextSession = int((dt.datetime.strptime(classTimeNextSession, "%I:%M %p")
                                                        - dt.datetime(1900, 1, 1)).total_seconds())
            if (scheduledTimeInSecondsForNextSession - present_time()) < 240:
                classTitle = time_table()[i + 1][1].upper()
                i += 1
        except IndexError:
            lastClass = True
            driver.execute_script("alert('This is the last class for today.')")
            time.sleep(4)
            try:
                driver.implicitly_wait(4)
                driver.switch_to.alert.accept()
            except NoAlertPresentException:
                pass

        # Joining the class 90 seconds before the scheduled time.
        if ((scheduledTimeInSeconds - present_time()) <= 90) or "\nNOW" in time_table()[i][2].text.upper():

            print('Joining the class \"' + classTitle + '\" now...', end='    ', flush=True)
            try:
                # Clicks on the specific class which is scheduled.
                time_table()[i][2].click()
            except StaleElementReferenceException:
                stale_element_relief()

        else:
            # When waiting time to class is more than 1m 30s
            driver.execute_script("alert('Will retry 1m 30s before the class is conducted.')")
            time.sleep(4)
            try:
                driver.implicitly_wait(4)
                driver.switch_to.alert.accept()
            except NoAlertPresentException:
                pass
            print('Will retry 1m 30s before the class is conducted.')
            time.sleep((scheduledTimeInSeconds - 90) - present_time())
            print('Joining the class \"' + classTitle + '\" now...', end='    ', flush=True)
            try:
                time_table()[i][2].click()
            except StaleElementReferenceException:
                stale_element_relief()

        # Turning Mic and Camera Off (Can be turned ON manually)
        time.sleep(1)
        try:
            blockPopUp = driver.find_element_by_xpath("/html/body/div[2]/div[3]/div/div[2]/div[2]/div[1]/div/span/span").click()
        except NoSuchElementException:
            pass
        turnOffMic = driver.find_element_by_class_name("EhAUAc").find_element_by_class_name("ZB88ed").click()
        turnOffCamera = driver.find_element_by_class_name("EhAUAc").find_element_by_class_name("GOH7Zb").click()
        try:
            bgBlur = driver.find_element_by_xpath(
                "/html/body/div[2]/c-wiz/div/div/div[5]/div[3]/div/div[2]/div/div/div[1]/div/div[6]").click()
        except NoSuchElementException:
            pass

        try:
            # Clicks the JOIN NOW button
            driver.find_element_by_class_name("l4V7wb").click()
        except ElementClickInterceptedException:
            time.sleep(3)
            driver.find_element_by_class_name("l4V7wb").click()
        except NoSuchElementException:
            # Clicks the ASK TO JOIN button
            try:
                WebDriverWait(driver, 600).until(expected_conditions.element_to_be_clickable((By.CLASS_NAME, "crqnQb"))).click()
            except TimeoutException:
                driver.refresh()
                try:
                    driver.execute_script("alert('Kindly ask the host to allow you in personally.')")
                    time.sleep(4)
                    try:
                        driver.implicitly_wait(4)
                        driver.switch_to.alert.accept()
                    except NoAlertPresentException:
                        pass
                    print('Kindly ask the host to allow you in personally.')
                    WebDriverWait(driver, 600).until(expected_conditions.element_to_be_clickable((By.CLASS_NAME, "crqnQb"))).click()
                except TimeoutException:
                    driver.execute_script("alert('Please restart the Automeet once the host allows you in or continue manually. Automeet will "
                                          "now exit excluding Browser Instance.')")
                    time.sleep(4)
                    try:
                        driver.implicitly_wait(4)
                        driver.switch_to.alert.accept()
                    except NoAlertPresentException:
                        pass
                    print('Please restart the Automeet once the host allows you in or continue manually.\n'
                          'Automeet will now exit excluding Browser Instance.')
                    exit()
        print('Success.', end='\n')

        # Clicks END button if number of student count goes lesser than 1/4th of total strength.
        # Ends session when either of the condition is satisfied
        cond = True
        while cond:
            live_count()
            try:
                if ((int(live_count.number_of_participants)) <= int(int(live_count.max_count) / 4)) or\
                        ("Several participants left the meeting." in live_count.left) or\
                        ("has stopped recording." in live_count.rec_stop):
                    end_class()
                    cond = False
                else:
                    cond = True
            except ValueError:
                pass
            except AttributeError:
                pass

        if lastClass:
            try:
                driver.execute_script("alert('This was the last Class for today. Tab closes in 5 seconds.')")
                time.sleep(4)
                try:
                    driver.implicitly_wait(4)
                    driver.switch_to.alert.accept()
                except NoAlertPresentException:
                    pass
            except JavascriptException:
                pass
            print('\nLast class ended.\n')
            time.sleep(5)
            exit_now()
