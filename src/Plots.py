'''
Created on 16-Jun-2019

@author: Abhishek Mishra
'''

import src.GraphPlot
import src.Reader


# Created object for plots and Reader
plot = src.GraphPlot.Plots()
reader = src.Reader.Helper()

normalHR = reader.readHeartRatesFromFile(0)
abnormalHR = reader.readHeartRatesFromFile(1)
