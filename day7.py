'''
Adv function 

'''

'''

In BlackJack, cards are counted with -1, 0, 1 values:

2, 3, 4, 5, 6 are counted as +1
7, 8, 9 are counted as 0
10, J, Q, K, A are counted as -1
Create a function that counts the number and returns it from the list of cards provided.

Examples
count([5, 9, 10, 3, "J", "A", 4, 8, 5]) ➞ 1

count(["A", "A", "K", "Q", "Q", "J"]) ➞ -6

count(["A", 5, 5, 2, 6, 2, 3, 8, 9, 7]) ➞ 5
Notes
String inputs will always be upper case.
You do not need to consider case sensitivity.
If the argument is empty, return 0.
No input other than: 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A".

Write a function that takes a string and calculates the number of letters and digits within it. 
Return the result in a dictionary.

Examples
count_all("Hello World") ➞ { "LETTERS":  10, "DIGITS": 0 }

count_all("H3ll0 Wor1d") ➞ { "LETTERS":  7, "DIGITS": 3 }

count_all("149990") ➞ { "LETTERS": 0, "DIGITS": 6 }
Notes
Tests contain only alphanumeric characters.
Spaces are not letters.
All tests contain valid strings.
'''
# def top_note(dict1):
#     max_val = max(dict1["notes"])
#     return ({ "name": "John", "top_note": max_val })

# print(top_note({"name":"John", "notes":[3,5,4]}))

# def  count(list1):
#     if(len(list1) == 0):
#         return 0
#     ans = 0
#     for i in list1:
#         if["10","J","K","Q","A"] in list1: #JKQA
#             ans -= 1
#         elif(i == 7 or i == 8 or i == 9):
#             continue
#         else:
#             ans += 1
#     return ans
# print(count(["A",5,5,2,6,2,3,8,9,7]))


# def count_function(lst):
#     for_1=(2,3,4,5,6)
#     for_0=(7,8,9)
#     for_minus1=(10, 'J', 'Q', 'K', 'A')
#     addition=0
#     for i in lst:
#         if i in for_1:
#             addition=addition+1
#         elif i in for_0:
#             addition+=0
#         elif i in for_minus1:
#             addition-=1
#     print(addition)
    
    
# count_function([5,9,10,3,"J", "A", 4, 8, 5])
# def count_all(string):
#     dic={
#         "letters":0,
#         "Digits":0
#     }
#     Digits=('0','1','2','3','4','5','6','7','8','9')
#     for i in string:
#         if i in Digits:
#             dic["Digits"]+=1
#         else:
#             dic["letters"]+=1
            
#     print(dic)

# string=input()
# count_all(string)

'''
if a == int():
    d += 1
elif a == str()
'''
# map and filter adv
# lambda
'''
lambda x: x+1
'''
add = lambda x,y: x+y
print(add(10,15))

# display  = lambda exp1,exp_n : exp + exp_n
sqr = lambda x :x*x
print(sqr(5))
print(sqr(15))

# print(type(sqr))

def add(a,b):
    return a+b

# sum_num = add
# print(type(sum_num))
# print(type(add))
# func , func

# sum_num = add(10,15)
# print(type(sum_num))
# print(type(add))
# int, fun

# sum_num = add()   #half func call 
# print(type(sum_num))
# print(type(add))
# #error
# str = "luyciwueh"
# len(str)
'''
1) both fun
2) both int
3) int, func
4) fun, int

match lang:
3.10

'''
# map func
'''
var_name = map(func, iterator)

func :- print length of the parameter 

iterator = ["apple","mango","grapes"]

1)func applies to iterator   = 3
2)fun applies to each and every value of the iterable   =  [5,5,6]
'''

def length(para):
    print(len(para))

lst = ["apple","mango","grapes"]

result = map(length,lst)
for i in result:
    print(i)
