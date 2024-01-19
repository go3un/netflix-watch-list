# Ella Kim
# 1/17
# To-do List 2


#Initialize
#mySchedule stores a list of the classes you are currently taking at Jones 
netflixList = ["Squid Game","Suits","The Office","Mad Men","Gilmore Girls"]


#adds a show to the list
def addShow():
    global netflixList
    newShow = input("What show would you like to add? ")
    netflixList.append(newShow)


#remove the selected show
def removeShow():
    global netflixList
    remShow = input("What show would you like to remove? ")
    netflixList.remove(remShow)


#view the list
def viewList():
    global netflixList
    print(netflixList)


#Mark the item as completed
def markComp():
    global netflixList
    markShow = input("What show would you like to mark as completed? ")
    x = netflixList.index (markShow)
    y = netflixList[x] 
    netflixList[x] = ("[X] " + y)


#clear the list
def delList():
    global netflixList
    netflixList.clear()


#print the number of entries on the list
def printNum():
    global netflixList
    print(len(netflixList))


#sorts the list alphabetically
def sortList():
    global netflixList
    netflixList.sort()
    


def accInput():
    while True:
        global netflixList
        print(netflixList)
        player_input = int(input("Would you like to... \n (1) Add a task to the watch list \n (2) View the current watch list  \n (3) Mark a show as completed \n (4) Remove a show from the watch list \n (5) Delete all items \n (6) Check number of items \n (7) Sort list aplhabetically \n (8) Quit \n"))
        if player_input == 1:
            addShow()
        elif player_input == 2:
            viewList()
        elif player_input == 3:
            markComp()
        elif player_input == 4:
            removeShow()
        elif player_input == 5:
            delList()
        elif player_input == 6:
            printNum()
        elif player_input == 7:
            sortList()
        elif player_input == 8:
            break










def final():
    global netflixList
    print(netflixList)


#Main
accInput()