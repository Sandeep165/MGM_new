'''
Create a function that takes a string as an argument and returns a coded (h4ck3r 5p34k) version of the string.

Examples
hacker_speak("javascript is cool") ➞ "j4v45cr1pt 15 c00l"

hacker_speak("programming is fun") ➞ "pr0gr4mm1ng 15 fun"

hacker_speak("become a coder") ➞ "b3c0m3 4 c0d3r"
Notes
In order to work properly, the function should replace all "a"s with 4, "e"s with 3, "i"s with 1, "o"s with 0,
 and "s"s with 5.



Write a function that takes a list and determines whether it's strictly increasing, strictly decreasing, 
or neither.

Examples
check([1, 2, 3]) ➞ "increasing"

check([3, 2, 1]) ➞ "decreasing"

check([1, 2, 1]) ➞ "neither"

check([1, 1, 2]) ➞ "neither"
Notes
The last example does NOT count as strictly increasing, since 1-indexed 1 is not strictly greater than 
the 0-indexed 1.
Input lists have a minimum length of 2.
In order to work properly, the function should replace all "a"s with 4, "e"s with 3, "i"s with 1, "o"s with 0,
 and "s"s with 5.
'''
# str1 = "Hello"
# print(str1.replace("o","0"))

def hacker_speak(x):
    return(x.replace("a","4").replace("o","0").replace("e","3").replace("i","1").replace("s","5"))

print(hacker_speak("javascript is cool"))
print(hacker_speak("programming is fun"))

'''
Write a function that takes a list and determines whether it's strictly increasing, strictly decreasing, 
or neither.

Examples
check([1, 2, 3]) ➞ "increasing"

check([3, 2, 1]) ➞ "decreasing"

check([1, 2, 1]) ➞ "neither"

check([1, 1, 2]) ➞ "neither"
Notes
The last example does NOT count as strictly increasing, since 1-indexed 1 is not strictly greater than 
the 0-indexed 1.
Input lists have a minimum length of 2.





Write a function that takes a list and a number as arguments. Add the number to the end of the list, 
then remove the first element of the list. The function should then return the updated list.

Examples
next_in_line([5, 6, 7, 8, 9], 1) ➞ [6, 7, 8, 9, 1]

next_in_line([7, 6, 3, 23, 17], 10) ➞ [6, 3, 23, 17, 10]

next_in_line([1, 10, 20, 42 ], 6) ➞ [10, 20, 42, 6]

next_in_line([], 6) ➞ "No list has been selected"
Notes
append and insert methods  remove and pop
For an empty list input, return: "No list has been selected"



Create a function that takes a list of positive and negative numbers. Return a list where the first 
element is the count of positive numbers and the second element is the sum of negative numbers.

Examples
sum_neg([0,1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]) ➞ [10, -65]
# There are a total of 10 positive numbers.
# The sum of all negative numbers equals -65.

sum_neg([92, 6, 73, -77, 81, -90, 99, 8, -85, 34]) ➞ [7, -252]

sum_neg([91, -4, 80, -73, -28]) ➞ [2, -105]

sum_neg([]) ➞ []
Notes
If given an empty list, return an empty list: []
0 is not positive.
'''
def next_in_line(list1, num):
    if(len(list1) == 0):
        return "No list has been selected"
    list1.pop(0)
    list1.append(num)
    return list
# print(next_in_line([5,6,7,8,9], 1))

# def sum_neg(list):
#     pos = 0
#     neg = 0
#     for i in list:
#         if(i > 0):
#             pos += 1
#         else:
#             neg += i
#     return [pos, neg]
# print(sum_neg([0,1,2,3,4,5,6,7,8,9,10,-11,-12,-13,-14,-15]))

'''

Q1:- 
Create a function that takes a dictionary of objects like { "name": "John", "notes": [3, 5, 4] } and returns a 
dictionary of objects like { "name": "John", "top_note": 5 }.

Examples
top_note({ "name": "John", "notes": [3, 5, 4] }) ➞ { "name": "John", "top_note": 5 }

top_note({ "name": "Max", "notes": [1, 4, 6] }) ➞ { "name": "Max", "top_note": 6 }

top_note({ "name": "Zygmund", "notes": [1, 2, 3] }) ➞ { "name": "Zygmund", "top_note": 3 }


'''

def top_note(dict1):
    max_val = max(dict1["notes"])
    return ({ "name": "John", "top_note": max_val })

print(top_note({"name":"John", "notes":[3,5,4]}))

def top_note(dict):
    dict["top_note"] = max(dict["notes"])
    del dict["notes"]  
    return dict
print(top_note({"name":"John", "notes":[3,5,4]}))


'''
Create a function to find only the root value of x in any quadratic equation ax^2 + bx + c. 
The function will take three arguments:

a as the coefficient of x^2
b as the coefficient of x
c as the constant term
Examples
quadratic_equation(1, 2, -3) ➞ 1  : x**2 + 2x -3 =0

quadratic_equation(2, -7, 3) ➞ 3 .   : 2x**2-7x+2 = 0 

quadratic_equation(1, -12, -28) ➞ 14 .  : x**2 - 12x -28 =0
Notes
Quadratic equation is always guaranteed to have a root.

x_pos = (-b + √ (b2 - 4ac) )/2a
x_neg = (-b - √ (b2 - 4ac) )/2a


'''
def quadratic_equ(a,b,c):
    x_pos = int((-b + (b**2 - 4*a*c)**(0.5) )/(2*a))
    x_neg = int((-b - (b**2 - 4*a*c)**(0.5) )/(2*a))
    print(x_pos)
  
quadratic_equ(2,-7,3)

# map and filter
'''
map (func,iter) (upper,[apple,mango])   = [APPLE,MANGO]    -> final leng of input iterable   = op iterable
filter (func,iter)                                          -> final leng of input iterable   != op iterable
func -> age>18         [adult,----,adult]
print(adult)
[15,------,29]
'''

 