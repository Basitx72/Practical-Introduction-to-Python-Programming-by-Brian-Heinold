# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/16ac6GTsCabRcYIOZeKLlojY58r88XCgh
"""

"""Exresie #1"""

#Q1
heigth = 5
width = 10
for i in range(heigth):
  print('* '*width)

#Q2
width =10
height = 10
for rows in range(height):
    for columns in range(width):
        if (rows == 0 or rows == height-1 or columns == 0 or columns == width-1):
            print("*" , end=" ")

        else:
            print(" ", end=" ")

    print()

#Q3
for i in range(7):
  print("* "*(i+1))

#Q4
x = 512-282
y = 47.48+5
z = float(x/y)
print(round(z,4))

#Q5
num = eval(input("Enter number: "))
x = (num*num)
print("The square of number",num,"is",x,".",sep=" ")

#Q6
x = eval(input("enter number: "))
y = x*2
z = x*3
i = x*4
j = x*5
print(x,y,z,i,j,sep="---")

#Q7
kg = eval(input("Enter weigth in kg: "))
lb = float(kg*2.2)
print(lb)

#Q8
x = eval(input("Enter a 1st number"))
y = eval(input("Enter a 2rd number"))
z = eval(input("Enter a 3rd number"))
total = x+y+z
avg = (total)/3
print("Total = ",total,"Avgerage = ",avg)

#Q9
price = eval(input("Enter the price of the meal: "))
tip_percent = eval(input("Enter the percent of tip: "))
tip_amount = (tip_percent/100)*price
print("Leave tip of ",tip_amount, "rs")
print("And the total bill will be: ",price+tip_amount,"rs")

"""Exresie #2"""

#Q1
for i in range(100):
  print("Humam")

#Q2
for j in range(200):
  for i in range(200):
    print("humam",end=" ")
  print()

#Q3
for i in range(100):
  print(i+1,"Humam")

#Q4
x = 1
for i in range(20):
  print(x,x*x,sep=" --- ")
  x+=1

#Q5
for i in range(8,90,+3):
  print(i)

#Q6
for i in range(100,1,-2):
  print(i)

#Q7
for i in range(10):
  print("A",end="")
for i in range(7):
  print("B",end="")
for i in range(5):
  print("CD",end="")
print("E",end="")
for i in range(6):
  print("F",end="")
print("G")

#Q8
name = input("Enter your name: ")
loop = eval(input("How many times you want to print it: "))
for i in range(loop):
  print(name)

#Q9
num = eval(input("Enter how many numbers you want: "))
fab = 0
s = 1
if num == 1:
  print("1")
else:
  print("1",end=",")
  for i in range(num):
    next = fab+s
    print(next,end=",")
    fab = s 
    s = next

#Q10
h = eval(input("Enter height: "))
w = eval(input("Enter width: "))
for i in range(h):
  print("* "*w)

#Q11
height = eval(input("Enter Heigth: "))
width = eval(input("Enter Width: "))
for rows in range(height):
    for columns in range(width):
        if (rows == 0 or rows == height-1 or columns == 0 or columns == width-1):
            print("*" , end=" ")

        else:
            print(" ", end=" ")

    print()

#Q12
h = eval(input("Enter h: "))
for i in range(h+1):
  print("* "*i)

#Q13
h = eval(input("Enter h:"))
for i in range(h,0,-1):
  print("* "*i)

#Q14
heigth = eval(input("Enter height: "))
for i in range(0,heigth,+1):
  print(" "*(heigth-i),"*"*i)
for i in range(heigth,0,-1):
  print(" "*(heigth-i),"*"*i)

#Q15
size=eval(input("enter size"))

for x in range(0,int(size)):
  print(" "*(size-x),end="")  
  print("*",end="")
  ast = " "
  if x==int(int(size)/2):
    ast = "*"
  for z in range(0,2*x):
      print(ast,end="")
  print("*")

"""# **  Exersie 3**#"""

#Q1
import random             #if you import a library in one cell you dont have to import it again for the other cells
for i in range(50):
  print(i+1,":",random.randint(3,6))

#Q2
x = random.randint(1,50)
y = random.randint(2,5)
z = x**y
print("x = ",x," and y = ",y," so x^y = ", z )

#Q3
x = random.randint(1,10)
print("Name "*x)

#Q4
x = round(random.uniform(1,10),2)
print(x )

