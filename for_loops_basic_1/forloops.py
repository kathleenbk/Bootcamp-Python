# Basic
for a in range(151):
    print(a)

# Mutliples of Five
for b in range(5,1001,5):
    print(b)

# Counting, the Dojo Way
for c in range(1,101):
    if c % 10 == 0:
        print("Coding Dojo")
    elif c % 5 == 0:
        print("Coding")
    else:
        print(c)

# Whoa. That Sucker's Huge
sum = 0
for d in range(1,500000,2):
    if d % 2 == 1: 
        sum+=d
print(sum)

# Countdown by Fours
for e in range(2018,0,-4):
    print(e)

# Flexible Counter
lowNum = 2
highNum = 9
mult = 3
for counter in range(lowNum, highNum+1):
    if counter % mult == 0:
        print(counter)