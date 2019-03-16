import csv
import sys

numberOfMonths = 0
totalNetEarnings = 0
bankData = open('PyBank_Resources_budget_data.csv').read().splitlines()
bankData.pop(0)
for item in bankData:
    numberOfMonths += 1
    splitItem = item.split(',')
    earningsVal = splitItem[1]
    earningsVal = int(earningsVal)
    totalNetEarnings = totalNetEarnings + earningsVal

average = totalNetEarnings / numberOfMonths

avgGainLossAccum = 0
max = -sys.maxint - 1
min = sys.maxint

maxMonth = bankData[0].split(',')[0]
minMonth = bankData[0].split(',')[0]
avgVals = 0
for x in range(len(bankData) - 1):
    first = int(bankData[x].split(',')[1])
    second = int(bankData[x+1].split(',')[1])
    avgGainLossAccum += second - first
    avgVals += 1
    if second - first > max:
        max = second - first
        maxMonth = bankData[x+1].split(',')[0]
    if second - first < min:
        min = second - first
        minMonth = bankData[x+1].split(',')[0]


print("Total Months: %d" % (numberOfMonths))
print("Total Earnings: %.2f" % (totalNetEarnings))
print("Average Change: %.2f" % (avgGainLossAccum/float(avgVals)))
print("Greatest Increase in Profits: %s %.2d" % (maxMonth, max))
print("Greatest Increase in Profits: %s %.2d" % (minMonth, min))
