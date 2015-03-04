#!/usr/bin/python3.4
from decimal import *

"""	RANGES					STEPS
	harvest: 1-4 				0.5
	capture
	binding capacity: 80-100 		10
	Flow rate capture: 0.06-0.12 		0.01
	intermediate binding capacity: 20-30 	5
	Polishing binding capacity: 5-10 	2
	Intermediate flow rate: 0.04-0.08 	0.01
	Polishing flow rate: 0.03-0.06 		0.005
"""
#times for equilibration, loading, washing, elution, regeneration, total
def calTime(resinVol, flowRate) :
	result = []
	for i in range(len(flowRate)) :
		result.append(resinVol / flowRate[i])
	return result
	
def calLoadingTime(loadVol, flowRate) :
	result = []
	for i in range(len(loadVol)) :
		for j in range(len(flowRate)) :
			result.append(loadVol[i] / flowRate[j])
	return result
	
def calTotalTime(equilibrationTime, loadingTime, washingTime, elutionTime, regenerationTime, noOfCycles) :
	result = []
	for i in range(len(equilibrationTime)) :
		for j in range(len(noOfCycles)) :
			result.append((equilibrationTime[i] + loadingTime[i] + washingTime[i] + elutionTime[i] + regenerationTime[i]) * noOfCycles[j])
	return result	
	
#def calProductWeight(						 						

#Small Scale Fermentor
#Size
i = 0
hV = 1
harvestVolume = []
while hV < 4.5 : 
	harvestVolume.append(hV)			#1-4 0.5
	hV = hV + 0.5
	i = i + 1

productConcentration = 2

hV = 1
i = 0
productInGrams = []
for i in range(len(harvestVolume)) :	#convert to function
	productInGrams.append(harvestVolume[i] * productConcentration)

time = 168

#Step Process 1
#Load
stepYield = 95				#95%
productProcess1 = []
for i in range(len(productInGrams)) :
	productProcess1.append((stepYield / 100) * productInGrams[i])

#Step Process 2 Capture
#Load
resinVolume = 0.02

resinBindingCapacity = []
rBC = 70
while rBC < 110 :
	resinBindingCapacity.append(rBC)	#?	#70-100 10
	rBC = rBC + 10

loadConcentration = []
for i in range(len(productProcess1)) :
	for j in range(len(harvestVolume)) :
		loadConcentration.append(productProcess1[i] / harvestVolume[j])

loadAmount = []
for i in range(len(resinBindingCapacity)) :
	loadAmount.append(resinVolume * resinBindingCapacity[i])

loadVolume = []
for i in range(len(loadAmount)) :
	for j in range(len(loadConcentration)) :
		loadVolume.append(loadAmount[i] / loadConcentration[j])		

numberOfCycles = []
for i in range(len(productProcess1)) :
	for j in range(len(loadAmount)) :		
		numberOfCycles.append(productProcess1[i] / loadAmount[j])
		
print(numberOfCycles)		

fRC = 0.06
flowRateCapture = []
while fRC < 0.13 :		
	flowRateCapture.append(fRC) 			#0.06-0.12 0.01
	fRC = fRC + 0.01
	
#Process Time	
equilibrationTime = [4 * x for x in calTime(resinVolume, flowRateCapture)]

loadingTime = calLoadingTime(loadVolume, flowRateCapture) #length different from eq Time

washingTime = [4 * x for x in calTime(resinVolume, flowRateCapture)]

elutionTime = [3 * x for x in calTime(resinVolume, flowRateCapture)]

regenerationTime = [2 * x for x in calTime(resinVolume, flowRateCapture)]

totalTime = calTotalTime(equilibrationTime, loadingTime, washingTime, elutionTime, regenerationTime, numberOfCycles)

print()

print(totalTime)
print()
print(len(loadingTime)," ",len(equilibrationTime)," ",len(regenerationTime))
