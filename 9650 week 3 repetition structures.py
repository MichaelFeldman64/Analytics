#Repetition structures
# a basic do-while loop

ctr = 1
while (ctr <= 5):
    print("hello world")
    ctr = ctr + 1

#there is a more pythonic way to write this loop:
#this uses an "augmented counter"
ctr = 1
while (ctr <= 5):
    print("hello world")
    ctr += 1  #means take the same variable and add one to it
#what would happen above if we leave out the counter variable?

# for our other example, how would we add up the first 20 numbers?

#intialize our variables or we will get an error the
#first time we access them

ctr= 1
tot = 0

while ctr <=20:
    tot = tot + ctr
    ctr = ctr +1
print('the total is: ' + str(tot))

#running this loop based on input from the user
starti = int(input('Enter a starting number'))
endi = int(input('Enter an ending number'))

tot = 0
ctr = starti

while ctr <= endi:
    tot = tot + ctr
    ctr = ctr +1
print('the total is: ' + str(tot))



#how would we modify the code to return the sum of squares
#of a range of numbers?
#copy the code from above.
print(1+2+3+4+5+6+7+8+9+10)
starti = input('Enter a starting number')
endi = input('Enter an ending number')

tot = 0
ctr = starti

while ctr <= endi:
    tot = tot + (ctr**2)
    ctr += 1
print('the total squares is: ' + str(tot))

#uh oh....we get an error
#the exponentiation is more sensitive and needs integers
#explictly stated
starti = int(input('Enter a starting number'))
endi = int(input('Enter an ending number'))
tot = 0
ctr = starti

while ctr <= endi:
    tot += ctr**2
    ctr += 1
print('the total squares is: ' + str(tot))
print((1**2) + (2**2) + (3**2) + (4**2) + (5**2))

#the basic for loop
#this will print out the values in the []
for n in [10,14,15,17,18]:
    print (n)

#we can also supply a range of values
#this will print from 1-9
for n in range(1,10):
    print (n)

#also can be run with characters
for x in ['a','b','c','d']:
    print(x)

#rewriting the sum of squares with a for loop
tot = 0
for i in range (1,21):
    tot += i**2
print(tot)

#multipling n numbers * 3
multiplier = 3
for i in range(1,11):
    tot = multiplier * i
    print(str(multiplier)  + " times:"  + str(i) + " is: " + str(tot))


#prime numbers
thevar = int(input('Enter the number to see if it is prime'))
divisorfound = False
for i in range(2,thevar-1):
    if thevar%i == 0:
        divisorfound = True

if divisorfound:
    print(str(thevar) + " is not prime")
else:
    print(str(thevar) + " is prime")

#basic example of a nest loop
for i in range(1,4):
    for j in range(1,4):
        print('i is: ' + str(i) +' and j is:' + str(j))
print ('we are done')


#how about a loop for the 12 * 12 multiplication table?
for i in range(1,13):
 for j in range(1,13):
    tot =  i * j
    print(str(i)  + " times:"  + str(j) + " is: " + str(tot))

#additional for loop option
#we can tell the for loop to "step"
#notice the third parameter in the range statement
#it is telling the interpreter to count by 2
for i in range(1,10,2):
    print(i)
#count down instead of up
for i in range(10,0,-1):
    print(i)

#a string can be formed from characters
strs =''
for i in ('H','e','l','l','o'):
    strs += i
print(strs)


#playing the guessing game
#the system will have a secret number and the user has
#to guess it

#we will import a library here to give us a random number
#we will be discussing libraries in detail later on
import random as rd
from datetime import date
#give us a random number between 1 and a 100
secret_numb = rd.randint(1,1000)

numb_guesses = 5
attempt = 1
guess_correct = False
while(guess_correct == False) and (attempt <= numb_guesses):
    user_guess =input('Guess the number between 1 and 1000')
    user_guess = int(user_guess)
    if user_guess == secret_numb:
        print('you guessed it!')
        guess_correct = True
    else:
        attempt += 1
if guess_correct == False:
    print('sorry, you lose')






