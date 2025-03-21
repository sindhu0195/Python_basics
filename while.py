s=input("Enter some string:")
n=len(s)
i=0
print("data in forward diraction")
while i < n:
    print(s[i],end="")
    i=i+1
print()
print("data in backword direction")
i=n-1
while i >=0:
    print(s[i],end="")
    i=i-1
print()
