

lt1 = []  # declaration of a list value
 
items = int (input (" Enter total number: "))  
 
print ("Enter the items into List 1 : ")  #entering items
for i in range(1, items + 1):  
    num = int ( input (" Enter the value of %d index is :" %i))  
    lt1.append(num) # insert the items into the list1  
print(lt1)
x = len(lt1) 
print('the len is : ' + str(x))
for i in range (int(x/2)):
    temp = lt1[i]
    lt1[i] = lt1[x-i-1]
    lt1[x-i-1] = temp
print('the reverse list is : ' +str(lt1))