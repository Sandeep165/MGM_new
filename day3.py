'''
if else 
looping

pass continue and break

functions

1 hr
4-5
3:30

data types
if else
for loops
(func)
basic interview ques

1 & 1 = 1
1 & 0 =  0
1 | 1 = 1
1 | 0 =  1

Q1 :- wap calculate electricity bill

Unit                        price
first 100 (0-100)              no charge
next 100 units (101-200)         Rs 5 per unit
next 200 units  (201-n)        Rs 10 per unit

unit = input()

119 = 100+19  =0+19*5 = 95

201= 100+100+1 = 0+500+10 = 510


Q2:- wap to display a particular day from user input (1-7) 1-7 :-  error pls enter a valid input
one data type
1:- Sunday
2:- monday
'''
# l1 = {1:"sunday", 2:"monday", 3:"tuesday", 4:"wednesday", 5:"thursday", 6:"friday", 7:"saturday"}
# n = int(input())
# if(1 <= n <= 7):
#     print(l1[n])
# else:
#     print("ERROR !! Please enter a valid input")

# unit=int(input("enter total unit:"))
# if(unit>=0 and unit<=100):
#     print("no bill")
# elif(unit<=200):
#     unit=unit-100
#     print("BIll=",unit*5)
# elif(unit<0):
#     print("invalid unit")
# else:
#     unit=unit-200
#     bill=500+unit*10
#     print("BILL=",bill)

'''
for i in var:

for i in range(start:end:step)
start:- inclusive
end :- exclusive
step :- 1
start = 4
for i in range(10): 0-9

'''

# for i in range(1,11):
#     print(i)

'''
string slicing:
str = "xyz"
str[start:end:step]

# '''
# string = "I love Python!"
# print(string[::-1])
'''
str[::] or str[:]   -> print entire string
str[start:]         -> start from index till last index

var1 == var2.reverse()
nayan = nayan

word from user
if else 
palindrom word or not
'''
# word=input("Enter the word:- ")

# if(word==word[::-1]):
#     print("Palindrome")
# else:
#     print("Enter a valid string")


string = "I love Python!"
# find word =love -> match ? No match
for i in string:
    if "love" in string:
        print("Match")
    else:
        print("No match")
    break

# lst = [1,2,3,4,5,6,7,8,9,10]
# # print(sum(lst))
# sum1 = 0

# #0-11 = 1   1+2 = 3  3+3

# for i in lst:
#     sum1 += i
# print(sum1)

fruits = ["apple","mango","grapes"]
# print(len(fruits))
for i in range(len(fruits)):
    print("I eat:- ",fruits[i])

'''
I eat apple
I eat mango
I eat grapes
'''

# for i in "apple":
#     if i == "e":
#         break
#     print(i)
# print("............................")

for i in "apple":
    if i == "l":
        continue
    print(i)
print("............................")

for i in "apple":
    pass
    

num1 = 10
num2 = 20