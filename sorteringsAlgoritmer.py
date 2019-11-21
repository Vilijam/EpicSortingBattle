def insertionSort(list):

    #Kopier liste til sortering.
    tempList = list.copy()
    
    #Går i gennem hvert element i listen, bortset fra det første, da funktionen sammenligner baglæns, og der er ikke noget element bag det første.
    for i in range(1, len(tempList)):
        #Sammenligner baglæns.
        if tempList[i] < tempList[i-1]:
            #Gemmer det tal, som bryder sorteringen
            num = i
            #Denne while-løkke skifter tal, så længe "num" er mindre end det tal bag det.
            while tempList[num] < tempList[num-1]:
                tempChar = tempList[num]
                tempList[num] = tempList[num-1] 
                tempList[num-1] = tempChar
                #Efter hvert skift skal sammenligningspunktet rykkes et element tilbage. Det gør denne operation.
                num = num - 1
                #Sikre at sammenligningspunktet ikke bliver negativt, når listen er sorteret.
                if num == 0:
                    break

    return tempList

def selectionSort(list):

    #Kopier liste til sortering.
    tempList = list.copy()
        
    #for-løkke til at sortere hvert element i listen.
    for e in range(0, len(tempList)):

        #Definerer, og nulstiller efter forrige sortering, variable til laveste usorteret element.
        lowNum = tempList[e]
        lowNumID = e

        #Sammenligner hvert element med alle andre usorterede elementer.
        for i in range(e, len(tempList)):

            #if-løkke til at finde det laveste usorterede element
            if tempList[i] < lowNum:
                lowNum = tempList[i]
                lowNumID = i

        #Skifter det laveste usorterede element og det element, som det bliver sammenlignet med. 
        tempChar = tempList[e]
        tempList[e] = tempList[lowNumID] 
        tempList[lowNumID] = tempChar

    return tempList


def bubbleSort(list):
    #Først kopierer jeg listen der skal sorteres, og opretter variable der skal bruges under sortering.
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
    #Først opretter jeg variable til funktionen, en kopi af listen der skal sorteres, en liste der er sorteret og en liste der kan samles med templist
    templist = list.copy()
    secondarylist = []
    sortedlist = []
    #Så splittes templist, og templist og secondarylist sættes nu til hver af de to nye lister
    res = split(templist)
    templist = res[0]
    secondarylist = res[1]
    #Nu bruges en if-sætning, som tjekker om længden af templist er lig 1
    if len(templist) == 1:
        #Hvis dette er tilfældet må listen være sorteret, og også secondarylist, siden de er lige lange
        #Derfor samles de nu med merge, og sortedlist sættes nu til dette.
        sortedlist = merge(templist, secondarylist)
    #Nu tjekkes om længden af den sorterede liste er lig med længden på listen der skulle sorteres. Hvis dette passer returneres den sorterede liste
    if len(list) == len(sortedlist):
        return sortedlist
    #Ellers kalder man mergeSort på hver af de to lister, templist og secondary list, samler dem, og gemmer dem i den sorterede liste
    else:
        list1 = mergeSort(templist)
        list2 = mergeSort(secondarylist)
        sortedlist = merge(list1, list2)
        #Til sidst returneres den sorterede liste
        return sortedlist

def split(list):
    #Dette er en hjælpefunktion til mergeSort, som modtager en liste og splitter den op i to lige store lister og returnerer disse
    #Hvis listen har et ulige antal elementer, vil det være den første af de to returnerede lister som har det ekstra element
    #Først oprettes variabler til funktionen, en kopi af listen der skal splittes, og de to lister den skal splittes op i
    #Derudover er der en konstant som er sat til halvdelen af listens længde og et integer der bruges til at sørge for at løkken køres den korrekte mængde
    templist = list.copy()
    list1 = []
    list2 = []
    length = len(templist)/2
    e = 0
    #Her er der en while-løkke der kører så længe e er mindre end length-konstanten, og per gennemkørsel rykker et element fra listen over i den første retur-liste
    #Derefter bliver der lagt 1 til e, så der holdes styr på hvor mange gange løkken har kørt
    while e < length:
        list1.append(templist[0])
        del templist[0]
        e += 1
    #Derefter er der en while-sætning der kører så længe der er elementer i den originale liste
    #Løkken flytter resten af elementerne i den originale liste over i den anden retur-list
    while len(templist) > 0:
        list2.append(templist[0])
        del templist[0]
    #Til sidst returneres de to lister
    return list1, list2

	
def merge(list1, list2):
    #Dette er en hjælpefunktion til mergeSort, som modtager to sorterede lister som parametre, og returnerer en sorteret liste med begge listers elementer
    #Først oprettes variabler til funktionen, listen elementerne skal samles i, og kopier af de to lister der skal samles.
    listMerged = []
    templist1 = list1.copy()
    templist2 = list2.copy()
    #Der er nu en while-løkke, som kører så længe der er elementer i begge de to lister der skal samles
    while len(templist1)>0 and len(templist2)>0:
        #Så tjekkes hvilke af de to første elementer der er mindst, og tilføjer dette element til den samlede liste, mens elementet slettes fra den originale liste
        if templist1[0]<templist2[0]:
            listMerged.append(templist1[0])
            del templist1[0]
        else:
            listMerged.append(templist2[0])
            del templist2[0]
    #Når en af listerne er tomme, tjekkes det hvilken af de to lister der er elementer tilbage i, og den listes elementer tiløjes nu til den samlede liste
    if len(templist1)>0:
        for e in range(len(templist1)):
            listMerged.append(templist1[e])
    else:
        for e in range(len(templist2)):
            listMerged.append(templist2[e])
    #Til sidst returneres den samlede liste
    return listMerged