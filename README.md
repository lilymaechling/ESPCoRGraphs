# ESPCoRGraphs
## Lily Maechling, June 2020


## Usage
There are three different files for the three different segments of robot movement. Each file has the necesary fucntions to extract data from the csv file and create the appropriate graphs.

### Boathouse to Buoy
The final fucntion in the file named `draw_four_graphs()` will produce four graphs: 
* Depth and Temp
* ODO(mgl), Turbidity, and Depth
* ODO(%sat), Turbidity, and Depth
* Chlorophyll, Conductivity, and Depth

The `draw_four_graphs()` function takes in 13 parameters:
* csv_filename: path to csv file holding data
* date: string date representation for graph title ie. 3/16/20
* start: starting csv row 
* stop: ending csv row
* range: how many total data points
* depth: csv column with depth data
* temp: csv column with temp data
* chloro: csv column with chorophyll data
* odopercent: csv column with ODO(%sat) data
* odomgl: csv column with ODO(mgl) data
* turb: csv column with turbidity data
* echodown: csv column with echosounder depth data (if there is no echosounder data, input '-1')
* confidence: csv column with confidence data (if there is no echosounder data, input '-1')

### Up Down Buoy
The final fucntion in the file named `draw_five_graphs()` will produce five graphs:
* Depth and Temp
* ODO(mgl), Turbidity, and Depth
* ODO(%sat), Turbidity, and Depth
* Chlorophyll, Conductivity, and Depth
* Temp Vs Depth

The `draw_five_graphs()` function takes in 11 parameters:
* csv_filename: path to csv file holding data
* date: string date representation for graph title ie. 3/16/20
* start: starting csv row 
* stop: ending csv row
* range: how many total data points
* depth: csv column with depth data
* temp: csv column with temp data
* chloro: csv column with chorophyll data
* odopercent: csv column with ODO(%sat) data
* odomgl: csv column with ODO(mgl) data
* turb: csv column with turbidity data


### Buoy to Boathouse
The final fucntion in the file named `draw_four_graphs()` will produce four graphs: 
* Depth and Temp
* ODO(mgl), Turbidity, and Depth
* ODO(%sat), Turbidity, and Depth
* Chlorophyll, Conductivity, and Depth

The `draw_four_graphs()` function takes in 13 parameters:
* csv_filename: path to csv file holding data
* date: string date representation for graph title ie. 3/16/20
* start: starting csv row 
* stop: ending csv row
* range: how many total data points
* depth: csv column with depth data
* temp: csv column with temp data
* chloro: csv column with chorophyll data
* odopercent: csv column with ODO(%sat) data
* odomgl: csv column with ODO(mgl) data
* turb: csv column with turbidity data
* echodown: csv column with echosounder depth data (if there is no echosounder data, input '-1')
* confidence: csv column with confidence data (if there is no echosounder data, input '-1')
