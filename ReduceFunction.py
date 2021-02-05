from functools import reduce
listItem=[1,2,3,4,5,6,7,8,9,10]
print(listItem)
#Tanpa Reduce
sum=0
for item in listItem:
    sum=sum+item
print(sum)

#Dengan Reduce
sum1= reduce(lambda x,y:x+y,listItem)
print(sum1)