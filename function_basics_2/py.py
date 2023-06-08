# 1. Countdown
def countdown(num):
    output=[]
    for i in range(num,-1,-1):
        output.append(i)
    return output

print(countdown(7))
# Prints [7, 6, 5, 4, 3, 2, 1, 0]


# 2. Print and Return
def printReturn(numList):
    print(numList[0])
    return(numList[1])

print(printReturn([9,17]))
# Prints 9 then 17


# 3. First Plus Length
sum = 0
def firstPlusLength(numList):
    sum = (numList[0]) + (len(numList))
    return sum

print(firstPlusLength([1,2,3,4,5]))
# Prints 6


# 4. Values Greater than Second
def valuesGreater(list):
    newList=[]
    if len(list)<2:
        return False
    for i in range(0,len(list)):
        if list[i]>list[1]:
            newList.append(list[i])
    print(len(newList))
    return newList

print(valuesGreater([6,3,1,3,5,4]))
# Prints 3 then [6,5,4]
print(valuesGreater([3]))
# Prints False


# 5. This Length, That Value
def lengthValue(num1, num2):
    newList=[]
    for i in range(0, num1):
        newList.append(num2)
    return newList

print(lengthValue(3,6))
# Prints [6,6,6]
