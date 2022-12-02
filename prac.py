
#TYPE CASTING
print('hello')
myinput = input('enter a value:')
print(type(myinput))
print(myinput)
y = int(myinput)
print(type(y))
print(y)

#taking different data type as an input
list_z = ['apple', 20 , 20.5, True]
tuple_z1 = ('apple', 20 , 20.5, True)
set_z2 = {'apple', 20 , 20.5, True}
print(list_z)
print(tuple_z1)
print(set_z2)
p = range(5)
print(p)

#condition
n = input('enter a value:' )
a = input('enter another value:')
if a>n :
    print('a is greater')
else :
    print('n is greater')

#looping
for a in range(5):
 print(a)