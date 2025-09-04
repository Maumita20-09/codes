h=int(input("Enter the hours:"))
if 1<h<=2:
    print("Price = 100")
elif h<=4:
    print("Price =",100+((h-2)*50))
elif h<=6:
    print("Price =",100+100+((h-4)*60))
else:
    print("Price =",100+200)
