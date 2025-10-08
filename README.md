Make sure Python 3.11+ is installed.

Create a virtual environment (optional but recommended):

python -m venv venv


Activate it:

Windows: venv\Scripts\activate

Mac/Linux: source venv/bin/activate

Install dependencies:

pip install -r requirements.txt

pandas
matplotlib
seaborn
plotly
gspread
gspread_dataframe

3️⃣ Prepare Data

If you already have JSON files (zepto.json, blinkit.json, instamart.json) in data/raw/, you can skip scraping.

Otherwise, run the scrapers to generate JSON files:

python scrapers/zepto.py
python scrapers/blinkit.py
python scrapers/instamart.py


Ensure each scraper outputs a JSON file to data/raw/ (without qty, unit, weight_grams, url if not needed).

4️⃣ Process Data

Merge and clean all platform data using processing.py.

python processing.py


This script should:

Load all JSON files

Combine them into a single DataFrame

Calculate derived columns like price_per_100g if needed

Save cleaned/combined data as a CSV or keep in memory for the dashboard

5️⃣ Run the Dashboard

Run dashboard.py to see all visualizations:

python dashboard.py


The dashboard includes:

Price Comparison Table

Best Deals Count per Platform

Platform-specific Visualizations:

Average Price per Brand

Number of Products per Brand

Price Distribution

Premium vs Budget Products, etc.

Make sure your processed data is available for the dashboard to read.

6️⃣ Export to Google Sheets (Optional)

Make sure you have service_account.json in the root folder.

Share the Google Sheet with the service account email (xxxxx@xxxxx.iam.gserviceaccount.com) with Editor access.

Edit export_to_gsheet.py with your sheet name:

sheet_name = "Quick Commerce Summary"


Run:

python export_to_gsheet.py


This will export summary statistics and insights into the Google Sheet.

Troubleshooting:

403 Error → Check if Sheets and Drive APIs are enabled in Google Cloud Console.

SpreadsheetNotFound → Make sure the sheet exists and the service account has access.

Quota exceeded → Free up space in your Google Drive.

7️⃣ Order of Execution

(Optional) Run scrapers if JSON files don’t exist:

python scrapers/zepto.py
python scrapers/blinkit.py
python scrapers/instamart.py


Process data:

python processing.py


Run dashboard:

python dashboard.py


Export to Google Sheets (optional):

python export_to_gsheet.py


✅ Tips for smooth running

Always keep the JSON files updated in data/raw/.

If you add a new platform, just create a new scraper and place the JSON in data/raw/.

Ensure platform-specific visualizations read from the combined DataFrame.

For Google Sheets, use a dedicated service account to avoid quota issues.

If you want, I can make a one-page “Run Guide” diagram showing all scripts and data flow visually. It will make it super easy to hand over or refer back.
