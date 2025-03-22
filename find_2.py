s=input("enter main string:")
subs=input("enter subs string:")
flag=False
pos=-1
n=len(s)
while True:
    pos=s.find(subs,pos+1,n)
    if pos == -1:
        break
    print("found at index:",pos)
    flag=True
if flag == False:
    print("not found")  
