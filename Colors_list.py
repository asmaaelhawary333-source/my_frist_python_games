colors=[]
fav_color=input("add the first color you like \n")
colors.append(fav_color)
choice=input("do you want to add more color? (yes,no) \n")
if choice=="yes":
    fav_color=input("add another color you like \n")
    colors.append(fav_color)
    print(f"the color you like{colors}")
else:
    print(f"the color you like :{colors}"
