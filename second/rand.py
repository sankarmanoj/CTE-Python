import random
import copy
randomArray = [random.randint(0,100) for x in range(10)]
print "Random Array =",randomArray

#Sort Array
randomArray.sort()
print "Sorted Array = ",randomArray

#Largest Element
print "Largest Element In Array = ",max(randomArray)

#Smallest Element
print "Smallest Element in Array = ",min(randomArray)


#Create New Array From the Existing Array
newArray = randomArray

anotherArray = newArray[:]
# anotherArray = copy.deepcopy(randomArray)
anotherArray = list(randomArray)
#Update Starting Value
newArray[0]=666
#Print Old Array
print "randomArray =",randomArray," newArray = ",newArray

#Update Starting Value
anotherArray[1]=333
#Print Old Array
print "randomArray =",randomArray," anotherArray = ",anotherArray