#Q5
for i in range(2,52):
  print(1,i,random.randint(1,i),sep=" -- ")

#Q6
x = eval(input("Enter any number"))
y = eval(input("Enter any number"))
z = abs(x-y)
a = x + y
print(z/a)

#Q7
angle = eval(input("Enter angel b/w 180 to -180: "))
angle =angle + 180
print(abs(angle))

#Q8
s = eval(input("Enter seconds: "))
m = s // 60
s = s % 60
print(m,"minutes and ",s," Seconds")

#Q9
cur_hour = eval(input("Enter hours:"))
ahead_hours = eval(input("How many hours you want to go further?"))
new_hour = cur_hour + ahead_hours
if new_hour % 12 == 0:
  print("12 O'Clock")
else:
  print(new_hour % 12 ," O'Clock")

"""Q10"""

#Part A
pow = eval(input("Enter the power you want to raise"))
pow = 2**pow
print(pow,"  ",pow%10)

#Part B
pow = eval(input("Enter the power you want to raise"))
pow = 2**pow
print(pow,"  ",pow%100)

#Part C
pow = eval(input("Enter the power you want to raise: "))
last = eval(input("How many last digits you want: "))
pow = 2**pow
last = 10**last
print(pow,"  last digit(s):",pow%last)

#Q11
kg = eval(input("Enter weigth in kgs: "))
lb = round((kg *2.2), 1)
print(lb)

#Q12
import math                       #only need to import a library once for a notebook
x = eval(input("Enter any number: "))
print(math.factorial(x))

#Q13
x = eval(input("Enter a number: "))
x = math.degrees(x)
print("Sin(x) = ",math.sin(x))
print("Cos(x) = ",math.cos(x))
print("Tan(x) = ",math.tan(x))

#Q14
from math import sin
x=eval(input("Enter an Angle in Degree: "))
print('Sine of the a=Angle is:',sin(x))

#Q15
for i in range(0,346,+15):
  print(i," --- ",round(math.sin(math.radians(i)),4)," ",round(math.cos(math.radians(i)),4))

#Q16   not solved

y = eval(input("Enter the full year: "))
c = eval(input("Enter century: "))
m = (15+c-( c/4 )- ( ( (8*c) +13 ) /25 ) ) % 30
n = (4+c-(c/4))%7
a = y%4
b = y%7
c = y%19
d = ((19*c)+m)%30
e = ((2*a)+(4*b)+(6*d)+n)%7
if d == 29 and e == 6:
  print("April 19, ",y)
elif d ==28 and e ==6 and ( m == 2 or m == 5 or m == 10 or m == 13 or m == 16 or m == 21 or m == 24 or m == 39):
  print("April 18, ",y)
else:
  print("March ",math.floor(22+d+e),y," or April",math.floor(d+e-9),y)

#Q17
year = eval(input("Enter year: "))

for year in range(1600,year):
  if year % 4 == 0 or (year % 100 == 0 and year % 400 == 0):
        print(year)

#Q18
num = eval(input("Enter the amount: "))
if num < 0 or num > 99:
  print("enter wrong range")
else:
  Q = num // 25
  D = num // 10
  N = num // 5
  P = num // 1
  print("Quaters: ",Q," Dimes: ",D," Nikles: ",N," Pennies: ",P)

#Q19
width = eval(input("Enter Width: "))
height = eval(input("Enter Height: "))

for i in range(0, height):
    print()
    for j in range(0, width):
        print(j % 10, end="")

"""# **Exercise #4**"""

len = eval(input("Enter length in cm: "))
if len < 0:
  print("Invalid value.")
else:
  len = len / 2.54
  print(len,"Inches")

temp = eval(input("Enter temprature: "))
unit = input("Enter units [c => celsius or f => fahrenheit]: ")
if unit == 'c':
  temp = ((9/5)*temp+32)
  print(temp)
elif unit == 'f':
  temp = (5/9)*(temp - 32)
  print(round(temp,2))
else: 
  print("You entered wrong units.")

temp = eval(input("Enter temprature: "))
if temp < -273.15:
  print("Invalid temprature.")
elif temp == -273.15:
  print("The temperature is absolute 0.")
elif temp < 0 and temp > -273.15:
  print("The temperature is below freezing.")
elif temp == 0:
  print("The temperature is at the freezing point.")
