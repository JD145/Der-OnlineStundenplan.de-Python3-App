<img alt="Logo" src="http://der-onlinestundenplan.de/app/templates/default/images/Der-OnlineStundenplan.de_logo.svg" width="100" height="100"</img>

# Der-OnlineStundenplan.de-Python3-App
## Introduction
This is an Python3 App for a little plattform used for online timetables in some german schools called <b>Der-Onlinestundenplan.de</b>. The application is tested with Python 3.5!

Here are some links to further informations. Sadly they are only available in german at this time.

+[School request](https://www.der-onlinestundenplan.de/schule-einreichen)
<br>If your school timetable isn't supported, but offers an online timetable, please let us know and we will try to expand the service for your school. You can easily use the link above to contact the administrator of this service. This is 100% free for you!

+[Other Apps](https://www.Der-OnlineStundenplan.de/apps)

+[API Documentation](https://www.Der-OnlineStundenplan.de/api)


## How to use
### 1. Select a school
First you have to select a school. The syntax for selecting a school is the following:<br>
<i>-s 'schoolname'</i> or <i>--school 'schoolname'</i>

If you don't know the correct schoolname, or want to know, which schools are supported, simply use the command:<br>
<i>-ls</i> or <i>--schools</i>

To show some information about a school, select only a school.

### 2. Select a class
After you have selected a school, you have to select a class of the school. Use the following syntax:<br>
<i>-c 'classname'</i> or <i>--schoolClass 'classname'</i>

You can list all available classes with:<br>
<i>-lc</i> or <i>--classes</i>

### 3. Select a timetable
At last, after selecting school and class, timetable of current week will be shown. The modify the shown week, use the parameter:<br>
<i>-rw '-1'</i> or <i>--relativeWeek '-1' </i>
(The '-1' will select the last week.)

Example for timetable of class 'eit42' of school 'rvwbk' and last week:
<br><i>Der-OnlineStundenplan.py -s rvwbk -c eit42 -rw -1</i>
