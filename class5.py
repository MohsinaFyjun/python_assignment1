#dictionary
##list2 = [10, 20, 3.6]

#newvar = dict(zip(list1,list2))
#newvar1 = list(zip(list1,list2))

#a = newvar.get(list[1])
#print(newvar)
#print(newvar1)
#print(a)

#newlist = {'Bangladesh', 'India', 'Japan'}
#newvalue = 'country'

#var_b  = dict.fromkeys(newlist, newvalue)

#mini project
student1 = { 'name': 'meeena', 'age': 22}
a = int(input('please enter the numbers:'))
list = []
for i in range(a):
    var = input('insert student name: ')
    student1['name'] = var
    var_age = input('insert student age: ')
    student1['age'] = var_age
    list.append(student1.copy())
print(list)
