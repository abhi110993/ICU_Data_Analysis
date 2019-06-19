"""

# Author: Abhishek Mishra
# MTech Student
# IIT Ropar
# Entry Number- 2018CSM1002

"""
import src.Reader


# Created object for plots and Reader
reader = src.Reader.Helper()

normalData = reader.readAllParametersFromFile(0);
print('Previous Normal Data Shape:', normalData.shape)

normalData = reader.featureTransformToDegree2(normalData)
print('After feature transformation Normal Data Shape:'  , normalData.shape)

abNormalData = reader.readAllParametersFromFile(0);
print('Previous Abnormal Data Shape:'  , abNormalData.shape)

abNormalData = reader.featureTransformToDegree2(abNormalData)
print('After feature transformation Abnormal Data Shape:'  , abNormalData.shape)

reader.writeDataIntoCSVFile(normalData,"NormalDeg2.csv")
reader.writeDataIntoCSVFile(normalData,"AbnormalDeg2.csv")

'''
normalData = reader.featureTransformToDegree3(normalData)
print(normalData.shape)
'''