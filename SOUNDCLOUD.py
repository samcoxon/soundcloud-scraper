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
artistLikesList = {}
artistFollowIdList = []

# create a dict of artists being followed by client
# matching id's to permalinks
# for artist in client.get('/me/followings'):
#     myArtistDict[artist.id] = artist.permalink;

# sort the list of followings IDs in ascending order
# artistIdList = sorted(artistIdList, key=int)

# for person in artistIdListTEST:
#     for followings in client.get('/users/' + str(person) + '/followers'):
#         print followings.id

for artist in artistIdList:
#myArtistDict.keys()
    followings = client.get('/users/' + str(artist) + '/followings', order = 'created_at', limit=100)
    for following in followings:
        if following.followers_count > 5000:
            artistLikesList[following.id] = following.followers_count

    # start paging through results, 100 at a time
    followings = client.get('/users/' + str(artist) + '/followings', order = 'created_at', limit=100, linked_partitioning=1)
    try:
        while followings.next_href:
            for following in followings.collection:
                if following.followers_count > 5000:
                    artistLikesList[following.id] = following.followers_count
            followings = client.get(followings.next_href)
    except AttributeError:
        for following in followings.collection:
                if following.followers_count > 5000:
                    artistLikesList[following.id] = following.followers_count

print len(artistLikesList.items())
artistFollowIdList = list(set(artistFollowIdList))
print len(artistFollowIdList)

date = strftime("%d%b", localtime())

keys = artistLikesList.keys()
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
# 67404771 --- kenny-frank
# 11165154 --- sethsentry
# 5363423 --- jameschatburn
# 277945 --- thegeek
# 11968208 --- zwaite321
# 120669165 --- king-of-palaisvert
# 2321697 --- davidpowell-1
# 2019686 --- tommisch
# 17480539 --- thisiscarmody
# 36266728 --- adultjazz
# 128264288 --- venusmtl
# 34647784 --- sophie_oh
# 592907 --- shigeto
# 416928 --- manilakilla
# 6458238 --- iamganz
# 21008200 --- king-krule
# 8785670 --- bustyandthebass
# 26013845 --- george-maple
# 54933731 --- dbrods
# 90341893 --- fnierho
# 9372589 --- sony-classical
# 97682528 --- nnaarchese
# 311257 --- sunmonx
# 76149067 --- spicyvibe
# 752705 --- platform
# 32204901 --- jakubimusic
