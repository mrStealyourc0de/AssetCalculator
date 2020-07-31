# write a program that can take any asset and calculate future or past values of that asset (support for dynamic rates)
	# conduct with good programming practices by using the web as a reference

# Ideas:
# - Inflation adjustment (use this feature to compare asset-class performance over time!!)
# - Pay rate to pay off loan in given time
# - Pay rate to keep loan stationary

#to do log: comment value function
# Create assets and applying real-data


# Changelog: 
# - Added support for dynamic interest and deposit rates
# - Added support for constant interest and deposit rates.
# - Seperated object from function
#see latex doc for math calculations of methods

#numpy allows for use of arrays
import numpy as np 

class asset:
	def __init__(self, name, initialValue):
		self.name = name
		self.value = initialValue

	#methods that can be applied to all asset classes
	def deposit(self, deposit):
		self.value = self.value + deposit

	def applyInterest(self, interestRate):
		self.value = self.value * interestRate

#function calculates value over time based on deposit rate and interest rates
def valueOverTime(asset, depositArray, interestRateArray):
	
	""" 
	Conditions
	1) Row-size of the depositArray needs to match column size of interestRateArray unless
	arrays are 1x1 in which case it just treats it as a constant. Check if 0.
	2) if interstRate is 1x1 array (i.e constant) 
	   generate interestRateArray with costant in each slot with the size 1 x columnSize
	"""

	if len(depositArray) != len(interestRateArray[0]):
		print(len(depositArray))
		print(len(interestRateArray[0]))
		return("Error! depositArray row size must match interestRateArray column size.")

	else if len(depositArray) == 1 || len(interestRateArray) == 1:
		if depositArray[0, 0] == 0: 
			valueOverTime = np.array(asset.value)
	else:
		valueOverTime = np.array(asset.value) 

		for event in range(0, len(depositArray)): #end = row size of depositArray
			#events are defined implicitly in depositArray and interestRateArray.
			#Event is given by the row in depositArray and column in interestRateArray

			sumDepositRow = sum(depositArray[event, 0:len(depositArray)])
			asset.deposit(sumDepositRow)
			print(asset.value)
			asset.applyInterest(interestRateArray[0, event])
			valueOverTime = np.append(valueOverTime, asset.value)
		return valueOverTime	

savings = asset("savings-account", 0)

depositArray1 = np.array([[100, 100], [100, 100]])
interestRateArray1 = np.array([[2, 2]])
test = valueOverTime(savings, depositArray1, interestRateArray1)
print(test)