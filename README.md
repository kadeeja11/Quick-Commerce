# Quick Commerce Project - Run Guide

## Prerequisites

Make sure **Python 3.11+** is installed.

Create a virtual environment (optional but recommended):

```bash
python -m venv venv


## Order of Execution

Follow these steps in order to run the project smoothly:


### Step 1: Run Scrapers
```bash
python scrapers/zepto.py
python scrapers/blinkit.py
python scrapers/instamart.py




### Step 2: Process Data
```bash
python processing.py




### Step 3: Run Dashboard
```bash
python dashboard.py


*** Step 4: Export to Google Sheets ***
```bash
python export_to_gsheet.py




### Step 5: Refer Output Screenshot folder to see all the output


