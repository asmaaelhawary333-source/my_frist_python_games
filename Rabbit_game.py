print(" welcome to place the rabbit")
filed=[["☘","☘","☘" ],["☘","☘","☘" ],["☘","☘","☘" ]]
print(f"{filed[0]}\n{filed[1]}\n{filed[2]}")
print(" \n where should the rabbit go? 🐰")
user=input("please chooce a row  \n")
user2=input("please chooce a column \n")
row_index=int(user[0])-1
column_index=int(user2[0])-1
map=[filed[0], filed[1], filed[2]]
map[row_index][column_index]="🐰"
print(f"{filed[0]} \n {filed[1]}\n {filed[2]}")
