import matplotlib

def insertionSort(list):

    listSorted = list.copy()
    
    for i in range(1, len(listSorted)):
        if listSorted[i] < listSorted[i-1]:
            numberSorted = i
            while listSorted[numberSorted] < listSorted[numberSorted-1]:
                switchedString = listSorted[numberSorted]
                listSorted[numberSorted] = listSorted[numberSorted-1] 
                listSorted[numberSorted-1] = switchedString
                numberSorted = numberSorted - 1
                if numberSorted == 0:
                    break

    return listSorted

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
