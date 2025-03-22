s=input("enter main string:")
sub=input("enter subs string:")
try:
    n=s.index(sub)
except ValueError:
    print("substring is not found in the main sting")
else:
    print("substring found")        
