'''
map() filter()

'''
'''

map - > func,iter
func on each and every items of an iterables

feasible solu and optimal solu

lambda x,y,z,....n : x+y+z+...n
'''


# result = list(map(lambda para: len(para),["apple","mango","grapes"]))
# print(result)


lst1 = [1,2,3]
lst2 = [4,5,6]

result = list(map(lambda x,y : x+y ,[1,2,3], [4,5,6]))

# print(result)

'''
Q1:- Write a Python program to listify the list of given strings individually using Python map.
lst = ["apple","mango"]   ==> ["a","p","p","L","e"]

Q2:- map func 2 list numb1 and num2   result [num2**num]
list1 = [1,2,3]
list2 = [5,4,9]
[5,16,27]

Q3 :- 2 list result 
list1 = [a,b,c] [5,10]
list2 = [x,y,z]  [1,2]

result = [((a+b),(a-b))]
result = [(6,4)]
'''
# result = list(map(lambda x,y : (x+y,x-y) , [1,2,3],[5,4,9]))
# print(result)

list1=["sandeep","mango"]
result=list(map(list,list1))   #list("apple"), list("mango")
# print(result)


# filter()

input_lst = ['s', 'a', 'n', 'd', 'e', 'e', 'p']  #7

op_lst = list(map(lambda x : x in "aeiou" , input_lst))
print(op_lst)   #7


'''

[1,2,3,4,5,6,7]    = [11,22,33,44,55,66,77]   1)map
[1,2,3,4,5,6,7]    = [6,7,5,1,2,3]            2)filter


Create a function that takes a number as an argument and returns "Fizz", "Buzz" or "FizzBuzz".

If the number is a multiple of 3 the output should be "Fizz".
If the number given is a multiple of 5, the output should be "Buzz".
If the number given is a multiple of both 3 and 5, the output should be "FizzBuzz".
If the number is not a multiple of either 3 or 5, the number should be output on its own as shown in the examples below.
The output should always be a string even if it is not a multiple of 3 or 5.
Examples
fizz_buzz(3) ➞ "Fizz"

fizz_buzz(5) ➞ "Buzz"

fizz_buzz(15) ➞ "FizzBuzz"

fizz_buzz(4) ➞ "4"
'''
def result(x):
    if(x%5==0 and x%3==0):
        return 'fizzbuzz'
    elif(x%5==0):
        return 'buzz'
    elif (x%3==0):
        return 'fizz'
    else:
        return str(x)
    
print(result(4))
