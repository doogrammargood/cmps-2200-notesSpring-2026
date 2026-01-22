x=3
y=(x+7)%6
print(y)
x=y//3
if y>x:
    x+=1
print(x)

#Raise to power
print(4**3)

#increment operator
x=5
x=x+2 #modifies the value of a variable.
print(x)
x+2 #this is different from x+=2 because it doesn't change the value of x.
x=x+2 #This is exactly the same as x+=2.

#/= operator
x=5
x/=3
print(x)

#*= operator
x=5
x*=3
print(x)

#//= operator
x=5
x//=3
print(x)

#**=

'''
This is a docstring
'''
x=4
x**=3
print(x)

#Why not print y on line 3 of the practice quiz.
y=7
print('y')

#types: int, float (decimals), str, ...
print(type(5))
print(type(5.0))
print(type('y'))
print(type(y))
print(type(10//2))
print(10//2)
print(type(type))
print(type(print))