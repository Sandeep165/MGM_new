# Data types in Python
# name = "Sandeep123"
# id = "001"
# print(type(id))
# list = "Harry"
import imp


list1 = [1,2,3]
set1 = {1,2,3}
tuple1 = (1,2,3)
dict1 = {
    1:"one",
    2:"two"
}
# print(type(list1))
# print(type(set1))
# print(type(tuple1))
# print(type(dict1))

# new1 = {}
# print(type(new1))
#bool-> TRUE FALSE
set1 = {True}
#Tuple having single value  will display data type of that particular value
dict1 = ("True")
# print(type(set1))
# print(type(dict1))

# num = [1,2,3]
# res = frozenset(num)
# print(res)

'''
List :-
mutable,ordered,allows duplicates
set :-
mutalble,unordered,no duplications
dict :-
ordered,mutable,allows duplication
from version 3.7 onwards ordered (v>3.7)
tuple:- immutable,ordered,allows duplication
'''
# set1 = {1,2,3,4,5,6}
# set1.add(10)
# print(set1)
# set2 = {"apple","mango","banana"}
# set2.add("Grapes")
# print(set2)

#list
myList = [10,11,[22,["India",123],546],33,55] #22 
# # 564,123
# print(myList[2][2])
# print(myList[2][1][1])


new = [10,20,30,[11.11,[["India"],"python"],["Java"],"Mumbai",11,12],[[101,102,103],["Delhi"]]]

#["India"],India ,[Java],java,11,102,Delhi
# print(new[4][1][0])


'''

Method          	Description
append()	Adds an element at the end of the list
clear()	Removes all the elements from the list
copy()	Returns a copy of the list
count()	Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	Removes the element at the specified position
remove()	Removes the item with the specified value
reverse()	Reverses the order of the list
sort()	Sorts the list
'''
#pop remove
mylist = [1,2,3,6,8,4,59]
mylist.remove(59)
print(mylist)

lst = ["apple","mango"]
print("This value is removed:- ",lst.pop(1)) #mango
print(lst)

'''
1)Remove :- take particular value itself and it will remove that value
2)pop :- take index of a value that you want to remove
'''

lst1 = ["apple","mango"]
lst2 = ["cherry","banana","Grapes"]

lst2.extend(lst1)
print(lst2)

tuple1 = (1,2,3,4,4,4,4,4,4,4,4,4)
print(tuple1.count(4))

#typescasting

int1 = 5

tuple2 = (2,56,8,77,9,33)  #append 100

# res = list(tuple2)
# res.append(100)
# print(res)

# tuple2 = tuple(res)


tup = (10,)
print(type(tup))

