from src.download import download_era5_max_temp
from src.process import count_hot_days
from src.aggregate import aggregate_by_country

year = 2022
download_era5_max_temp(year)
hot_days = count_hot_days(f"data/era5_max_temp_{year}.nc", threshold_c=35)
df = aggregate_by_country(hot_days)
df["Year"] = year
df.to_csv(f"data/heat_days_{year}.csv", index=False)
