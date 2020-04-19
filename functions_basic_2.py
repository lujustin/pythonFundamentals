1. Countdown - Create a function that accepts a number as an input. Return a new list that counts down by one, from the number (as the 0th element) down to 0 (as the last element).
def countdown(n):
    newlist = []
    for x in range (n, -1, -1):
        newlist.append(x)
    print(newlist)
countdown(20)

2. Print and Return - Create a function that will receive a list with two numbers. Print the first value and return the second.
def printAndReturn(a,b):
    print(a)
    return(b)

3. First Plus Length - Create a function that accepts a list and returns the sum of the first value in the list plus the list's length.
def firstPlusLength(arr):
    # sum = 0
    sum = arr[0] + len(arr)
    return(sum)

print(firstPlusLength([1,2,3,4,5]))

4. Values Greater than Second - Write a function that accepts a list and creates a new list containing only the values from the original list that are greater than its 2nd value. Print how many values this is and then return the new list. If the list has less than 2 elements, have the function return False
def valsGreaterThan(arr):
    newlist = []
    count = 0
    for x in range(len(arr)):
        if arr[x] > arr[1]:
            newlist.append(arr[x])
            count += 1
    return count, newlist

print(valsGreaterThan([5,2,3,2,1,4]))

5. This Length, That Value - Write a function that accepts two integers as parameters: size and value. The function should create and return a list whose length is equal to the given size, and whose values are all the given value.
def length_and_value(length, val):
    list = []
    for i in range(length):
        list.append(val)
    return list

print(length_and_value(4,5))