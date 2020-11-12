import os
import pandas as pd
from transform import *

cwd_dir = os.getcwd()

data_dir = os.path.join(cwd_dir, "data", "gps_data_ground.csv")

df = pd.read_csv(data_dir)

transform = Transform()

result = pd.DataFrame(columns=["latitude", "longitude", "altitude"])

latitude = []
longitude = []
altitude = []

for i in range(len(df)):
    lat, lon, alt = transform.exec(df["Latitude"].values[i], df["Longitude"].values[i])
    latitude.append(lat)
    longitude.append(lon)
    altitude.append(alt)

result.to_csv("result.csv")
