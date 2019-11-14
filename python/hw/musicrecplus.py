DATABASE = "musicrecplus.txt"
def main():
    userdb = loadusers()
    username = input("Enter your name (put a $ symbol after your name if you wish your preferences to remain private):")
    readusers(username, userdb)

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
    #existing user, goto menu
    if username in userdb:
        showmenu()
    #new user, ask for recommendations
    else:
        while True:
            prefs.append(newPref.strip().title())
            newPref = input("Enter an artist that you like (Enter to finish):")
            if not newPref:
                savepreferences(username, prefs, userdb, DATABASE)
                break
    prefs.sort()
    return prefs

def showmenu():
    print("Enter a letter to choose an option:")
    print("e - Enter preferences")
    print("r - Get recommendations")
    print("p - Show most popular artists")
    print("h - How popular is the most popular")
    print("m - Which user has the most likes")
    choice = input("q - Save and quit")
    #if choice == blah then do said action

def savepreferences(username, prefs, userdb, filename):
    userdb[username] = prefs
    file = open(filename, 'w')
    for user in userdb:
        toSave = str(user) + ":" + ",".join(userdb[user]) + "\n"
        file.write(toSave)
    file.close()

if __name__ == "__main__": main()