elif temp > 0 and temp < 100:
  print("The temperature is in the normal range.")
elif temp  == 100:
  print("The temperature is at the boiling point.")
elif temp > 100:
  print("The temperature is above the boiling point.")

c = eval(input("Enter the credit: "))
if c <= 23:
  print("The student is a freshman.")
elif c >= 24 and c < 53:
  print("The student is a sophomore.")
elif c >= 54 and c < 83:
  print("The student is a juniors.")
elif c >= 84:
  print("The student is a senior.")

"""# **Exersice #5**"""

count = 0
j = 1
for i in range(1,101):
  j = i*i
  if j%10 == 1:
    count += 1
  else:
    pass
print(count)

count = 0
count2 = 0
j = 1
for i in range(1,101):
  j = i*i
  if j%10 == 4:
    count += 1
  elif j%10 ==  9:
    count2 += 1
print(count," : 4")
print(count2," : 9")

num = eval(input("Enter any number: "))
x = 0
for i in range(1,(num+1)):
   x = 1/i + x
x = x - math.log(num)
print(x)

num = 1
for i in range(1,9):
    sol = num-(i+1)
    num += 1
    ans = num + sol
    print(sol,ans)

#Q4
num = 2000
sum = 0
sum2 = 0
for i in range(1,2001,2):
  sum = i - (i+1)
  print(sum)
  sum2 = sum + sum2
  print("sum",sum2)
print(sum2)

#Q5
num = eval(input("Enter num: "))
sum = 0
for i in range(1,num+1):
  if num%i == 0:
    sum = sum + i 
print(sum)

#Q6
for i in range(1,1000):
  sum = 0
  for j in range(1,i+1):
    if i%j == 0:
      sum = sum + j
  if sum == i:
    print(i)

"""# **Exersice#6**"""

s = input('Enter a string: ')
for i in range(len(s)):
  print(s[i]*2)

L = [1,2,5,5,1,5,5,4,5,5,8,9,34,1]
L=L.sort()
print(L)



"""

# Ex7
"""

num_of_entries = eval(input("Enter number of entries you want to add in the list: "))
List = []
for i in range(num_of_entries):
  L = eval(input("Enter the number: "))
  List.append(L)
print(len(List))#A
print(List[-1])#B
List.reverse()#C
print(List)
if 5 in List:#D
  print("Yes")
else:
  print("no")

print(List.count(5))#E
L2 = List
del L2[0]
del L2[-1]
L2.sort()
print(L2)
count = 0
for i in List:
  if i < 5:
    count += 1
  else:
    pass
print(count)

from random import randint
List = []
for i in range(20):
  num = randint(1,100)
  List.append(num)


print(List)#A

larg_num = 0#B
small_num = 1000000000000000000000
for i in List:
  if i >= larg_num:
    larg_num = i
  if i < small_num:
    small_num = i
print(larg_num)
print(small_num)
List.pop(Larg_num)
List.pop(small_num)

larg_num = 0
small_num = 1000000000000000000000
for i in List:
  if i >= larg_num:
    larg_num = i
  if i < small_num:
    small_num = i

print(larg_num)
print(small_num)
print(len(List))

List = [8,9,10]
List[1] = 17
List.append(4)
List.append(5)
List.append(6)
del List[0]
List.sort()
List = List*2
List.insert(2,25)
print(List)



"""# Ex8"""

#Q1
s = input("Enter any text: ")
s = s.lower()
List = s.split()
articles = ["a","an","the"]
for i in articles:
  print("There are ",List.count(i)," ",i)
print("in ",s)

#Q2
List = []
for i in range(5):
  s = input("Enter a nubmer: ")
  List.append(s)
print("+".join(List))

#Q3
#A
s = input("Enter a string: ")
List = s.split()
print(List[2])
#B
s = input("Enter the sentence: ")
List = s.split()
for i in range(len(List)):
  if (i+1)%3 == 0 :
    print(List[i])
  else:
    pass

#Q4
#A
from random import shuffle
s = input("Enter a sentence: ")
List = s.split()
shuffle(List)
print(" ".join(List))
#B
from random import shuffle
s = input("Enter a sentence: ")
s = s.lower()
s=s.replace(".","")
print(s)
List = s.split()
shuffle(List)
List[1] = List[1].capitalize()
print(" ".join(List),".")

