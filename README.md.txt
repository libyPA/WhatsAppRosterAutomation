# WhatsAppRosterAutomation
Developed a Python script that automates sending weekly rosters to employees via WhatsApp. The script reads data from Excel, formats schedules, and sends messages automatically. Implemented using Python, Pandas, PyWhatKit, and time management logic for reliable delivery.

## Features

* Reads employee schedules from Excel using **Pandas**.
* Formats messages with **day, time, and place** for each employee.
* Sends messages via **WhatsApp Web** automatically.
* Handles international phone numbers with country codes.
* Ensures reliable delivery using configurable wait times.

## Technologies

* Python 3.x
* Pandas
* PyWhatKit
* Excel Automation
* PowerShell (Windows)

## Installation

1. Clone the repository:

```bash
git clone https://github.com/YourUsername/whatsapp-roster-automation.git
cd whatsapp-roster-automation
```

2. Create a virtual environment:

```bash
python -m venv env
```

3. Activate the virtual environment:
   **On Windows PowerShell:**

```powershell
# Temporarily bypass execution policy for the current session only
Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope Process
.\env\Scripts\Activate.ps1
```

4. Install required packages manually:

```bash
pip install pandas pywhatkit openpyxl
```

## Usage

1. Prepare an Excel file `roster.xlsx` with columns:

```
Name | Phone | Monday | Tuesday | ... | Sunday
```

* **Phone number** must include country code (e.g., `+353123456789`).

2. Run the script:

```bash
python rosterExcelToWhatsapp.py
```

3. The script will automatically open WhatsApp Web and send messages after the configured `wait_time`.

## Notes

* Make sure you are **logged in to WhatsApp Web** in your default browser.
* If using PowerShell, the **execution policy bypass** is required, and it only applies to the current session.
* Adjust `wait_time` in the script if your system/browser is slow.

