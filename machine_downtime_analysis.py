import pandas as pd

#1. reads json file as data frame
telemetry_data = pd.read_json("daikibo-telemetry-data.json")

#2. data(json) flattening  -  this extracts status and temperature from nested dictionary
data_expanded = pd.json_normalize(telemetry_data["data"])

#3. column data is deleted from original dataframe and remaining columns are concatenated with status & temperature - stored in data_expanded
telemetry_data = pd.concat([telemetry_data.drop(columns=["data"]),data_expanded],axis=1)
print(telemetry_data)

#4. downtime is calculated using lamda function (if status is unhealthy returns 10 , if healthy returns 0)
telemetry_data["downtime"] = telemetry_data["status"].apply(lambda x:10 if x == "unhealthy" else 0)
print(telemetry_data["downtime"])

#5.country,city,area,factory,section are extracted from location which contains nested dictionary . concatenated the columns extracted with telemetry data
location_data = pd.json_normalize(telemetry_data["location"])
telemetry_data = pd.concat([telemetry_data.drop(columns=["location"]),location_data],axis=1)
print(telemetry_data)

#6. downtime is calculated by summing the downtime per factory
downtime_per_factory = telemetry_data.groupby("factory")["downtime"].sum()
print(downtime_per_factory.sort_values(ascending=False))

#7. downtime is calculated by summing the downtime per deviceType
downtime_per_device = telemetry_data.groupby("deviceType")["downtime"].sum()
print(downtime_per_device.sort_values(ascending=False))

#8. downtime calculated per factory per deviceType
downtime_per_factory_per_device = telemetry_data.groupby(["factory","deviceType"])["downtime"].sum()
print(downtime_per_factory_per_device.sort_values(ascending=False))

#9. Visualization using matplotlib

import matplotlib.pyplot as plt

downtime_per_factory.sort_values(ascending=False).plot(kind="bar")
plt.title("Downtime per Factory")
plt.xlabel("Factories")
plt.ylabel("Downtime")
plt.show()


downtime_per_device.sort_values(ascending=False).plot(kind="bar")
plt.title("Downtime per Device")
plt.xlabel("Device Types")
plt.ylabel("Downtime")
plt.show()












