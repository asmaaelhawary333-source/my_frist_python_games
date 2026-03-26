your_library=[]
book=input("enter the name of the book you own \n")
your_library.append(book)
book=input(" enter the name of another book you own , or enter to skip \n")
your_library.append(book)
print(f"you have: {your_library}")

wish_list=[]
wish=input(" enter the name of the book you wish \n")
wish_list.append(wish)
wish=input("enter the name of another book you wish ,or enert to skip\n")
wish_list.append(wish)
print(f"your wish list {wish_list}")

acquired_book=input("enter a book from your wish list thatb you have acquired \n")
if acquired_book in wish_list:
    wish_list.remove(acquired_book)
    your_library.append(acquired_book)
print(f"updated library:{your_library}")
print(f"updated wishlist:{wish_list}")
