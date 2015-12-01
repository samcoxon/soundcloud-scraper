import soundcloud
import urllib2
from time import localtime, strftime
import csv
import os

# Create a new client that uses the user credentials oauth flow
client = soundcloud.Client( client_id='9538533753e11862b9ecab64f80feffa',
                            client_secret='665b784dcc9898a27d46db1c941cdc72',
                            username='Ayrak94',
                            password='campbell007')


myArtistDict = {};
artistIdList = [24969134];
followedByDict = {}

# create a dict of artists being followed by client
# matching id's to permalinks
for artist in client.get('/me/followings'):
    myArtistDict[artist.id] = artist.permalink;

# sort the list of followings IDs in ascending order
# artistIdList = sorted(artistIdList, key=int)

def FindFollowings(artistDict):
    for artist in artistDict.keys:
    #myArtistDict.keys()
        followings = client.get('/users/' + str(artist) + '/followings', order = 'created_at', limit=100)
        for following in followings:
            if following.followers_count > 1000:
                artistDict[following.id] = following.permalink
                if (!followedByDict[following.id].contains(artist))
                    followedByDict[following.id].append(artist)

        # start paging through results, 100 at a time
        followings = client.get('/users/' + str(artist) + '/followings', order = 'created_at', limit=100, linked_partitioning=1)
        try:
            while followings.next_href:
                for following in followings.collection:
                    if following.followers_count > 1000:
                        artistDict[following.id] = following.permalink
                        followedByDict[following.id].append(artist)
                followings = client.get(followings.next_href)
        except AttributeError:
            for following in followings.collection:
                    if following.followers_count > 1000:
                        artistDict[following.id] = following.permalink
                        followedByDict[following.id].append(artist)
    return




# print len(followedByDict.items())
# artistFollowIdList = list(set(artistFollowIdList))
# print len(artistFollowIdList)

date = strftime("%d%b", localtime())

keys = followedByDict.keys()
with open("artistfollows" + date + ".csv", 'wb') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerow(artistLikesList)


# 1302738 --- rjd2-1
# 24969134 --- louisthechild
# 198444 --- marcus-marr
# 56231237 --- lightningeagle
# 11908863 --- kasbomusic
# 3201738 --- arca1000000
# 22194235 --- henry-ott
# 162719426 --- sl33pyjvm3s
# 4091150 --- djvanic
# 892605 --- samgellaitry
# 117451218 --- leonbridges
# 29244439 --- donnietrumpet
# 68181 --- sbtrkt
# 788205 --- kaytranada
# 329369 --- skreamizm
# 128082007 --- foreignfamily
# 284803 --- takugotbeats
# 889885 --- bearmountain
# 375 --- futureclassic
# 29257324 --- louisfuton
# 11980254 --- rustyhook
# 4684315 --- djatat
# 6969243 --- chancetherapper
# 1526116 --- jaiwolfmusic
