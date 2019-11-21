import matplotlib

def insertionSort(list):

    tempList = list.copy()
    
    for i in range(1, len(tempList)):
        if tempList[i] < tempList[i-1]:
            num = i
            while tempList[num] < tempList[num-1]:
                tempChar = tempList[num]
                tempList[num] = tempList[num-1] 
                tempList[num-1] = tempChar
                num = num - 1
                if num == 0:
                    break

    return tempList

def selectionSort(list):

    tempList = list.copy()
    lowNumID = 0
        
    for e in range(0, len(tempList)):
        lowNum = tempList[e]
        lowNumID = e

        for i in range(e, len(tempList)):
            if tempList[i] < lowNum:
                lowNum = tempList[i]
                lowNumID = i

        tempChar = tempList[e]
        tempList[e] = tempList[lowNumID] 
        tempList[lowNumID] = tempChar

    return tempList


def bubbleSort(list):
    #Først kopierer jeg listen der skal sorteres og opretter variable der skal bruges under sortering.
	templist = list.copy()
	tempChar = None
	num = 1
    #Jeg laver her to for-løkker, en der kører for hver gang man skal kører listen igennem, 
	for e in range(len(templist)-1):
        #Og en for den mængde elementer den skal sammenligne med hinanden
		for e in range(len(templist)-num):
            #Her er en if-sætning som tjekker om elementet der kigges på er større end elementet der har en højere key.
            #Hvis dette passer byttes deres plads
			if templist[e+1]<templist[e]:
				tempChar = templist[e]
				templist[e] = templist[e+1]
				templist[e+1] = tempChar
        #Til sidst lægges 1 til variablen num, som er med til at bestemme hvor mange elementer der skal tjekkes hver gang listen løbes igennem
		num += 1
    #Til sidst returneres den sorterede liste
	return templist


def mergeSort(list):
    templist = list.copy()
    currentlist = templist.copy()
    secondarylist = []
    sortedlist = []
    res = split(currentlist)
    currentlist = res[0]
    secondarylist = res[1]

    if len(currentlist) == 1:
        sortedlist = merge(currentlist, secondarylist)

    if len(list) == len(sortedlist):
        return sortedlist
    else:
        list1 = mergeSort(currentlist)
        list2 = mergeSort(secondarylist)
        sortedlist = merge(list1, list2)
        return sortedlist

def split(list):
    templist = list.copy()
    list1 = []
    list2 = []
    length = len(templist)/2
    e = 0
    while e < length:
        list1.append(templist[0])
        del templist[0]
        e += 1
    while len(templist) > 0:
        list2.append(templist[0])
        del templist[0]
    return list1, list2

	
def merge(list1, list2):
    listMerged = []
    templist1 = list1.copy()
    templist2 = list2.copy()
    while len(templist1)>0 and len(templist2)>0:
        if templist1[0]<templist2[0]:
            listMerged.append(templist1[0])
            del templist1[0]
        else:
            listMerged.append(templist2[0])
            del templist2[0]
    if len(templist1)>0:
        for e in range(len(templist1)):
            listMerged.append(templist1[e])
    else:
        for e in range(len(templist2)):
            listMerged.append(templist2[e])
    return listMerged