availabe_clothes=["shirts","pants","dress","scarfs"]
shopping_cart=[]
print("welcome to fashion store")
print(f"we have {availabe_clothes}")
item1=input("what do you want from our store \n").lower()
if item1 in availabe_clothes:
    shopping_cart.append(item1)
    print("added successfuly")
item2=input("do you want another item ?\n").lower()
if item2 in availabe_clothes:
    shopping_cart.append(item2)
    print("added successfuly")
else:
    print("sorry, we do not have this item")
    
print(f"your item is {shopping_cart}")
