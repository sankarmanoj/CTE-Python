#!/usr/bin/env python
array = range(2,32,3) #Create An Array from 2 to 30 Step 3. 30 is exclusive
print array

#Print Square of Each Element in Array
for x in array:
    print x**2
    # print x*x

#Calculate Sum And Average of an Array
total = 0
count = 0
for x in array:
    total+=x
    count+=1
print "Average = ",float(total)/count


#Create List of Only Even Numbers
evenarray = [x for x in array if x%2==0]
print "Even Array = ",evenarray

evenarray.insert(-1,73) # Same as evenarray.append(73,len(evenarray)-2)
print evenarray

evenarray.remove(2) #Removes only the first instance of 2
# while 2 in evenarray :    Removes Every Instance of 2
#   evenarray.remove(2)
