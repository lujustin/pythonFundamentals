# 1. Basic - print all integers from 0 to 150.
for x in range(0, 151, 1):
    print(x)

# 2. Multiples of Five - print all multiples of five from 5 to 1000.
for x in range (5, 1001, 5):
    print(x)

# 3. Counting, the Dojo Way - print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".
#for x in range (1, 101, 1):
    if(x % 10 == 0):
        print("Coding Dojo")
    elif (x % 5 == 0):
        print("Coding")
    else:
        print(x)

# 4. Whoa. That Sucker's Huge - add odd integers from 0 to 500,000 and print the final sum.
    sum = 0
    for x in range(0, 500001, 1):
    if(x % 2 != 0):
        sum = sum + x
print(sum)

# 5. Countdown by Fours - Print positive numbers starting at 2018, counting down by fours.
for x in range(2018, 0, -4):
    print(x)

# 6. Flexible Counter - Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNUm, print only the integers that a multiple of mult.
lowNum = int(input("Please enter Minimum number: "))
highNum = int(input("Please enter Maximum number: "))
mult = int(input("Please enter Multiple: "))
for x in range (lowNum, highNum + 1, 1):
    if(x % mult == 0):
        print(x)