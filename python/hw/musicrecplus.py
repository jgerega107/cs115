DATABASE = "musicrecplus.txt"
#main program loop


def main():
    userdb = loadUsers()
    username = input("Enter your name (put a $ symbol after your name if you wish your preferences to remain private):")
    prefs = readUsers(username, userdb)
    userdb[username] = prefs
    choice = ""
    while choice != "q":
        print("Enter a letter to choose an option:")
        print("e - Enter preferences")
        print("r - Get recommendations")
        print("p - Show most popular artists")
        print("h - How popular is the most popular")
        print("m - Which user has the most likes")
        print("q - Save and quit")
        choice = input()
        if choice == "e":
            prefs = enterPreferences(username, userdb)
            userdb[username] = prefs
        elif choice == "r":
            getRecommendations(username, prefs, userdb)
        elif choice == "p":
            findMostPopularArtists(userdb)
        elif choice == "h":
            findMostPopularArtistHitCount(userdb)
        elif choice == "m":
            findMostLikesUser(userdb)
        elif choice == "q":
            savePreferences(username, prefs, userdb, DATABASE)

def loadUsers():
    try:
        file = open(DATABASE, 'r')
    except:
        file = open(DATABASE, 'w+')
    userfile = {}
    for line in file:
        [username, artists] = line.strip().split(":")
        artistList = artists.split(",")
        artistList.sort()
        userfile[username] = artistList
    file.close()
    return userfile


def readUsers(username, userdb):
    prefs = []
    #new user, ask for recommendations
    if username not in userdb:
        while True:
            print("Enter an artist that you like (Enter to finish):")
            newPref = input()
            if not newPref:
                break
            else:
                prefs.append(newPref.strip().title())
    #existing user
    else:
        prefs = userdb[username]
    prefs.sort()
    return prefs


def savePreferences(userName, prefs, userMap, fileName):
    userMap[userName] = prefs
    file = open(fileName, "w")
    for user in userMap:
        toSave = str(user) + ":" + ",".join(userMap[user]) + \
                    "\n"
        file.write(toSave)
    file.close()


def enterPreferences(username, userdb):
    prefs = []
    while True:
        print("Enter an artist that you like (Enter to finish):")
        newPref = input()
        if not newPref:
            savePreferences(username, prefs, userdb, DATABASE)
            break
        else:
            prefs.append(newPref.strip().title())
    prefs.sort()
    return prefs


def numMatches(list1, list2):
    matches = 0
    i = 0
    j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] == list2[j]:
            matches += 1
            i += 1
            j += 1
        elif list1[i] < list2[j]:
            i += 1
        else:
            j += 1
    return matches


def drop(list1, list2):
    list3 = []
    i = 0
    j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] == list2[j]:
            i += 1
            j += 1
        elif list1[i] < list2[j]:
            i += 1
        else:
            list3.append(list2[j])
            j += 1

    return list3


def getRecommendations(currUser, prefs, userMap):
    bestUser = findBestUser(currUser, prefs, userMap)
    if type(bestUser) is type(None) or userMap[bestUser] is type(None):
        print("No recommendations available at this time.")
    else:
        recommendations = drop(prefs, userMap[bestUser])
        for recommendation in recommendations:
            print(recommendation)


def findBestUser(currUser, prefs, userMap):
    users = userMap.keys()
    bestUser = None
    bestScore = -1
    for user in users:
        if isUserNotPrivate(user) and userMap[user] != prefs:
            score = numMatches(prefs, userMap[user])
            if score > bestScore and currUser != user:
                bestScore = score
                bestUser = user
    return bestUser


def isUserNotPrivate(username):
    lastIndex = len(username)
    if username[lastIndex-1] != "$":
        return True
    return False


def putRecommendationsTogether(userMap):
    addedList = []
    for user in userMap:
        if isUserNotPrivate(user):
            addedList += userMap[user]
    addedList.sort()
    return addedList


def findMostPopularArtistsHelper(artists, hits):
    mostPopularArtists = []
    for artist in artists:
        if artists.count(artist) == hits and artist not in mostPopularArtists:
            mostPopularArtists += [artist]
    return mostPopularArtists


def findMostPopularArtistHitCountHelper(artists):
    highestCount = -1
    for artist in artists:
        count = artists.count(artist)
        if count > highestCount:
            highestCount = count
    return highestCount


def findMostPopularArtists(userMap):
    combinedList = putRecommendationsTogether(userMap)
    hitCount = findMostPopularArtistHitCountHelper(combinedList)
    mostPopularArtists = findMostPopularArtistsHelper(combinedList, hitCount)
    if not mostPopularArtists:
        print("Sorry, no artists found.")
    else:
        for artist in mostPopularArtists:
            print(artist)


def findMostPopularArtistHitCount(userMap):
    combinedList = putRecommendationsTogether(userMap)
    print(findMostPopularArtistHitCountHelper(combinedList))


def findMostLikesUserHelper(userMap):
    highestLikeCount = -1
    for user in userMap:
        if len(userMap[user]) > highestLikeCount and isUserNotPrivate(user):
            highestLikeCount = len(userMap[user])
    return highestLikeCount


def findMostLikesUser(userMap):
    likeCount = findMostLikesUserHelper(userMap)
    mostLikesUserList = []
    for user in userMap:
        if len(userMap[user]) == likeCount and user not in mostLikesUserList and isUserNotPrivate(user):
            mostLikesUserList += [user]
    if not mostLikesUserList:
        print("Sorry, no user found.")
    else:
        for user in mostLikesUserList:
            print(user)


if __name__ == "__main__": main()