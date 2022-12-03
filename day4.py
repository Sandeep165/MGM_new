'''
Functions
Adv func
map,filter and lambda

structural prog :-
func prog
oops prog
'''
# age = int(input("Entrer the age :-"))

# if age>18:
#     print("can drive a car")
# else:
#     print("Person is under age")

def check(age):
    if age>18:
     print("can drive a car")
    else:
     print("Person is under age")

# sum = 10+15

# check(25)

'''
def func_name(parameter):       #func declaration
    #logic
    #logic1                     #func body

func_name(argument)             #func call

parameter and arguments
parameter :- var that u are taking inside the func(func declaration)
argument :- value for that variable(func call)
'''

def greet():
    # print("Good morning!")
    return("Good morning!")
# var1 = greet()
# print(var1)
# print(greet())

# num1 = 10
# res  =num1
# print(res)




# greet()
# new_greet = "msg1"
# print(new_greet)
'''
print()
return()
local and global
'''
# y=10
# print ("Hello, Dcoder!")
# def check(i):
#   y=2 #local variable
#   def arg(y):
#     print("y is ",y)
#   arg(y)
#   print(i)
# check(2)

# print(y)

# def speak(num1):
#     num1 = 20
#     print(num1)

# speak(10)

#Arbitary argument
#Keyword argument
# def greet(name1,name2,name3):

#     print("Good morning", name2)

# greet(name3="jack",name1="Sam",name2="Sima")


def show(name="hema"):
    print("My name is :-",name)

show("Jack")
show("sam")
show("Tim")

'''
Good morning Sam
Good morning jack
Good morning Sima

'''
'''
Q1:- create a function that finds all even numbers from 1 to the given number.

Examples
find_even_nums(8) ➞ [2, 4, 6, 8]
find_even_nums(4) ➞ [2, 4]
find_even_nums(2) ➞ [2]


Q2:-Create a function that takes a list of strings and integers, and filters out the list so that it returns a
 list of integers only.
Examples
filter_list([1, 2, 3, "a", "b", 4]) ➞ [1, 2, 3, 4]
filter_list(["A", 0, "Edabit", 1729, "Python", "1729"]) ➞ [0, 1729]
filter_list(["Nothing", "here"]) ➞ []
int()   = str()

Q3:-Create a function that takes three integer arguments (a, b, c) and returns the amount of integers 
which are of equal value.

Examples
equal(3, 4, 3) ➞ 2
equal(1, 1, 1) ➞ 3
equal(3, 4, 1) ➞ 0 
'''
def even(num):
    l=[]
    for i in range(1,num+1):
        if(i%2==0):
            l.append(i)
        else:
            pass
    print(l)
even(8)


def filter_list(int1):
    l=[]
    for i in (int1):
        if(type(i)==int):
            l.append(i)
        else:
            pass
    print(l)
filter_list([1,2,"as",'asd'])
