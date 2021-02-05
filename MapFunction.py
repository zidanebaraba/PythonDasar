listItem=[1,2,3,4,5,6,7]
print(listItem)
#tanpa map
tempList=[]
for item in listItem:
    tempList.append(item*2)
print(tempList)

# Dengan map
tempList2=list(map(lambda x:x*2, listItem))
print(tempList2)

tempList3=list(map(lambda x:x+3,listItem))
print(tempList3)
