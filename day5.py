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





Write a function that takes a list and a number as arguments. Add the number to the end of the list, 
then remove the first element of the list. The function should then return the updated list.

Examples
next_in_line([5, 6, 7, 8, 9], 1) ➞ [6, 7, 8, 9, 1]

next_in_line([7, 6, 3, 23, 17], 10) ➞ [6, 3, 23, 17, 10]

next_in_line([1, 10, 20, 42 ], 6) ➞ [10, 20, 42, 6]

next_in_line([], 6) ➞ "No list has been selected"
Notes
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
str1 = "I love python"

print(str1.replace("python","java"))