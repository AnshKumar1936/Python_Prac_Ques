# Using Empty List

def Remove(dup):
    list=[]
    for num in dup:
        if num not in list:
            list.append(num)
    return list
     
duple = [2, 4, 10, 20, 5, 2, 20, 4]
print("List without duplicate values:" , Remove(duple))

#--------------------------------------#


#Using Empty List

list = [2, 4, 10, 20, 5, 2, 20, 4]
i=0
while i<len(list):
    item=list[i]
    if list.count(item) > 1:
        list.remove(item)
    else:
        i = i+1
print("List without duplicate values:" , list)
