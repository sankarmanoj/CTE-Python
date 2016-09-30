#dealing with if-elif-else statements

number = 10
#check if the number is 20
# "==" to check if two values are same
if number == 20:
    print "Number = 20"
else:
    print "Some other number"

#check if number is 20 or 10
# or evaluates true if either conditions are true
if number == 20 or number == 10:
    print "Number is either 20 or 10"
else:
    print "Some other number"

#check if number is a multiple of 10

number = 50

# '%' operator to calculate remainder on division
if number % 10 == 0:
    print str(number) + " is a multiple of 10"
else:
    print "Number not a multiple of 10"

#if it's a multiple of ten, if it's not then a multiple of 3
number = 21

if number % 10 == 0:
    print str(number) + " is a multiple of 10"
#else if condition to check alternative condition
#multiple of such can be added
elif number % 3 == 0:
    print str(number) + " is a multiple of 3"
else:
    print "Number not a multiple of 10 or 3"



#if a multiple of 10 then only check if it is less than 100

number = 90
if number % 10 == 0:

    print str(number) + " is a multiple of 10",
    #nested if condition
    if number < 100:
        print "and Less than 100"
    else:
        print "and Greater than 100"
else:
    print "Number not a multiple of 10"
