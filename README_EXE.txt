EASY TRACKER — EXE BUILD PACKAGE

BUILDING THE APP
================
1. Extract this ZIP completely.
2. Optional: place your custom Windows icon in the folder as:
       app_icon.ico
3. Double-click:
       BUILD_EXE.bat
4. The script installs/updates PySide6 and PyInstaller.
5. When complete, the 'dist' folder opens automatically.

FINAL PORTABLE APP
==================
dist\
    Easy Tracker.exe
    job_applications.csv
    app_icon.ico          (if supplied)
    tracker_settings.txt  (if present)

IMPORTANT
=========
Keep job_applications.csv in the same folder as the EXE.

The source has been adjusted for PyInstaller so the executable reads and
writes data beside the EXE, rather than inside PyInstaller's temporary folder.

CUSTOM ICON
===========
Name your ICO exactly:
    app_icon.ico

If it is present when BUILD_EXE.bat runs, it will be embedded in the EXE
and also used as the running application's window/taskbar icon.

WHERE TO KEEP THE APP
=====================
A folder in Desktop, Documents, OneDrive, etc. is ideal.

Avoid Program Files if you want the CSV beside the EXE because Windows may
restrict write access there.

WINDOWS SMARTSCREEN
===================
This is a locally built, unsigned executable, so Windows may show
'Unknown publisher'. That is normal for personal PyInstaller builds.


HOVER NOTES
===========
Hover the mouse over any application row for about 2 seconds.
If that application has Notes, a small note card appears beside the cursor.
Moving away, clicking, or scrolling hides it immediately.