#Q5
from random import choice
quotes = ["You’re off to great places, today is your day. Your mountain is waiting, so get on your way.","“You always pass failure on the wayto success.”","“No one is perfect - that’s why pencils have erasers.”",]
print(choice(quotes))

#Q6
from random import choice
List = [str(i) for i in range(1,49)]
lottery = []
for x in range(6):
  rand = choice(List)
  lottery.append(rand)
print(lottery)
print("".join(lottery))

#Q7
from random import sample

lottery_number = [i for i in range(1,11)]

loop = 1000

def drawing():
  #generates a random list from lottery_number having 6 numbers
  List = sample(lottery_number,6)
  return List


def win(rep):
  #generates 2 lottery tickets , 1 for user and one for computer, and checks if both are same and then increases count by 1
  count = 0
  for i in range(rep):
    user_hand = drawing()
    comp_hand = drawing()
    if user_hand == comp_hand:
      count += 1
  return count

won = win(loop)
print((won/loop)*100)

#Q8
from random import choice
pep_num = eval(input("Enter the number of people: "))
Names = []
Entries = []
num_try = 0
for i in range(pep_num):
  name = input("Enter the name of person: ")
  num_entries = eval(input("Enter their tries: "))
  for j in range(num_entries):
    Names.append(name)
print(choice(Names))

#Q9
que = ["What is the name of your university?","Who is the best teacher?","What is my full name?"]
answer = ["institue of space technology","sir tufail","muhammad humam choudhary"]
right = 0
for i in range(len(que)):
  print(que[i])
  user_ans = input("Answer: ")
  if  answer[i] in user_ans:
    print("Rigth")
    right += 1
  else:
    print("wrong answer") 
print("You got",right,"right answer")

#Q10
curse = ["darn","dang","freakin","heck", "shoot"]
text = input("Enter text: ")
text = text.lower()
Text = text.split()
for i in range(len(Text)):
  for j in curse:
    if Text[i] == j:
      Text[i] = "*"*len(Text[i])
    else:
      pass

print(" ".join(Text))

































"""# Ex9"""

#Q1
i = 1
while i < 51:
  print(i)
  i+=1

#Q2
#A
s = "Hello"
x = 0
while x < len(s):
  print(s[x])
  x+=1
#B
s = "Hello World"
x = 0

while x < len(s) :
  if (x % 2) == 0:
    if x+1 < len(s):
      print(s[x+1]) 

  x+=1

#Q3
while True :
  kg = eval(input("Enter weigth in KG: "))
  if kg > 0:
    pound = kg * 2.2
    print(pound)
  elif kg == 0:
    break
  else:    
    print("Invalid Weigth ")

#Q4
password = "strongpassword123"
count = 5
while True:
  password_in = input("Enter password: ")
  if password_in == password:
    print("Logged in ")
    break
  elif count < 0:
    break
  else:
    print("Invalid password. Try again. Tries left: ",count)
  count-=1

#Q5
score_list = []
Total_count = 0
count = 0
count2 = 0
while True:
  score = eval(input("Enter your test score: "))
  if score <0:
    break
  Total_count += 100
  score_list.append(score)
  count += score
  if score >= 90:
      count2 += 1



avg = (count/Total_count)
print(avg)
print("There are ",count2," A grade")

#Q6
from random import randint 
secret_num = randint(1,100)
guessed = False
print(secret_num)
i = 0
while  i <=5 :
  guess =eval(input('Enter your guess (1-100):'))
  if guess < secret_num:
    if 5-i == 1:
      print('HIGHER.', 5-i,'guess left.\n')
    else:
      print('HIGHER.', 5-i,'guesses left.\n')
  elif guess > secret_num:
    if 5-i == 1:
      print('LOWER.', 5-i,'guess left.\n')
    else:
      print('LOWER.', 5-i,'guesses left.\n')

  elif guess == secret_num:
    print('You got it!')
    guessed = True
    break
  
  i+=1

if not guessed: 
    print('You lose.  The correct number is', secret_num)



























"""#Ex10 Q11 """

inp = eval(input("Enter a number: "))
inps = str(inp)
reversed = inps[::-1]
sum = inp + int(reversed)
for i in range(25):
  if str(sum) == str(sum)[::-1]:
    print(sum)
    break
  else:
    sum = sum + int(sum)

"""#Q13"""

