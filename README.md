# Automeet
![Automeet Downloads](https://img.shields.io/github/downloads/pixincreate/Automeet/total?color=Blue&label=Automeet%20Downloads&logo=PiXinCreate&logoColor=Blue&style=for-the-badge)  
To download the **lastest** release, click **_[here](https://github.com/pixincreate/Automeet/releases/latest)_**.

### Introduction:
As the name says, Automeet is all about automating the process of logging **in** and **out** when attending a Meeting on Google Meet platform with a single run. Automeet is mainly targeted for the employees and Students out there to help them out manage their time which is basically wasted in waiting to attend sessions and clickings!

**Code by:** Pavana Narayana Bhat

### PreRequisites:
- **Windows** Operating system.
- Google Chrome / Brave (v**85.0** or **above**).
- A Google **Account**.
- **Stable Internet** connection.

### Usage:
- Once the **PreRequisites** is satisfied, you're almost done. **Download** the executable from the *[releases section](https://github.com/pixincreate/Automeet/releases)*.
- Run the **Automeet.exe**.
- Enter your **Google Account Login Credentials** that you used to join your online meetings.
- Chill all day long watching the automation.

### Things to keep in mind:
- Please make sure that the Google Meet meetings are scheduled on your Google Calendar and the timings doesnot overlap with each other(like 2 meetings at the same time             or whatever).
- Also, do note that the **Password** that you enter is not visible(neither in ```*```), instead you'll see nothing but empty space.
- User will get an error stating **```valueError```** when a user interferes at the time of Auromation. Just re-run the **Automeet**.

### Working:
- On logging in to your Google Account, **Automeet** will fetch the day's **scheduled meetings**.
- Then updates them in the console for you with timings.
- If the meeting is not yet started, it will wait till 1m 30s before the scheduled time.
- When participants' count **reduces** to/below the **1/4th** of the total strength **or** if *```"Several participants left the meeting."/ "User_name stopped recording"```* notification arrives in the meeting when going on, **Automeet** will end the call, and waits for/joins the next one.
- Incase you join the meeting 5 minutes before the next scheduled meeting, it will directly join you for that instead of the previous one.

### Found any bugs?
Incase you find any bugs, please raise an *[Issue Ticket](https://github.com/pixincreate/Automeet/issues/new/choose)* under the *[Issues Tab](https://github.com/pixincreate/Automeet/issues)* of this Repository. Will look into it, then solve the issue if it exist.

**Note:**  A **Warning** exists in both the .py files. To learn more about the warning, click *[here](https://stackoverflow.com/questions/63958561/how-to-merge-chromedriver-exe-with-a-python-script-that-runs-on-selenium-webdriv/63959432#63959432)*.

### FAQ:
*Q*: **Why _Automeet_ is SLOW at Start up**?  
*A*: It is a standalone executable file that contains all the required files to run the **Automeet**. As the executable creates a temporary folder to extract the files that are requierd by the **Automeet** to run during the Start up, it takes around `2 -3` seconds at Max!

*Q*: **Is it safe to use and trustable**?  
*A*: Read the security.md by clicking *[here](https://github.com/pixincreate/Automeet/blob/main/Security.md)* first. Yes, you can trust **Automeet** and its processes. You can check it's **source** by clicking *[here](https://github.com/pixincreate/Automeet/blob/main/Source/Automeet.py)*.

*Q*: **How do I create the EXECUTABLES**?  
*A*: `.exe` has been created using *[pyinstaller](https://pypi.org/project/pyinstaller/)*.

### Feature updates(that I'm currently thinking to Add):
- Auto attendance (for students) that puts Present Sir/ Mam on behalf of you.
- Exit meetings based on Recording of sessions.

### LICENSE:
This project comes under CC0-1.0 License copyrighted to *(C) Pavana Narayana Bhat*. Click *[here](https://github.com/pixincreate/Online-Class-Automater/blob/master/LICENSE)* to learn more about the permissions offered by this license.

### Like my work?
I ask you nothing but a **Like** and **[Subscribe](https://www.youtube.com/c/pixincreate/subscribe)** to my **YouTube** channel **[*PiXinCreate*](https://www.youtube.com/c/pixincreate)** followed by **hitting BELL icon** *once*, incase if you haven't already.

### About me:
I'm Pavana Narayana Bhat, a coder, and a YouTuber running PiXinCreate on YouTube. I make videos related to Photo editing where I teach my fellow viewers to edit photos on their own to the extinct I know. I'm a Privacy Centered tech enthusiast. You can find me on: Instagram, Facebook, YouTube, Twitter **`@pixincreate`** is the userName. See you there.:)

© PiXinCreate All rigths reserved.
#
## Change Logs based on the commits to the Source:
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
- Made `Ask To Join` button to work in a more specific way by making it wait `Explicitly` and finalised the code as of now.
- Increased icon quality.
- Added some Exception Handlers to handle errors(especially `IndexError` and `JavascriptError`) that occurred due to bad practices followed by the host.
- Fixed the unexpected endings of `Sessions` after the first one.
- Removed unnecessary 240 iterations and some minor tweaks to pop-up notifications on the browser instance.
- Add supoort for Firefox web browsers - 32 bit, 64 bit.
- Add condition to end session when recording stops(if it was recording before).
#
