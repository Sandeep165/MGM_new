'''
set and dict
conditional statement
'''
#Set
'''

set its unchangeble
Mutable:- we can edit 
Set is changeable dataype :- True
Set item is unchangeble :- True
mutable and immutable
'''
set1 = {"apple","mango","banana"}
set2 = {"Car","Plane","Apple"}
set1.add("Grapes")
#update
set1.update(set2)

# set1.discard("apple")

# print(set1)
'''
Typecasting :- set to list
new = list(set1)
logic
set1 = set(new)
'''

# lst = ["apple","mango","banana"]
# #["Grapes","mango","banana"]
# lst[0] = "Grapes"
# print(lst)
copy_set1 = set1.copy()
# print(copy_set1)


set3 = {"mumbai","pune","delhi"}

new_set3 = set3
copy_set3 = set3.copy()

set3.add("Welcome")
# print(set3)
# print(new_set3)
# print(copy_set3) 


set4 = {"python","java","C","JS"}
# print(set4)
set4.pop() #any random value
# print(set4)

#Dict{key:value}
'''
ordered
changeable
key should be uique
key == index
dosent allow the duplication
'''
mydict = {
    "name" : "Sandeep",
    "age"  : 23,
    "contact_num" : 9892705566,
    "status" : True

}
# print(mydict["contact_num"])
mydict["name"] = "Harry"
# print(mydict.get("status"))
# print(mydict.items())
# print(mydict.keys())
# print(mydict.values())
# print(mydict.pop("contact_num"))
print(mydict.popitem())
mydict.update({"status":False})

mydict["new_member"] = "Welcome"
print(mydict)

new_dict = {}
new_dict[1] = "One"
new_dict[2] = "Two"
new_dict[99] = "Three"

print(new_dict)

# dict1 = { "name":"harry", "age":22}

# lst = [10,12,14,16] #3
# lst[4] = 18
# # print(lst)

family = {
    "member1" : {
        "mom1" : "Bharti",
        "dad1" : "Aditya",
        "nums" : [10,12,14]
    },
    "member2" : {
        "mom1" : "Bharti",
        "dad1" : "Aditya",
        "age1" : {
            10 :"under_age",
            18 : "adults"
        }
    }
}

print(family["member2"]["age1"][10])

'''
if (condition) == True:
    print(s1)
else:
    print(s2)


if (condition) == True:
    print(s1)
elif (condition) == True:
    print(s2)
else:
    print(sn)
'''
num = int(input(",,,,,,,,,,"))
str1 = input(",,,,,,,,,,")
'''
Q1:-A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years.
Ask user for their salary and year of service and print the net bonus amount.

Q2:-A school has following rules for grading system:
a. Below 25 - F
b. 25 to 45 - E
c. 45 to 50 - D
d. 50 to 60 - C
e. 60 to 80 - B
f. Above 80 - A
Ask user to enter marks and print the corresponding grade.  45 ;- d
 
Q3:- Write a program to print absolute vlaue of a number entered by user. E.g.-
INPUT: 1        OUTPUT: 1
INPUT: -1        OUTPUT: 1

'''
num1 = int(input("number:- "))
if num1>0:
    print(num1)
else:
    print(-num1)
salary=int(input("Enter your salary:"))
service_years=int("Enter years of service:")
if service_years>5:
     print("your  bonus =",(salary)*5/100)
else:
    print ("your not eligible for bonus")

num = int(input("Enter ur marks: "))

if(num>80):
    print("A")
elif(num>=60 & num<80):
    print("B")
elif(num>=50 & num<60):
    print("C")
elif(num>=45 & num<50):
    print("D")
elif(num>=25 & num<45):
    print("E")
else:
    print("F")

