#Handling for loops

#create a list to iterate over

numberList = [10,4,20,50,100]

#iterate thro the list
for number in numberList:
    #use "number" name as an identifier for the values in the list
    #Note the indentation
    print number,
print ""

#Iterate through a range of numbers using range() method
for i in range(0,100):
    #print the count from 0->99
    #can be achieved by just range(100)
    #other ranges can be generated as range(10,100) will create a count [10,11,12........99]
    print i,

print ""

#using nested for loops
#creating multiDimMatrix = [[0,1,2],[3,4,5],[6,7,8]]
multiDimMatrix = []
for row in range(3):
    #iterate thro rows
    multiDimMatrix.append([])
    for col in range(3):
        #going thro columns and setting values
        #try to understand what the append() expression is doing
        multiDimMatrix[row].append(col+row*3)

print multiDimMatrix



#using xrange can also be used
#it's more efficient memory management, because instead of creating and storing the list
#it evaluates it lazily, i.e as required

for count in xrange(10):
    print count,
