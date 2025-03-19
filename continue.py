#for i in range (10):
 #   if i % 2 == 0:
  #      continue
   # print(i)


cart=[10,20,500,75,600]
for item in cart:
    if item >= 500:
        print("sorry we canot process this order",item, "insurance must be requred")
        continue
    print("processin item:",item)