for i in range(1, 10000):
    sumi = 0
    ply = 1
    istr = str(i)
    for x in istr:
        sumi += int(x)
        ply = ply * int(x)
    result = ply + sumi
    if result == i:
        print(result)

"""#Q16"""

feets = eval(input("Enter a number: "))
print(feets)
foot = int(feets)
inch = feets - foot
inches = inch*12
print(f"{foot} feet, {int(inches)} inches")

"""#Q17"""

heigth = []
while True:
  inp = input("Enter heigth in feet'inches\": ")
  inp = inp.lower()
  if inp == "done":
    break
  else:
    heigth.append(inp)
count4 = 0
count5 = 0
count6 = 0
count7 = 0
for i in heigth:
  if i[0] == "4":
    count4 +=1
  elif i[0] == "5":
    count5+=1
  elif i[0] == "6":
    count6+=1
  elif i[0] == "7":
    count7 += 1
print(f"{count4} 4-footer \n{count5} 5-footer \n{count6} 6-footer \n{count7} 7-footer \n")

"""#Q30"""

n = int(input("Enter the number of rows:"))

for i in range(n):
    print(' '*(n-i), end='')

    print(' '.join(map(str, str(11**i))))

"""# Ex11"""

#Q1
product_num = eval(input("Enter Number of products: "))
my_dict ={}
for x in range(product_num):
    productName = input("Enter Product Name: ")
    productPrice = int(input("Enter Product Price"))
    my_dict[productName] = productPrice


while True:
    productName = input("Enter Product name to get Price")
    if productName in my_dict:
        print("The price for your product is ", my_dict[productName])

    else:
        print("This product is not found in dictionary")


print(my_dict)

#Q2 
my_dict ={'Mercedez': '100','Ferrari':'200','Bugatti':'300'}
print(my_dict)

amt =eval(input("Enter Amount: $$"))
for key ,values in my_dict.items():
    if  int(values) < amt:
        print (key ,"->",values)

#Q3
my_dic = {'january':31, 'february':28, 'march':31, 'april':30,
'may':31, 'june':30, 'july':31, 'august':31,
'september':30, 'october':31, 'november':30, 'december':31}

# part a
month = input("Enter the name of month :").lower()
print("The number of days in ",month,' are ',my_dic[month])

#part b
print(sorted(my_dic))

#part c
for key ,values in my_dic.items():
  if int(values)==31:
    print(key)

#Q4
user_dict ={"ahmad":"1234","Basit":"abcd","zaryab":"6789"}
def CheckUser_Pass(x,y):
    for keys ,values in user_dict.items():
        if keys == x  and y == user_dict[keys]:
            return ("you are succesfully logged in",keys,user_dict[keys])
        else:
            return  ("Please do check your login details")



x = input("Enter Username: ")
y = input("Enter Your Password ")
print(CheckUser_Pass(x,y))

#Q5
def teamWIn():
    numberofTeams = int(input("Enter Number of Teams: "))
    team_dict={}
    score_list =[]
    winning_record =[]
    percentage_score = 0
    for team in range(numberofTeams):
        team_name = input("Enter Team Name: ")
        team_winning_score = int(input("Team Winning game: "))
        team_dict.update({team_name:team_winning_score})
        score_list.append(team_winning_score)
        winning_record.append(team_name)

    userinput = input("Enter team to check % of wins: ")
    for  keys,values in team_dict.items():

         if userinput == keys:
            score = team_dict[keys]
            percentage_score = (score/100)* 100

    return "Your teams list is {},Percentage win of team {}%, All team with winning record  {}".format(team_dict,percentage_score,winning_record)

print(teamWIn())

#Q6
def teamInfo():
   num_team =int(input("Enter Number Of Teams: "))
   team_dict={}
   for team in range(num_team):
       key = input("Enter Team name: ")
       value =[]
       wins = int(input("Enter Win: "))
       losses = int(input("Enter Losses: "))
       value.extend((wins,losses))
       team_dict.update({key:value})
       
   return team_dict

print(teamInfo())

#Q7
def creatList():
    matrix_dict={}
    for num in range(len(matrix_5)):
        key = matrix_5[num]
        value = matrix_5.count(key)
        matrix_dict.update({key:value})
    return matrix_dict

print(creatList())

#Q8
import random

