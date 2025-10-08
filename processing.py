import json
import pandas as pd
from pathlib import Path

def load_all_products():
    data_dir = Path(__file__).parent / "data" / "raw"
    
    files = ["zepto.json", "instamart.json", "blinkit.json"]
    all_data = []
    
    for file in files:
        path = data_dir / file
        if path.exists():
            with open(path, "r", encoding="utf-8") as f:
                all_data.extend(json.load(f))
    
    df = pd.DataFrame(all_data)
    return df
