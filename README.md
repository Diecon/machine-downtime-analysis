**Machine Downtime Analysis**

Project Context

This analysis is based on a case study from the Deloitte Data Analytics Virtual Experience Program (Forage). The task simulates analyzing telemetry data to identify operational downtime across manufacturing factories.

Objective

Analyze industrial telemetry data to identify factories and machine types responsible for the highest operational downtime.

Tools

Python
Pandas
Matplotlib

Key Findings

• Daikibo Seiko factory recorded the highest downtime (480 minutes).
• LaserWelder machines contribute the majority of downtime events.
• Shenzhen factory experiences significant downtime mainly from LaserCutter machines.
• Device failures are concentrated in a small number of machine types.

Approach

1. Flatten nested JSON telemetry data using pandas.
2. Perform feature engineering to compute machine downtime.
3. Aggregate downtime metrics by factory and device type.
4. Visualize results using Matplotlib.

Dataset

This project uses telemetry data provided as part of the Deloitte Data Analytics Virtual Experience Program (Forage).
The dataset contains telemetry logs from industrial machines across multiple Daikibo factories.
Each log records machine status (healthy/unhealthy), temperature readings, and location metadata such as factory, city, and section.



