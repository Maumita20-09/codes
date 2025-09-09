x=int(input("Enter the side 1:"))
y=int(input("Enter the side 2:"))
z=int(input("Enter the side 3:"))
if x+y<=z or y+z<=x or x+z<=y:
    print("Invalid")
else:
    if x==y==z:
        print("Equilateral Triangle")
    elif x==y or x==z or y==z:
        print("Isoceles Triangle")
    else:
        print("Scalene Triangle")