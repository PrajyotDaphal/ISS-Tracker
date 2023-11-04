import requests
from features.Speak import Say
import matplotlib.pyplot as plt
import cartopy.crs as ccrs   


url = "http://api.open-notify.org/iss-now.json"

r = requests.get(url)

Data = r.json()

dt = Data['timestamp']

lat = Data['iss_position']['latitude']

lon = Data['iss_position']['longitude']

Say(f"Time And date : {dt}")
Say(f"Lantitude: {lat}")
Say(f"Longitude : {lon}")

plt.figure(figsize=(10,8))

ax = plt.axes(projection = ccrs.PlateCarree())

ax.stock_img() # type: ignore

plt.scatter(float(lon),float(lat),color = 'blue' , marker= 'o') # type: ignore

plt.show()