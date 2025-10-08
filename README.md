# Quick Commerce Project - Run Guide

## ⚡ Prerequisites

Make sure **Python 3.11+** is installed.

Create a virtual environment (optional but recommended):

```bash
python -m venv venv


## 7️⃣ Order of Execution

Follow these steps in order to run the project smoothly:

---

### Step 1: Run Scrapers (Optional)

Only required if the JSON files in `data/raw/` do not exist or need updating:

```bash
python scrapers/zepto.py
python scrapers/blinkit.py
python scrapers/instamart.py


### Step 2: Process Data

This script processes all raw JSON files (`zepto.json`, `blinkit.json`, `instamart.json`) and combines them into a single DataFrame for use in the dashboard.  

```bash
python processing.py


### Step 3: Run Dashboard

Launch the interactive dashboard to visualize the combined data from all platforms.

```bash
python dashboard.py


### Step 4: Export to Google Sheets (Optional)

This step uploads summary statistics and insights to a Google Sheet. Make sure you have your **service account JSON** file and proper access.

1. Place your service account JSON file in the root folder of the project.
2. Share your Google Sheet with the **service account email**.
3. Run the script:

```bash
python export_to_gsheet.py
