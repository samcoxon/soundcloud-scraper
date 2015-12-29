import soundcloud
import urllib2
from time import localtime, strftime
import csv
import os

# Create a new client that uses the user credentials oauth flow
client = soundcloud.Client( client_id='',
                            client_secret='',
                            username='',
                            password='')


artist_dict = {}
been_checked = {}
is_following = {}


# Create a dict of artists being followed by client
# matching id's to permalinks
# Build a dict matching users to lists of artists they follow

def getFollowings( following_list, min_followers = 5000, follower = 0 ):
    if (is_following.get(follower) is None):
        # initialize list to keep track of followings per follower
        is_following[follower] = []

        # first JSON response
        for artist in following_list.collection:
            if artist.followers_count > min_followers:
                artist_dict[artist.id] = artist.permalink
                # add each artist that is being followed to the list
                is_following[follower].append(artist.id)

        # if more pages of followings scroll through those
        while following_list.next_href:
            following_list = client.get(following_list.next_href)
            for artist in following_list.collection:
                if artist.followers_count > min_followers:
                    artist_dict[artist.id] = artist.permalink
                    is_following[follower].append(artist.id)


# get first collection of results
my_followings = client.get('/me/followings')
getFollowings(my_followings)

# get list of artists followed by artists followed by "me"
for artist in artist_dict.keys():
    followings = client.get('/users/' + str(artist) + '/followings')
    getFollowings(followings, 5000, artist)


# num_artists = len(artist_dict.keys()) + 1
# follow_matrix = [[0 for x in range(num_artists)] for x in range(num_artists)]

# add "me" to artist_dict
artist_dict[0] = "me"

print artist_dict.values()

# for artist in is_following:
#     row_position = artist_dict.keys().index(artist)
#     for followed in is_following[artist]:
#         column_position = artist_dict.keys().index(followed)
#         follow_matrix[row_position][column_position] = 1

# print follow_matrix
# with open("artist_adjacency_matrix.csv", "wb") as f:
#     writer = csv.writer(f)
#     writer.writerows(follow_matrix)

# print (client.get('/users/' + str(29257324))).permalink
# print len(is_following[29257324])
# print len(artist_dict.keys())

# print len(followedByDict.items())
# artistFollowIdList = list(set(artistFollowIdList))
# print len(artistFollowIdList)

date = strftime("%d%b", localtime())

# keys = followedByDict.keys()
# with open("artistfollows" + date + ".csv", 'wb') as output_file:
#     dict_writer = csv.DictWriter(output_file, keys)
#     dict_writer.writeheader()
#     dict_writer.writerow(artistLikesList)


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






# for artist in artist_dict.keys():
# myArtistDict.keys()
#     followings = client.get('/users/' + str(artist) + '/followings', order = 'created_at', limit=100)
#     for following in followings:
#         if following.followers_count > 1000:
#             artist_dict[following.id] = following.permalink
#             if (followedByDict[following.id].contains(artist) == false):
#                 followedByDict[following.id].append(artist)

# # start paging through results, 100 at a time
# followings = client.get('/users/' + str(artist) + '/followings', order = 'created_at', limit=100, linked_partitioning=1)
# try:
#     while followings.next_href:
#         for following in followings.collection:
#             if following.followers_count > 1000:
#                 artist_dict[following.id] = following.permalink
#                 followedByDict[following.id].append(artist)
#         followings = client.get(followings.next_href)
# except AttributeError:
#     for following in followings.collection:
#             if following.followers_count > 1000:
#                 artist_dict[following.id] = following.permalink
#                 followedByDict[following.id].append(artist)

