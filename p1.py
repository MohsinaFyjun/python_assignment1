

n1 = int(input('enter a value:'))
n2 = int(input('enter a value:'))
n3 = int(input('enter a value:'))
list_1 = [n1,n2,n3]
print (" Display the List1", list_1) 

n4 = int(input('enter a value:'))
n5 = int(input('enter a value:'))
n6 = int(input('enter a value:'))
list_2 = [n4,n5,n6]
print (" Display the List1", list_2) 

result = [] # declaration of the list  
for x in range (0, len (list_1)):  
   #result.append( list_1[x] + list_2[x] )
#print ( "Addition of the list list_1 and list_2 is: " + str (result))
   sum = list_1[x] + list_2 [x] #another way..
   result.append(sum)
print ( "Addition of the list list_1 and list_2 is: " + str (result))