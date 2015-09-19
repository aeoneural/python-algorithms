#1 Linked-list printing: 
class Node: 
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next 
    
    def __str__(self):
        return str(self.value)
        
        
mynode1 = Node("First")
mynode2 = Node("Second")
mynode3 = Node("Third")
    
mynode1.next = mynode2
mynode2.next = mynode3    
    
def Iterate(var):
    while(var):
        print var.value
        var = var.next
            
Iterate (mynode1)

------------------------------------------------------------
#2 Cube root guess:
num = int(raw_input("Enter a number: ")) 
ans = 0
# while (ans**3 < abs(num)):
#    ans = ans + 1
for ans in range(0, abs(num) + 1):
    if ans**3 == abs(num):  
        break    
if ans**3 != abs(num): #if you are out of value 
    print(str(num) + " is not a perfect cube")
else: 
    if (num < 0): 
        ans = -ans 
    print("Cube root of " + str(num) + " is " + str(ans))


------------------------------------------------------------
#3 decimal -> binary
num = 20
if num<0:
    isNeg = True
    num = abs(num)
else: 
    isNeg = False
result = ''

if num == 0:
    result = '0'

while num>0:
    result = str(num%2) + result 
    num = num/2

if isNeg:
    result = '-' + result

------------------------------------------------------------
#4 Float -> binary 
num = float(raw_input("Enter a decimal btw 1 and 0: "))

p=0 
while((2**p)*num)%1 != 0:
    print("Remainder = "+str((2**p)*num - int((2**p)*num)))
    p+=1      
num = int(num*(2**p))

result = ''
if num == 0:
    result = '0'

while num>0:
    result = str(num%2) + result 
    num = num/2

for i in range (p-len(result)):
    result = '0' + result

result = result [0:-p] + '' + result[-p:]  #spot S
print("The binary rep of decimal: "+ str(num)+ " is " + str(result)) 

------------------------------------------------------------
#5 Square root (precise) 
num = 24
eps=0.01
ans = 0.0 
nguess = 0
step = eps**2

while abs(ans**2 - num) >= eps and ans <= num:
    ans += step
    nguess += 1

print("Number of guesses: " + str(nguess))

if abs(ans**2-num)>= eps: 
    print("Guess failed!") 
    
else: 
    print(str(ans)+" is close to the sqrt of " + str(num))

------------------------------------------------------------
#6 Square root (bisection algorithm): 
x = 24

eps = 0.01
nguess = 0
low = 0.0 
high = x
ans = (low+high)/2

while abs(ans**2 - x) >= eps: 
    print ("High " + str(high) + " low: " + str(low) + " ans: " + str(ans))
    nguess += 1 
    if ans**2 < x: 
        low = ans
    else: 
        high = ans
    ans = (low + high)/2.0
print("Nguess: " + str(nguess))
print(str(ans)+ " is close to sqrt of " + str(x))

------------------------------------------------------------
#7 Guess game: 
low, high = 0, 100

print("Please think of a number {0} and {1}!.".format(low,high))

guessing = True
while guessing:
    guess = (low+high)/2
    print("Is your secret number {0}?".format(guess))
    x = raw_input("Enter 'h' to indicate the guess is too high. "
                        "Enter 'l' to indicate the guess is too low. " 
                        "Enter 'c' to indicate I guessed correctly.").lower()
    if x == 'h':
        high = guess
    elif x == 'l':
        low = guess
    elif x == 'c':
        guessing = False
    else:
        print("Sorry, I didn't undersand your input")
    
print("Game over. Your secret number was {0}.".format(guess))
         
------------------------------------------------------------       
#8 Newton-Raphson way of finding square root: 
eps= 0.01
y= 16.0
guess = y/2.0

while abs(guess*guess - y) >= eps: 
    guess = guess - (((guess**2) - y)/ (2*guess))
    
print("Square root of " + str(y) + " is about " + str(guess))

#9  Root finding : pth root of n.

def findRoot1(x, power, eps): 
    if x<0 and power%2 == 0: #for even powered root of negative number
        return None
    low = min(-1.0, x) 
    high = max(1.0,x)
    ans = (high + low)/2.0
    if ans**power<x: 
        low = ans
    else:
        high = ans
    ans = (high + low)/2.0
    return ans
print findRoot1(0.25, 2, 0.01) 