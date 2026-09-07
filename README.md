# Easy Tracker

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![PySide6](https://img.shields.io/badge/UI-PySide6-41CD52?logo=qt&logoColor=white)](https://doc.qt.io/qtforpython-6/)
[![Windows](https://img.shields.io/badge/Platform-Windows-0078D6?logo=windows&logoColor=white)](https://www.microsoft.com/windows)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Free](https://img.shields.io/badge/Price-Free-success)](#license)
[![Status](https://img.shields.io/badge/Status-Active%20Development-blue)](#roadmap)

A lightweight desktop app for keeping track of job applications without needing
an account, subscription, browser tab, or online service.

Built with **Python + PySide6**, the tracker stores everything locally in a simple
CSV file that you can open, back up, move, or analyze with Excel, Google Sheets,
Python, R, or any other spreadsheet/data tool.

> **Free to use, test, and share. No charge whatsoever. Credit is appreciated if
> you find it useful or redistribute it.**

---

## Features

- Track **Company, Country, Application Date, Position, Medium, Status, Last Update, Follow-up Date, Job URL, and Notes**
- Search across all application information
- Click any column header to sort ascending or descending
- Multi-select rows with `Ctrl` / `Shift`
- Delete multiple applications at once
- Open multiple job-posting URLs at once
- Native-style calendar date picker
- Status color coding
- Windows Light, Dark, and Slate themes
- Persistent appearance preference
- Hover over an application for about **2 seconds** to preview its Notes
- CSV-based local storage
- Buildable as a standalone Windows `.exe`
- No account or cloud connection required

---

## Screenshots

Add screenshots to a folder named `screenshots/`, then replace these placeholders:

```text
screenshots/
├── main-light.png
├── main-dark.png
├── add-application.png
└── hover-notes.png
```

Recommended README syntax:

```markdown
![Main window](screenshots/main-light.png)
![Dark mode](screenshots/main-dark.png)
```

---

## Quick Start

### Option 1 — Run from Python

Requirements:

- Windows 10 or 11
- Python 3.10+
- Internet access the first time dependencies are installed

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/easy-tracker.git
cd easy-tracker
```

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

Run:

```bash
python easy_tracker.py
```

You can also double-click:

```text
run_easy_tracker.bat
```

---

## Build the Windows `.exe`

A ready-to-use PyInstaller build script is included.

Double-click:

```text
BUILD_EXE.bat
```

The script will:

1. Check for Python
2. Install/update PySide6 and PyInstaller
3. Clean previous builds
4. Build a single windowed executable
5. Copy the CSV beside the executable
6. Open the finished `dist` folder

The final result will look like:

```text
dist/
├── Easy Tracker.exe
├── job_applications.csv
└── app_icon.ico
```

If `app_icon.ico` is present when building, it will automatically be embedded
into the executable.

> Keep `job_applications.csv` beside the `.exe`, because that is where the app
> reads and writes your application data.

---

## Example Data

The repository includes:

```text
job_applications_example.csv
```

It contains a single example application so you can immediately test the app,
including a sample note and GitHub link.

To use it, either:

- Rename it to `job_applications.csv`, or
- Copy its sample row into your existing `job_applications.csv`

The included example note says:

> Feel free to test it and share it. Not charged in anyway, but thankful if used and credited. Will work on future updates to add a Data Analysis page. Stay tuned :)

---

## CSV Structure

The tracker uses the following columns:

| Column | Purpose |
|---|---|
| Company | Company or studio name |
| Country | Country associated with the role |
| Date | Date you applied |
| Position | Job title |
| Medium | LinkedIn, company website, email, recruiter, referral, etc. |
| Status | Waiting, Interviewing, Follow-up, Offer, Accepted, Rejected, Withdrawn |
| Last Update | Last time the application changed |
| Next Follow-up | Optional follow-up reminder date |
| Job URL | Link to the original posting/application |
| Notes | Free-form notes shown in the hover preview |

Dates are stored as:

```text
YYYY-MM-DD
```

---

## Privacy

All job application information is stored **locally on your computer**.

The app does not require:

- An account
- A database server
- Cloud storage
- Analytics
- Telemetry
- A web connection during normal use

Your data is simply stored in `job_applications.csv`.

That also means **you are responsible for backing up the CSV** if the data is
important to you.

---

## Themes

Three themes are currently included:

- **Windows Light**
- **Dark**
- **Slate**

Your selected appearance is saved locally in:

```text
tracker_settings.txt
```

---

## Hover Notes

Applications can have longer notes without cluttering the table.

Hover over a row for roughly **2 seconds** and, if Notes are available, a small
preview card appears beside your cursor.

Move away, scroll, or click to dismiss it.

---

## Roadmap

Planned / considered improvements:

- [ ] **Data Analysis page**
- [ ] Application statistics and charts
- [ ] Response-rate analysis
- [ ] Interview / rejection / offer ratios
- [ ] Application activity over time
- [ ] Follow-up reminders
- [ ] More filtering controls
- [ ] Optional CSV import/export helpers
- [ ] Additional themes
- [ ] Better installer / release workflow

Have an idea? Feel free to open an Issue.

---

## Project Structure

```text
easy-tracker/
├── easy_tracker.py
├── run_easy_tracker.bat
├── BUILD_EXE.bat
├── requirements.txt
├── job_applications.csv
├── job_applications_example.csv
├── app_icon.ico
├── README.md
├── CONTRIBUTING.md
├── LICENSE
└── .gitignore
```


## Windows SmartScreen

Locally built PyInstaller executables are normally **unsigned**.

Because of that, Windows may show an **Unknown publisher** or SmartScreen
warning when opening the `.exe`.

This does not require disabling Windows Security. Code signing can be added in
the future for public release builds.

---

## Why I Made This

I wanted a simple application tracker that behaves like a normal desktop tool:
fast to open, easy to search, easy to back up, and without turning job hunting
into another online service or subscription.

The CSV format also keeps the data portable, which leaves room for future
analysis and visualization features.

---

## Support / Feedback

If you test it, find a bug, or have an idea for the next version, feel free to
open an Issue or reach out through GitHub.

GitHub: **https://github.com/YOUR_USERNAME**

---

## License

Released under the [MIT License](LICENSE).

Free to use, modify, and share.

Credit is appreciated. :)
