import json
from pathlib import Path

RAW_JSON_PATH = Path(__file__).parent.parent / "data" / "raw" / "zepto.json"

def load_zepto_json(json_path=RAW_JSON_PATH):
    """Load Zepto products from JSON file."""
    if not json_path.exists():
        print(f"JSON file not found: {json_path}")
        return []

    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    print(f"Loaded {len(data)} Zepto products from {json_path}")
    return data

if __name__ == "__main__":
    products = load_zepto_json()
    # Example: print first 3 products
    for p in products[:3]:
        print(p)
