import csv
# total number votes cast
votes = open('election_data.csv').read().splitlines()
votes.pop(0)


myDict = {}
for x in range(len(votes)):
    splitItem = votes[x].split(',')
    firstName = splitItem[1]
    lastName = splitItem[2]
    if lastName in myDict:
        myDict[splitItem[2]]['voteCount'] += 1
    else:
        myDict[lastName] = { 'voteCount': 1, 'firstName': firstName, 'lastName': lastName}

for x in myDict:  
    lastName = myDict[x]['lastName']
    percent = round(100* myDict[x]['voteCount']/float(len(votes)))
    voteCount = myDict[x]['voteCount']

    print("%s %s %.2f %s %d" % (lastName, ":", percent, "%" , voteCount))