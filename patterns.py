# left *
n=int(input("Enter last row value: "))
for r in range(1,n+1):
    for c in range(1,r+1):
        print("*",end="")
    print()


# up-side down left *
n=int(input("Enter last row value: "))
for r in range(1,n+1):
    for c in range(r,n+1):
        print("*",end="")
    print()

#right *
n=int(input("Enter last row value: "))
for r in range(1,n+1):
    for s in range(n-r,0,-1):
        print(" ",end="")
    for c in range(1,r+1):
        print("*",end="")
    print()

#central *
n=int(input("Enter last row values: "))
for r in range(1,n+1):
    for s in range(n-r,0,-1):
        print(" ",end="")
    for c in range(1,r+1):
        print(" *",end="")
    print()
