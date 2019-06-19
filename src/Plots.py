"""

# Author: Abhishek Mishra
# MTech Student
# IIT Ropar
# Entry Number- 2018CSM1002

"""
import src.GraphPlot
import src.Reader


# Created object for plots and Reader
plot = src.GraphPlot.Plots()
reader = src.Reader.Helper()

normalHR = reader.readHeartRatesFromFile(0)
abnormalHR = reader.readHeartRatesFromFile(1)


''
#print(normalHR)
plot.plot3DGraph(normalHR[: , 0 ], normalHR[: , 1 ], normalHR[: , 2 ],abnormalHR[: , 0 ], abnormalHR[: , 1 ], abnormalHR[: , 2 ], "HR A", 'HR B', 'HR C', 'Heart Rate')

#print(normalHR)
normalHR = reader.readRespFromFile(0)
abnormalHR = reader.readRespFromFile(1)
plot.plot3DGraph(normalHR[: , 0 ], normalHR[: , 1 ], normalHR[: , 2 ],abnormalHR[: , 0 ], abnormalHR[: , 1 ], abnormalHR[: , 2 ], "Resp A", 'Resp B', 'Resp C', 'Resp')

normalHR = reader.readOxygenFromFile(0)
abnormalHR = reader.readOxygenFromFile(1)
plot.plot3DGraph(normalHR[: , 0 ], normalHR[: , 1 ], normalHR[: , 2 ],abnormalHR[: , 0 ], abnormalHR[: , 1 ], abnormalHR[: , 2 ], "Oxy A", 'Oxy B', 'Oxy C', 'Oxy')

normalHR = reader.readBPFromFile(0)
abnormalHR = reader.readBPFromFile(1)
plot.plot3DGraph(normalHR[: , 0 ], normalHR[: , 1 ], normalHR[: , 2 ],abnormalHR[: , 0 ], abnormalHR[: , 1 ], abnormalHR[: , 2 ], "BP A", 'BP B', 'BP C', 'BP')