all_card ={"One":1,"Two":2,"Three":3,"Four":4,"Five":5,"Six":6,"Seven":7,"Eight":8,"Nine":9,"Ten":10}
cards = 3
player1Card =[]
player2Card =[]
for card in range(cards):
    c1 =random.choice(list(all_card.values()))
    c2= random.choice(list(all_card.values()))
    player1Card.append(c1)
    player2Card.append(c2)
print(player1Card,player2Card)

if sum(player1Card) > sum(player2Card):
    print("Player 1 wins with ",sum(player1Card)," Against Player 2 with",sum(player2Card))
elif sum(player2Card) > sum(player1Card):
    print("Player 2 wins with ",sum(player2Card)," Against Player 1 with",sum(player1Card))



"""#Ex13 """

#Q1
def rectangle(m,n):
  for i in range(m):
    print("* "*n)
rectangle(2,4)

#Q2
#PART A
def add_excitement(List):
  List_temp=[]
  for i in range(len(List)):
    x = f"{List[i]}!"
    List_temp.append(x)
  List = List_temp
  print(List)


inp = input("Enter text: ")
L = inp.split()
add_excitement(L)

#PART B
def add_excitement(List):
  List_out = []
  for i in range(len(List)):
    out = f"{List[i]}!"
    List_out.append(out)
  return List_out
  
inp = input("Enter text: ")
L = inp.split()
print(add_excitement(L))

#Q3
def sum_digits(num):
  L = list(str(num))
  sum = 0
  for i in L:
    sum += int(i)
  return sum
print(sum_digits(15))

#Q4
def Digital_root(num):
  L = list(str(num))
  sum = 0
  for i in L:
    sum += int(i)
  print(sum)
  return sum
x = 45893
out = x
while len(str(out)) != 1:
  out = Digital_root(out)

#Q5
def first_diff(str1,str2):
  List1 = list(str1)
  List2 = list(str2)
  for i in List:


string1 = input("Enter string1: ")
string2 = input("Enter string2: ")
first_diff(string1,string2)

#Q6
from math import factorial
def binom(n,k):
  result = factorial(n)/(factorial(k)*factorial(n-k))
  return result
n = eval(input("Enter n: "))
k = eval(input("Enter k: "))
print(binom(n,k))



#Q18
d = {0: 'A', 1: 'B', 2: 'C', 3: 'D',
     4: 'E', 5: 'F', 6: 'G', 7: 'H', 8:
     'I', 9: 'J', 10: 'K', 11: 'L', 12:
     'M', 13: 'N', 14: 'O', 15: 'P', 16:
     'Q', 17: 'R', 18: 'S', 19: 'T'}


def base20(num):
    list = []
    while int(num) > 0:
        rem = num % 20
        num = num / 20
        remander = int(rem)
        list.append(str(remander))
    return list


for j in range(402):
    num = j
    rem = base20(num)
    rem.reverse()

    l2 = []
    l3 = []
    for i in rem:
        l2.append(d[int(i)])
        l3.append(j)
    out = ''.join(l2)
    print(f"{j} | {out}")

"""#Q23"""

from random import *


def check(List):
    for i in List:
        for j in i:
            print(j, " : ", i.count(j))
            if i.count(j) != 1:
                  return False

    for i in range(len(List)):
        for j in range(len(List[i])):
            try:
                if List[i][j] == List[i+1][j]:
                    print(List[i][j], "==", List[i][j+1], "--", i, "--", j)
                    return False
            except:
                pass         

List = []
for i in range(9):
    List2 = []
    for i in range(9):
        # randomly generetes a list /// we can also take input for better results
        x = randint(0, 9)
        List2.append(x)
    List.append(List2)
print(List)

if not check(List):
    print("The board is wrongly filled")
else:
    print("The board is filled correctly")

"""##Q Multiply the digits of a integer"""

num = 432
str_num = str(num)
result =1 
for i in str_num:
  result *= int(i)
print(result)

import pandas as pd
L= ["humam","ali","rafay","haseeb"]
D={"name": L}
L2= ["humam","ali","rafay","haseeb"]
D2={"fname": L}
Data2= pd.DataFrame(D2)
Ser2 =pd.Series(Data2["fname"])
Data= pd.DataFrame(D)
Ser =pd.Series(Data["name"])
print(Data.append(Data2))
Data

a={1:"A",2:"B"}
print(a.get(1))

i=5
while True:
  if i%0o11==0:
    break
  print(i)
  i+=1