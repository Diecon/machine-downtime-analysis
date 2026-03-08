**Machine Downtime Analysis**


_**Project Context**_

This analysis is based on a case study from the Deloitte Data Analytics Virtual Experience Program (Forage). The task simulates analyzing telemetry data to identify operational downtime across manufacturing factories.

_**Objective**_

Analyze industrial telemetry data to identify factories and machine types responsible for the highest operational downtime.

_**Tools**_

1. Python
2. Pandas
3. Matplotlib

_**Key Findings**_

1. Daikibo Seiko factory recorded the highest downtime (480 minutes).
2. LaserWelder machines contribute the majority of downtime events.
3. Shenzhen factory experiences significant downtime mainly from LaserCutter machines.
4. Device failures are concentrated in a small number of machine types.

_**Approach**_

1. Flatten nested JSON telemetry data using pandas.
2. Perform feature engineering to compute machine downtime.
3. Aggregate downtime metrics by factory and device type.
4. Visualize results using Matplotlib.

_**Dataset**_

This project uses telemetry data provided as part of the Deloitte Data Analytics Virtual Experience Program (Forage).
The dataset contains telemetry logs from industrial machines across multiple Daikibo factories.
Each log records machine status (healthy/unhealthy), temperature readings, and location metadata such as factory, city, and section.

_**How to Run**_

1. Extract the dataset zip file.
2. Ensure the dataset is in the same directory as the script.
3. Run the analysis:

python machine_downtime_analysis.py


