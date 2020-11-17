# Automeet - Google Meet Meetings Automater!
![Automeet Downloads](https://img.shields.io/github/downloads/pixincreate/Automeet/total?color=Blue&label=Automeet%20Downloads&logo=PiXinCreate&logoColor=Blue&style=for-the-badge)  
To download the **latest** release, click **_[here](https://github.com/pixincreate/Automeet/releases/latest)_**.

### Introduction:
**Automeet** is all about automating the process of logging **in** and **out** when attending a Meeting on Google Meet platform with a single run.

**Code by:** Pavana Narayana Bhat

### PreRequisites:
- **Windows** Operating system.
- Firefox / Google Chrome / Brave (v**85.0** or **above**).
- A Google **Account**.
- **Stable Internet** connection.

### Usage:
- Once the **PreRequisites** is satisfied, **Download** the executable from the *[releases section](https://github.com/pixincreate/Automeet/releases/latest)*.
- Run the **Automeet.exe**.
- Enter your **Google Account Login Credentials** that you use to join your meet meetings. **Automeet** takes care of the rest.

### Things to keep in mind:
- Please make sure that the **Google Meet meetings are scheduled on your Google Calendar** and the timings **doesnot** overlap with each other(like 2 meetings at the same time or whatever).
- Do note that the **Password** that you enter will show you nothing.

### Found any bugs?
Incase if you find any bugs, please raise an *[Issue Ticket](https://github.com/pixincreate/Automeet/issues/new/choose)* under the *[Issues Tab](https://github.com/pixincreate/Automeet/issues)* in this Repository. Will look into it, then solve the issue if it exist ASAP.

**Note:**  A **Warning** exists the .py file. To learn more about the warning, click *[**here**](https://stackoverflow.com/questions/63958561/how-to-merge-chromedriver-exe-with-a-python-script-that-runs-on-selenium-webdriv/63959432#63959432)*.

### FAQ:
*Q*: **Why _Automeet_ is SLOW at Start up**?  
*A*: It is a standalone executable file that contains all the required files to run the **Automeet**. As the executable creates a temporary folder to extract the files that are requierd by the **Automeet** to run during the Start up, it takes around `2 - 5` seconds at Max!

*Q*: **How did I create the EXECUTABLES**?  
*A*: `.exe` has been created using *[pyinstaller](https://pypi.org/project/pyinstaller/)*.

### Feature updates(will be added - If Online meetings continues to be conducted everywhere):
- Auto attendance (for students) that puts Present Sir / Mam on behalf of you.
- Make the UI interactable by replacing CLI with GUI.
- Add option for placing Meet links along with the Calendar scheduled links in meet homepage with the help of GUI.(Major update)

### LICENSE:
This project comes under CC0-1.0 License copyrighted to *(C) Pavana Narayana Bhat*. Click *[here](https://github.com/pixincreate/Online-Class-Automater/blob/master/LICENSE)* to learn more about the permissions offered by this license.

### Like my work?
**[SUBSCRIBE](https://www.youtube.com/c/pixincreate/subscribe)** to my **YouTube** channel **[*PiXinCreate*](https://www.youtube.com/c/pixincreate)** followed by **hitting BELL icon**(*once*), incase if you haven't already!

### About me:
I'm Pavana Narayana Bhat, a coder, and a YouTuber running PiXinCreate on YouTube. I make videos related to Photo editing where I teach my fellow viewers to edit photos on their own to the extinct I know. I'm a Privacy Centered tech enthusiast. You can find me on: Instagram, Facebook, YouTube, Twitter **`@pixincreate`** is my userName. See you there.:)

© PiXinCreate All rigths reserved.
#
## Improvements over time:
- Initial Release.
- Fixed ```IndexError```, ```NoSuchElementException``` that used to appear in common for no reasons.
- Some Console CLI changes to interact with user.
- Reduced code complexity by creating functions for code re-use.
- Fixed waiting time issues.
- Ending of meetings now depends on number of participants left in the meeting(1/4th of participant strength) instead of Time, which was used by the **Automeet** earlier.
- **Automeet** now brings support for 64 bit Brave Browsers.
- Merged Automeet_C with Automeet_B, reduced confusion in users as well.
- Added live participants' count.
- Fixed *End button* issue that used to give ```NoSuchElementException``` as the `button array` hides itself when more than `1` participant present in the meeting.
- Some extra exceptions added through Testing.
- Made the `Live Count` to get replaced by the `Session ended now` notification.
- Added default dimensions to the executable. 
- Made `Ask To Join` button to work in a more specific way by making it wait `Explicitly`.(fixes needed)
- Increased icon quality.
- Added some Exception Handlers to handle errors(especially `IndexError` and `JavascriptError`) that occurred due to bad practices followed by the host.
- Removed unnecessary 240 iterations and some minor tweaks to pop-up notifications on the browser instance.
- Add supoort for Firefox web browsers - 32 bit, 64 bit(theoritically).
- Add condition to end session when recording stops(if it was recording before).
- Fix sudden ending of meetings from ```session - 2``` and minor console UI changes.
- Fixed for `Ask to join` button that didn't use to do it's work properly.
- Removed unnecessary lines of code.
- Fixed Live-count error (```NoSuchElementException``` and ```StaleElementReferenceException``` error, to be more precise) and ```End-call``` button.
- Added some exceptions to handle ```You lost your network connection. Trying to reconnect.``` in a systematic way.
- Fix Live Count when `people` or `chat` tab is open.
- Change ```end_class``` dependency from ```xpath``` to ```aria-label``` just to avoid exceptions like ```NoSuchElementException```.
- Fix ```IndexError``` at ```lastclass```.
- Fix rare ```ValueError``` when meetings ends at less then 1m 30s to the next scheduled meeting.
- Waiting time for upcoming session is now made visible.
#
