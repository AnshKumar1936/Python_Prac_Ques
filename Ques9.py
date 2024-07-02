tup = ("hii" , "ok" , 1 , 2 , 1.1 , 1.2)

list = []
for item in tup:
    if isinstance(item, float):
        list.append('XYZ')
    elif isinstance(item, int):
        list.append('XYZ')
    else:
        list.append(item)

tup = tuple(list)

print("Result:", tup)