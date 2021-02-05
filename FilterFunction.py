listItem=[1,2,3,4,5,6,7,8,9,10]
print(listItem)

#tanpa filter
tempList=[]
for item in listItem:
    if (item % 2==0):
        tempList.append(item)
print(tempList)

#Dengan Filter
tempList2= list(filter(lambda x:x % 2==0,listItem))
print(tempList2)