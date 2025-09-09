listOfNumbers = [0, 1, 7, 2, 4, 8]
# listOfNumbers = []

listLength = len(listOfNumbers)
summ = 0
i = 0

while i < listLength:
     summ += listOfNumbers[i]
     i += 2

if listLength == 0 :
    print(0)
else :
    print(summ * listOfNumbers[listLength-1])








