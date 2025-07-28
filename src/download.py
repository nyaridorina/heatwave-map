import cdsapi

client = cdsapi.Client()

dataset = 'era5_daily_postprocessed_single_levels'  # Correct dataset for daily max temp

request = {
    'variable': 'maximum_2m_temperature_since_previous_post_processing',
    'year': ['2023'],                   # You can add multiple years, e.g. ['2020','2021']
    'month': [f'{m:02d}' for m in range(1, 13)],  # All months
    'day': [f'{d:02d}' for d in range(1, 32)],    # All days
    'format': 'netcdf',                # Use NetCDF for easy Python processing
}

target = 'era5_max_temp_2023.nc'       # Output filename

client.retrieve(dataset, request, target)
