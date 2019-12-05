import sorteringsAlgoritmer, random

def testList(f):
    l = []
    print("\n"+f.__name__)
    for i in range(1000):
        l.append(random.randint(0, 1000))
    sortedl = f(l)
    timsortl = sorted(l)
    print(str(eval(str(timsortl)+"=="+str(sortedl))))
    print(str(eval(str(timsortl)+"=="+str(l))))


testList(sorteringsAlgoritmer.mergeSort)
testList(sorteringsAlgoritmer.bubbleSort)
testList(sorteringsAlgoritmer.selectionSort)
testList(sorteringsAlgoritmer.insertionSort)

def testFakeList(f):
    l = [2, "fk", True, 2.3, {"a":0, "b":2, "c":3}, [0,2,3,4,1,5]]
    print("\n"+f.__name__)
    try:
        sortedl = f(l)
    except:
        print("Kan ikke sortere listen")



testFakeList(sorteringsAlgoritmer.mergeSort)
testFakeList(sorteringsAlgoritmer.bubbleSort)
testFakeList(sorteringsAlgoritmer.selectionSort)
testFakeList(sorteringsAlgoritmer.insertionSort)

def testWrongData(f):
    d = {"a":0, "b":2, "c":3}
    i = 53
    s = "halloj"
    b = True
    fl = 2.3
    print("\n"+f.__name__)
    try:
        f(d)
    except:
        print("Kan ikke sortere dict")
    try:
        f(i)
    except:
        print("Kan ikke sortere int")
    try:
        f(s)
    except:
        print("Kan ikke sortere str")
    try:
        f(b)
    except:
        print("Kan ikke sortere boolean")
    try:
        f(fl)
    except:
        print("Kan ikke sortere float")

testWrongData(sorteringsAlgoritmer.mergeSort)
testWrongData(sorteringsAlgoritmer.bubbleSort)
testWrongData(sorteringsAlgoritmer.selectionSort)
testWrongData(sorteringsAlgoritmer.insertionSort)
