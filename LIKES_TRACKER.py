import soundcloud
import csv
import os
from collections import defaultdict

likesDict = defaultdict(list)
ratioDict = {}
ratioList = []
topTen = []
ratioChartDict = {}


for myfile in os.listdir("/Users/SamCoxon/personal_projects/soundcloud_project/Artist_Follows"):

    inputArtistFile = csv.DictReader(open("Artist_Follows/" + myfile))
    for row in inputArtistFile:
        for artist in row.keys():
            likesDict[artist].append(int(row[artist]))

for artist in likesDict.keys():
    beginning = likesDict[artist][0]
    end = likesDict[artist][-1]

    #
    if (float(end)/beginning > 1.20):
       ratioChartDict[beginning] = (float(end)/beginning)

    if (beginning < 15000):
        percentage = ((float(end)/beginning) - 1)/2
        ratioDict[1+percentage] = artist
    elif ( 15000 < beginning < 50000):
        ratioDict[float(end)/beginning] = artist
    else:
        percentage = ((float(end)/beginning) - 1)*2
        ratioDict[1+percentage] = artist

ratioList = ratioDict.keys()
ratioList.sort()
topTen = ratioList[-10:]

# for ratio in topTen:
#     print ratioDict[ratio]

client = soundcloud.Client( client_id='9538533753e11862b9ecab64f80feffa',
                            client_secret='665b784dcc9898a27d46db1c941cdc72',
                            username='Ayrak94',
                            password='campbell007')

# for ratio in topTen:
    # print likesDict[ratioDict[ratio]]
    # artist = client.get('/users/' + ratioDict[ratio])
    # print artist.permalink

print ratioChartDict.keys()
print ratioChartDict.values()


