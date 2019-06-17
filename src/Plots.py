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
print(normalHR)
plot.plot3DGraph(normalHR[: , 0 ], normalHR[: , 1 ], normalHR[: , 2 ],abnormalHR[: , 0 ], abnormalHR[: , 1 ], abnormalHR[: , 2 ], "HR", 'HR', 'HR', 'Heart Rate')