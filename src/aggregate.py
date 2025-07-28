import geopandas as gpd
import rioxarray
from tqdm import tqdm

def aggregate_by_country(dataarray, shapefile="data/countries.shp"):
    dataarray.rio.write_crs("EPSG:4326", inplace=True)
    countries = gpd.read_file(shapefile)

    results = []
    for _, row in tqdm(countries.iterrows(), total=len(countries)):
        name = row["ADMIN"]
        geom = row.geometry
        try:
            clipped = dataarray.rio.clip([geom], countries.crs)
            mean_val = clipped.mean(dim=["latitude", "longitude"]).values.item()
            results.append({"Country": name, "DaysAbove35C": round(mean_val, 2)})
        except Exception:
            continue

    return pd.DataFrame(results)
