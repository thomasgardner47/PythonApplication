#define function called bubbleSort below, and accept argument called myList
def bubbleSort (myList):
    #the length of numbers in my list and the number of items in the list - 1
    for i in range (0, len(myList) - 1):
        # J being the range of the list and 0 to -1 length being the length of the list
        for j in range(0, len(myList) - 1 - i):
            #inside the inner loop we will compare the item with the item its right
            # and if the item on the right is larger then the item on the left it will swap places
            if myList[j] > myList[j+1]:
                myList[j], myList[j+1] = myList[j+1],myList[j]
        return myList
    
theList = ['1', '5', '3', '2', '4', '6']
print (bubbleSort(theList))