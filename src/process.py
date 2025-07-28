import xarray as xr
import numpy as np
import pandas as pd

def count_hot_days(file_path, threshold_c=35):
    threshold_k = threshold_c + 273.15
    ds = xr.open_dataset(file_path)
    tmax = ds["mx2t"]  # ERA5 variable name for max 2m temp
    daily_hot = (tmax > threshold_k).groupby("time.year").sum(dim="time")
    return daily_hot
