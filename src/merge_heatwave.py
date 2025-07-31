import geopandas as gpd
import pandas as pd

def merge_heatwave_data(
    csv_path="data/heat_days_2023.csv",
    geojson_path="data/countries.geojson",
    output_path="data/countries_heatwave.geojson",
    country_col_geojson="ADMIN",
    country_col_csv="Country",
    heat_col="DaysAbove35C"
):
    # Load country polygons
    countries = gpd.read_file(geojson_path)

    # Load heatwave data CSV
    heat_data = pd.read_csv(csv_path)

    # Merge on country name
    merged = countries.merge(
        heat_data,
        left_on=country_col_geojson,
        right_on=country_col_csv,
        how="left"
    )

    # Fill missing heat data with zero
    merged[heat_col] = merged[heat_col].fillna(0)

    # Save merged GeoJSON
    merged.to_file(output_path, driver="GeoJSON")
    print(f"Saved merged GeoJSON to {output_path}")

if __name__ == "__main__":
    merge_heatwave_data()
