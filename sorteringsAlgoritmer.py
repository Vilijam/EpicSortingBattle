import matplotlib

def insertionSort(list):

    listSorted = list.copy()
    switchedString = None

    for i in range(0,len(listSorted) - 1)
        if listSorted[i] < listSorted[i-1]
            switchedString = listSorted[i]
            listSorted[i] = listSorted[i-1] 
            listSorted[i-1] = switchedString

    return listSorted





    pass


def selectionSort(list):

    pass


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

    pass
