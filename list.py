MyList = [[22, 14, 16], ["Joe", "Sam", "Abel"], [True, False, True]]
print(MyList[0])
print(MyList[1])
print(MyList[2])
for objects in MyList:
    print(id(MyList))
MyList[1].append(7)
print(MyList)
