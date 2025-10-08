# Quick Commerce Project - Run Guide

## Prerequisites

Make sure **Python 3.11+** is installed.

Create a virtual environment (optional but recommended):

python -m venv venv

For macOS/Linux:
source venv/bin/activate

For Windows:
venv\Scripts\activate

## Order of Execution

Follow these steps in order to run the project smoothly:

### Step 1: Run Scrapers

python scrapers/zepto.py
python scrapers/blinkit.py
python scrapers/instamart.py


### Step 2: Process Data

python processing.py


### Step 3: Run Dashboard

python dashboard.py


### Step 4: Export to Google Sheets

python export_to_gsheet.py


### Step 5: View Output

Refer to the **Output Screenshot** folder to see all results.
