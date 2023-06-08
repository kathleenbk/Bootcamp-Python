#1
def number_of_food_groups():
    return 5
print(number_of_food_groups())
# Prediction: 5
# Predicted correct!


#2
def number_of_military_branches():
    return 5
print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches())
# Prediction: undefined
# Predicted incorrect, prints error b/c first function is not defined


#3
def number_of_books_on_hold():
    return 5
    return 10
print(number_of_books_on_hold())
# Prediction: 5
# Predicted correct!

#4
def number_of_fingers():
    return 5
    print(10)
print(number_of_fingers())
# Prediction: 5
# Prediction correct!


#5
def number_of_great_lakes():
    print(5)
x = number_of_great_lakes()
print(x)
# Prediction: 5
# Prediction incorrect, prints 5 and then None, because the function does not have a return statement!


#6
def add(b,c):
    print(b+c)
print(add(1,2) + add(2,3))
# Prediction: error?
# Prediction somewhat incorrrect, first prints 3 and 5 then you get the error

#7
def concatenate(b,c):
    return str(b)+str(c)
print(concatenate(2,5))
# Prediction: 25
# Prediction correct!


#8
def number_of_oceans_or_fingers_or_continents():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(number_of_oceans_or_fingers_or_continents())
# Prediction: 100, 10
# Prediction correct!


#9
def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
# Prediction: 7, 14, 21
# Prediction correct!

#10
def addition(b,c):
    return b+c
    return 10
print(addition(3,5))
# Prediction: 8
# Prediction correct!


#11
b = 500
print(b)
def foobar():
    b = 300
    print(b)
print(b)
foobar()
print(b)
# Prediction: 500,500,300,500
# Prediction correct!


#12
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
foobar()
print(b)
# Prediction: 500,500, 300, 500
# Prediction correct!


#13
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
b=foobar()
print(b)
# Prediction: 500, 500, 300, 300
# Prediction correct!


#14
def foo():
    print(1)
    bar()
    print(2)
def bar():
    print(3)
foo()
# Prediction: 1,3,2
# Prediction correct!

#15
def foo():
    print(1)
    x = bar()
    print(x)
    return 10
def bar():
    print(3)
    return 5
y = foo()
print(y)
# Prediction: 1, 3, 5, 10
# Prediction correct!