#additonal math commands in python

#Plain old division
print(5/2)
#division - returning an integer value
print(5//2)
#division for the remainder only
print(5%2)

#exponentation
print('Exponentiaton')
print(2**3)
print(0**4)

#order of operations
a=7
b=6
c=10
print(a*b+c)
print(a*(b+c))
print(a**b +c)

#data types
myvar = 0
print(type(myvar))

somevar = True
print(type(somevar))

#printing with formatting
someval = 9202.3434
print('the number is:' , + format(someval,'.3f' ))
#adding a comma to the format will have it show comma separators
print('the number is: ', format(someval,',.2f' ))
someotherval = 2344.55892
print('both numbers are: ', format(someval,',.2f' ),format(someotherval,'.2f' ) )
#one last example
someint = 23344
print(format(someint, ',d'))

#escape characters
#\n will have the print skip a line
print('investor 1\ninvestor 2\ninvestor 3')
print("this will allow us print a \" that won't mess up the line" )

#if then
if a==5:
    print('yes it is 5')
else:
    print('sorry, it is not 5')

#if-elseif
mynumb = 200
if mynumb > 1000:
    print("we have a big number")
elif mynumb >= 700:
    print('big, but not that big')
elif mynumb >= 500:
    print('not too big at all')
else:
    print('pretty small')

#testing with booleans
a= True
if a == True:
    print("it's true")
if a:
    print("see this works")
#multiple conditions

a= 10
b= 7
if a==7 and b==10:
    print('both conditions are true')
else:
    print('both conditions are not true')

a= 10
b= 7
if a==10 or b==8:
    print('one or both conditions are true')
else:
    print('neither conditions are true')

a= True
b=True
if a and b:
    print("both are true")
else:
    print("both are not true")
#futher examples
var1 = 'cat'
var2 = 'Cat'
if var1 == var2:
    print('they are equal')
else:
    print('they are not equal')

#convert to upper case - using a built in python function
#python is case senstive
var1 = 'cat'
var2 = 'Cat'
if var1.upper() == var2.upper():
    print('they are equal')
else:
    print('they are not equal')

#getting an average of 5 different numbers
var1 = 10
var2 = 20
var3 = 30
var4 = 40
var5 = 50

tot = var1 + var2 + var3 + var4 + var5
print ('the average is: ' + tot/5)
#uh oh - we get an error?
#why? the print statement can not print out different types
# of data
#we can fix using the str() statment. this will convert the
# integer to a string
print ('the avg is: ' + str(tot/5))

#how would we test if a number is even or not?

#using the math library
#square root, trig functions, degrees and radians
import math
#we can use square root, trig functions etc

#how to determine if a number is even or odd

#how to determine if a numnber is a perfect square or not?

thenum = 26
inp = math.sqrt(thenum)
check = inp**2

if thenum  == check:
    print('its a perfect square')
else:
    print('not a perfect square')


#working with hierachy of conditions
#imagine three random numbers
import random as rd
a = rd.randint(1,100)
b = rd.randint(1,100)
c = rd.randint(1,100)

if (a>b and c> 50) or (c> 60):
    print ('condition is true')
    print ('a: ' + str(a))
    print ('b: ' + str(b))
    print ('c: ' + str(c))
else:
    print('condition is false')
    print('a: ' + str(a))
    print('b: ' + str(b))
    print('c: ' + str(c))