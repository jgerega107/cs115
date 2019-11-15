DATABASE = "musicrecplus.txt"
#main program loop
def main():
    userdb = loadusers()
    username = input("Enter your name (put a $ symbol after your name if you wish your preferences to remain private):")
    prefs = readusers(username, userdb)
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
            prefs = enterpreferences(username, userdb)
        if choice == "q":
            savepreferences(username, prefs, userdb, DATABASE)
    # if choice == blah then do said action

#background functions
def loadusers():
    file = open(DATABASE, 'r')
    userfile = {}
    for line in file:
        [username, artists] = line.strip().split(":")
        artistList = artists.split(",")
        artistList.sort()
        userfile[username] = artistList
    file.close()
    return userfile

def readusers(username, userdb):
    newPref = ""
    prefs = []
    #new user, ask for recommendations
    if username not in userdb:
        while True:
            newPref = input("Enter an artist that you like (Enter to finish):")
            if not newPref:
                break
            else:
                prefs.append(newPref.strip().title())
    prefs.sort()
    return prefs

def savepreferences(userName, prefs, userMap, fileName):
    userMap[userName] = prefs
    file = open(fileName, "w")
    for user in userMap:
        toSave = str(user) + ":" + ",".join(userMap[user]) + \
                    "\n"
        file.write(toSave)
    file.close()

#begin menu items
def enterpreferences(username, userdb):
    newPref = ""
    prefs = []
    while True:
        newPref = input("Enter an artist that you like (Enter to finish):")
        if not newPref:
            savepreferences(username, prefs, userdb, DATABASE)
            break
        else:
            prefs.append(newPref.strip().title())
    prefs.sort()
    return prefs

if __name__ == "__main__": main()