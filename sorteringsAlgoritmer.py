import matplotlib

def insertionSort(list):

    listSorted = list

    for i in range(0,len(listSorted) - 1)
        if i < i-1
            for
        
        



    pass


def selectionSort(list):

    pass


def bubbleSort(list):
    def bubbleSort(list):
	templist = list.copy()
	tempChar = None
	num = 1
	for e in range(len(templist)-1):
		for e in range(len(templist)-num):
			if templist[e+1]<templist[e]:
				tempChar = templist[e]
				templist[e] = templist[e+1]
				templist[e+1] = tempChar
		num += 1
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