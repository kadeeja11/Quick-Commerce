# run.py
import os
import subprocess

# Step 1: Process data (optional: prints head)
from processing import load_all_platforms
df_all = load_all_platforms()
print(f"Loaded {len(df_all)} total bread items.")

# Step 2: Run analysis
from analysis import compare_prices
df_compare = compare_prices(df_all)
print("Top 5 products with best deals:")
print(df_compare.head())

# Step 3: Launch Streamlit dashboard
print("Launching Streamlit dashboard...")
subprocess.run(["streamlit", "run", "dashboard.py"])
