import pandas as pd

def compare_prices(df):
    # Group by normalized product name
    grouped = df.groupby("product_name_clean")
    
    results = []
    for name, group in grouped:
        best = group.loc[group['price_rupees'].idxmin()]
        result = {
            "product_name": group.iloc[0]["product_name"],
            "best_platform": best["platform"],
            "best_price": best["price_rupees"],
            "all_prices": group[["platform", "price_rupees"]].to_dict(orient="records")
        }
        results.append(result)
    
    return pd.DataFrame(results)

if __name__ == "__main__":
    from processing import load_all_platforms
    df_all = load_all_platforms()
    df_compare = compare_prices(df_all)
    print(df_compare.head())
