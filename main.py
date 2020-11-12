import os
import numpy as np
import pandas as pd
from transform import *

fname = "gps_data_jaesung.csv"

cwd_dir = os.getcwd()

data_dir = os.path.join(cwd_dir, "data", fname)

df = pd.read_csv(data_dir)

data_len = len(df)

transform = Transform()

result = pd.DataFrame(columns=["latitude", "longitude", "altitude"])

latitude = []
longitude = []
altitude = []

lat_np = np.abs(df["Latitude"].values)
lon_np = np.abs(df["Longitude"].values)

for i in range(data_len):
    coord_np = transform.exec(lat_np[i], lon_np[i], 0)
    latitude.append(coord_np[0])
    longitude.append(coord_np[1])
    altitude.append(coord_np[2])

result["latitude"] = latitude
result["longitude"] = longitude
result["altitude"] = altitude

result_dir = os.path.join(cwd_dir, "result", fname)

result.to_csv(result_dir)